"""Dựng gói dữ liệu offline cho app Tra Cứu Thuốc.

Cào lịch sự hai cổng công khai của Bộ Y tế (cùng API ABP):
  - Cục Quản lý Dược               dichvucong.dav.gov.vn         (~55.000 thuốc)
  - Cục Quản lý Y, Dược cổ truyền  ydct-dichvucong.moh.gov.vn    (~4.200 thuốc)
mỗi lần MỘT yêu cầu, 1.000 dòng/trang, nghỉ giữa các yêu cầu. Chỉ giữ các trường
app dùng, gộp thuốc trùng SĐK giữa hai nguồn theo đúng quy tắc của app
(lib/models/thuoc.dart · Thuoc.gopVoi), rồi ghi SQLite + chỉ mục FTS5 và nén gzip.

Kế hoạch: docs/plans/tracuuthuoc-offline.md

Chạy:
  python3 tools/tracuuthuoc_data/snapshot.py --out build/tracuuthuoc_data
  python3 tools/tracuuthuoc_data/snapshot.py --out … --cache …/raw   # dùng lại trang đã tải
Chỉ dùng thư viện chuẩn của Python (sqlite3 phải có FTS5).
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import re
import shutil
import sqlite3
import ssl
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

SCHEMA_VERSION = 1
PAGE = 1000  # tối đa API cho phép
PAUSE_S = 2.0  # nghỉ giữa hai yêu cầu
TIMEOUT_S = 120
USER_AGENT = (
    "TraCuuThuoc-data/1.0 "
    "(+https://minhthang9911.github.io/home-free-tracuuthuoc/privacy-policy.html)"
)
PATH = "/api/services/app/soDangKy/GetAllPublicServerPaging"
SOURCES = {
    "qld": "dichvucong.dav.gov.vn",
    "ydct": "ydct-dichvucong.moh.gov.vn",
}

# Trường app đọc (Thuoc trong lib/models/thuoc.dart). Thêm getter mới ở app thì
# thêm vào đây, nếu không bản offline sẽ thiếu.
KEEP_TOP = [
    "soDangKy", "soDangKyCu", "tenThuoc", "isHetHan", "isDaRutSoDangKy",
    "hoatChatChinh", "tenCongTyDangKy", "diaChiDangKy", "nuocDangKy",
    "tenCongTySanXuat", "diaChiSanXuat", "nuocSanXuat",
    "thongTinDangKyThuoc", "thongTinRutSoDangKy", "thongTinTaiLieu",
    "thuocKiemSoatDacBiet",
]
KEEP_COBAN = [
    "hoatChatChinh", "hamLuong", "dangBaoChe", "dongGoi", "tieuChuan",
    "tuoiTho", "tenDuongDung",
]
KEEP_CONGTY = [
    "tenCongTyDangKy", "diaChiDangKy", "nuocDangKy",
    "tenCongTySanXuat", "diaChiSanXuat", "nuocSanXuat",
]


# Cổng YDCT (F5 BIG-IP) chọn DHE với khoá DH quá ngắn khi gặp danh sách mã hoá
# mặc định của Python → OpenSSL từ chối (DH_KEY_TOO_SMALL). Chỉ dùng ECDHE: máy
# chủ có hỗ trợ, và đó cũng là thứ app Dart/curl tự chọn.
TLS = ssl.create_default_context()
TLS.set_ciphers("ECDHE+AESGCM:ECDHE+CHACHA20:ECDHE+AES:!aNULL:!DHE")


def log(*a: object) -> None:
    print(*a, file=sys.stderr, flush=True)


# --------------------------------------------------------------------------- cào
def fetch_page(host: str, skip: int) -> dict:
    body = json.dumps({
        "SoDangKyThuoc": {}, "KichHoat": True,
        "skipCount": skip, "maxResultCount": PAGE, "sorting": None,
    }).encode()
    req = urllib.request.Request(
        f"https://{host}{PATH}", data=body, method="POST",
        headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
    )
    delay = 10.0
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_S, context=TLS) as r:
                obj = json.loads(r.read().decode("utf-8"))
            result = obj.get("result")
            if not isinstance(result, dict) or not isinstance(result.get("items"), list):
                raise ValueError(f"cấu trúc lạ: {str(obj)[:200]}")
            return result
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            if isinstance(getattr(e, 'reason', None), ssl.SSLError):
                raise  # lỗi TLS không tự khỏi khi thử lại
            code = getattr(e, "code", None)
            if code is not None and 400 <= code < 500 and code != 429:
                raise
            retry_after = getattr(e, "headers", None) and e.headers.get("Retry-After")
            wait = float(retry_after) if retry_after and retry_after.isdigit() else delay
            log(f"  {host} skip={skip} lỗi ({e}); thử lại sau {wait:.0f} s")
            time.sleep(wait)
            delay *= 2
    raise RuntimeError(f"{host} skip={skip}: hỏng 5 lần liền, dừng.")


def crawl(name: str, host: str, cache: Path | None) -> list[dict]:
    """Tải hết một nguồn. Thứ tự API là id giảm dần; thuốc mới chèn vào giữa
    lúc đang cào làm trang sau lặp vài dòng → bỏ trùng theo id."""
    items: dict[object, dict] = {}
    skip, total = 0, None
    while total is None or skip < total:
        f = cache / f"{name}_{skip:06d}.json" if cache else None
        if f and f.exists():
            result = json.loads(f.read_text())
        else:
            t0 = time.monotonic()
            result = fetch_page(host, skip)
            log(f"  {name} skip={skip:>6} {len(result['items'])} dòng "
                f"{time.monotonic() - t0:.1f} s")
            if f:
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text(json.dumps(result, ensure_ascii=False))
            time.sleep(PAUSE_S)
        total = result.get("totalCount") or 0
        page = result["items"]
        if not page:
            break
        for it in page:
            items[it.get("id", id(it))] = it
        skip += len(page)
    log(f"{name}: {len(items)} bản ghi (API báo {total})")
    if total and len(items) < total * 0.98:
        raise RuntimeError(f"{name}: chỉ lấy được {len(items)}/{total}, dừng.")
    return list(items.values())


# ------------------------------------------------------------------ rút gọn, gộp
def strip(o):
    if isinstance(o, dict):
        r = {k: strip(v) for k, v in o.items()}
        return {k: v for k, v in r.items() if v not in (None, "", [], {}, False)}
    if isinstance(o, list):
        return [strip(x) for x in o]
    if isinstance(o, str):
        return o.strip()
    return o


def project(it: dict, source: str) -> dict:
    o = {k: it.get(k) for k in KEEP_TOP}
    o["soDangKy"] = re.sub(r"\s+", "", it.get("soDangKy") or "")
    o["soDangKyCu"] = re.sub(r"\s+", "", it.get("soDangKyCu") or "")
    o["thongTinThuocCoBan"] = {
        k: (it.get("thongTinThuocCoBan") or {}).get(k) for k in KEEP_COBAN}
    for c in ("congTyDangKy", "congTySanXuat"):
        o[c] = {k: (it.get(c) or {}).get(k) for k in KEEP_CONGTY}
    o = strip(o)
    if source != "qld":
        o["_nguon"] = source
    return o


def het_han(o: dict) -> str:
    return ((o.get("thongTinDangKyThuoc") or {}).get("ngayHetHanSoDangKy") or "")[:10]


def merge(qld: list[dict], ydct: list[dict]) -> list[dict]:
    """Như Thuoc.gopVoi: trùng SĐK giữa HAI nguồn thì giữ bản QLD, lấy phần
    đăng ký của bản hết hạn muộn hơn. Trùng trong cùng nguồn thì giữ cả hai."""
    out = list(qld)
    first: dict[str, int] = {}
    for i, o in enumerate(out):
        k = o.get("soDangKy", "").upper()
        if k:
            first.setdefault(k, i)
    merged = 0
    for o in ydct:
        k = o.get("soDangKy", "").upper()
        i = first.get(k) if k else None
        if i is None or out[i].get("_gop"):
            out.append(o)
            continue
        goc = dict(out[i])
        a, b = het_han(goc), het_han(o)
        if b and (not a or b > a):
            goc["thongTinDangKyThuoc"] = o.get("thongTinDangKyThuoc")
            if o.get("isHetHan"):
                goc["isHetHan"] = True
            else:
                goc.pop("isHetHan", None)
            goc["_hanTu"] = "ydct"
        goc["_gop"] = True
        out[i] = goc
        merged += 1
    log(f"gộp: {merged} thuốc có ở cả hai nguồn")
    return out


# ------------------------------------------------------------------------ SQLite
def fold(s: str) -> str:
    """Bỏ dấu tiếng Việt, đ→d, chữ thường. App phải chuẩn hoá từ khoá y hệt."""
    s = s.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.lower()


def search_text(o: dict) -> tuple[str, str, str, str]:
    cb = o.get("thongTinThuocCoBan") or {}
    ct_dk = o.get("congTyDangKy") or {}
    ct_sx = o.get("congTySanXuat") or {}
    sdk = " ".join(x for x in (o.get("soDangKy"), o.get("soDangKyCu")) if x)
    ten = o.get("tenThuoc", "")
    hoat_chat = cb.get("hoatChatChinh") or o.get("hoatChatChinh") or ""
    cong_ty = " ".join(dict.fromkeys(x for x in (
        o.get("tenCongTyDangKy"), ct_dk.get("tenCongTyDangKy"),
        o.get("tenCongTySanXuat"), ct_sx.get("tenCongTySanXuat")) if x))
    return tuple(fold(x) for x in (sdk, ten, hoat_chat, cong_ty))  # type: ignore


def build_db(rows: list[dict], path: Path, meta: dict) -> None:
    path.unlink(missing_ok=True)
    db = sqlite3.connect(path)
    db.executescript("""
        PRAGMA page_size = 4096;
        CREATE TABLE meta (k TEXT PRIMARY KEY, v TEXT NOT NULL);
        CREATE TABLE thuoc (
          id   INTEGER PRIMARY KEY,
          khoa TEXT NOT NULL,          -- SĐK bỏ khoảng trắng, viết hoa
          json TEXT NOT NULL           -- đọc lại bằng Thuoc(json) trong app
        );
        CREATE INDEX thuoc_khoa ON thuoc(khoa);
        -- Đã bỏ dấu sẵn (fold): unicode61 không coi đ là d có dấu.
        CREATE VIRTUAL TABLE thuoc_fts USING fts5(
          sdk, ten, hoat_chat, cong_ty,
          content='', tokenize='unicode61'
        );
        -- Không thêm prefix='2 3': nặng thêm 8,5 MB (+2,7 MB nén) mà truy vấn
        -- tiền tố "từ"* vẫn < 5 ms (đo Pha 0, 28/11/2026).
    """)
    with db:
        for i, o in enumerate(rows, 1):
            db.execute("INSERT INTO thuoc VALUES (?,?,?)", (
                i, o.get("soDangKy", "").upper(),
                json.dumps(o, ensure_ascii=False, separators=(",", ":"))))
            db.execute("INSERT INTO thuoc_fts(rowid, sdk, ten, hoat_chat, cong_ty) "
                       "VALUES (?,?,?,?,?)", (i, *search_text(o)))
        db.executemany("INSERT INTO meta VALUES (?,?)",
                       [(k, str(v)) for k, v in meta.items()])
    db.execute("INSERT INTO thuoc_fts(thuoc_fts) VALUES ('optimize')")
    db.commit()
    db.execute("VACUUM")
    db.close()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--cache", type=Path, help="thư mục lưu/đọc lại trang thô")
    ap.add_argument("--previous", type=Path,
                    help="manifest.json bản trước; tụt quá 5%% số thuốc thì dừng")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    t0 = time.monotonic()
    raw = {name: crawl(name, host, args.cache) for name, host in SOURCES.items()}
    crawl_s = time.monotonic() - t0

    # Thiếu SĐK nhiều bất thường → API đổi tên trường. (Không xét tên: 28/11/2026
    # bên YDCT có 605/4.243 bản ghi thật sự không có tên, bên QLD 0.)
    for name, items in raw.items():
        bad = sum(1 for x in items if not (x.get("soDangKy") or "").strip())
        if bad > len(items) * 0.02:
            raise RuntimeError(f"{name}: {bad}/{len(items)} bản ghi thiếu SĐK — "
                               "API có thể đã đổi cấu trúc, không đăng gói.")

    qld = [project(x, "qld") for x in raw["qld"]]
    ydct = [project(x, "ydct") for x in raw["ydct"]]
    rows = merge(qld, ydct)

    if args.previous and args.previous.exists():
        prev = json.loads(args.previous.read_text())
        for k, n in (("count_qld", len(qld)), ("count_ydct", len(ydct))):
            old = int(prev.get(k, 0))
            if old and n < old * 0.95:
                raise RuntimeError(f"{k}: {n} < 95% bản trước ({old}) — không đăng gói.")
        log(f"so với bản {prev.get('created')}: qld {prev.get('count_qld')}→{len(qld)}, "
            f"ydct {prev.get('count_ydct')}→{len(ydct)}")

    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=7)))
    stamp = now.strftime("%Y%m%d")
    meta = {
        "schema": SCHEMA_VERSION,
        "created": now.isoformat(timespec="seconds"),
        "count": len(rows),
        "count_qld": len(qld),
        "count_ydct": len(ydct),
    }
    db_path = args.out / f"tracuuthuoc-{stamp}.db"
    build_db(rows, db_path, meta)

    gz_path = db_path.with_suffix(".db.gz")
    with db_path.open("rb") as src, gzip.open(gz_path, "wb", compresslevel=9) as dst:
        shutil.copyfileobj(src, dst)
    sha = hashlib.sha256(gz_path.read_bytes()).hexdigest()
    manifest = {
        **meta,
        "file": gz_path.name,
        "size": gz_path.stat().st_size,
        "sha256": sha,
        "db_size": db_path.stat().st_size,
    }
    (args.out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    log(f"xong sau {time.monotonic() - t0:.0f} s (cào {crawl_s:.0f} s): "
        f"{len(rows)} thuốc, DB {manifest['db_size'] / 1e6:.1f} MB, "
        f"gzip {manifest['size'] / 1e6:.1f} MB")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
