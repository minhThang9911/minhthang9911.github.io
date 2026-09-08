# Prompt sinh ảnh cho Tính Lãi Vay (home.free.laisuat)

Dán vào Google Nano Banana (gemini.google.com hoặc aistudio.google.com).
Sinh 3–4 biến thể mỗi prompt rồi chọn.

**Màu chủ đạo lấy từ code** (`LaiSuatApp.seed` trong `lib/main.dart`):
indigo `#303F9F` → indigo đậm `#1A237E`. Giữ nguyên mã hex trong prompt để
icon khớp giao diện app.

Sau khi có ảnh, áp icon bằng một lệnh:

```bash
python3 assets-shared/icons/apply_icon.py laisuat <đường-dẫn-ảnh-icon>.png
```

---

## A. APP ICON — bản chính (khuyên dùng)

Ý tưởng: **đồng tiền bị cắt một miếng** — đúng thông điệp của app: số tiền ký
trên hợp đồng và số tiền thật sự cầm về không giống nhau.

```
App icon for a loan interest calculator app. A bold white coin seen head-on
with a clean wedge slice cut out of its right side and the slice floating
slightly away, revealing that part of the money is taken before you receive
it; a small white percent sign sits centered on the coin face. Minimal flat
vector style with subtle depth and soft inner shadows. Background: smooth
diagonal gradient from indigo #303F9F to deep indigo #1A237E. Centered
composition, the symbol fills 68% of the frame, crisp clean edges, high
contrast, trustworthy financial mood, professional Play Store app icon,
square 1:1, full-bleed background with no rounded corners, no text, no
numbers, no letters, no watermark, no phone mockup.
```

## B. APP ICON — biến thể: phần trăm + biểu đồ cột giảm dần

Bám sát hình ảnh trong app (biểu đồ gốc/lãi ở màn lịch trả nợ).

```
App icon for a loan and interest calculator app. A bold white percent sign
standing in front of three descending bar-chart columns, the bars shrinking
from left to right to suggest a shrinking loan balance, drawn as one clean
white silhouette. Minimal flat vector style, clean geometric shapes with
subtle depth. Background: smooth diagonal gradient from indigo #303F9F to
deep indigo #1A237E. Centered composition, symbol fills 65% of the frame,
crisp edges, instantly readable at small size, professional Play Store app
icon, square 1:1, full-bleed background, no rounded corners, no text, no
numbers, no letters, no watermark.
```

## C. APP ICON — biến thể 3D clay (đang thịnh trên Play VN)

```
App icon for a loan calculator app, cute 3D clay render style with soft
studio lighting and gentle shadows. A rounded matte white coin with a wedge
slice removed, resting at a slight angle on a small stack of two rounded
clay coins, tactile plasticine material, subtle indigo rim light. Background:
smooth diagonal gradient from indigo #303F9F to deep indigo #1A237E. Centered
composition, the object fills 65% of the frame, soft realistic shadows,
friendly trustworthy mood, professional Play Store app icon, square 1:1,
full-bleed background, no rounded corners, no text, no letters, no watermark.
```

---

## D. FEATURE GRAPHIC 1024×500 — bản chính

```
Wide 1024x500 mobile app store feature banner, landscape 2:1. On the left
third, a large white coin with a wedge slice cut out and floating away, with
a soft glowing percent sign beside it; across the middle, a row of white
bar-chart columns descending from left to right, gradually fading out.
Background: smooth horizontal gradient from indigo #303F9F on the left to
deep indigo #1A237E on the right, with a very faint ledger-grid pattern
fading into the background. The right third is clean empty gradient space for
a title. Modern premium flat vector illustration with soft glow and gentle
depth, trustworthy financial mood. Key elements inside the central 80% safe
zone. No text, no numbers, no letters, no watermark, no phone mockup, no
store badges.
```

## E. FEATURE GRAPHIC — biến thể gọn (an toàn khi Play crop mép)

```
Wide 1024x500 mobile app store feature banner, landscape 2:1. A single bold
white coin with a wedge slice removed, floating on the left third with a soft
glow, and three thin white horizontal light streaks trailing to the right
like rows of a ledger. Background: smooth horizontal gradient from indigo
#303F9F to deep indigo #1A237E. The right two thirds is clean empty gradient
space for a title. Modern premium flat vector illustration, crisp edges, soft
glow. Key elements inside the central 80% safe zone. No text, no letters, no
numbers, no watermark, no phone mockup.
```

---

## Lưu ý khi dùng

- **Đừng để AI viết chữ "Tính Lãi Vay"** — Nano Banana hay sai dấu tiếng Việt.
  Sinh ảnh không chữ rồi thêm tên bằng Canva/Figma với font **Be Vietnam Pro**
  (đã có sẵn trong `res/font` của bộ app), đặt vào 1/3 phải nơi prompt chừa sẵn.
- Nếu kết quả lòi chữ hoặc khung điện thoại, thêm cuối prompt:
  `Absolutely no text, no letters, no phone mockup, no watermark.`
- **Icon**: xuất 512×512 PNG, **không bo góc** (Play tự bo). `apply_icon.py`
  lo phần bo góc cho launcher.
- **Feature graphic**: đúng **1024×500**, PNG 24-bit hoặc JPG, **không kênh
  alpha**.
- Đặt file vào thư mục này với đúng tên `icon.png` và `play-feature-image.png`
  thì trang privacy tự nhận (nó nhúng theo đường dẫn tương đối).

## Vì sao chọn hình "đồng tiền bị cắt"

Cả 16 app trong bộ đang dùng glyph tả **chức năng** (thước thuỷ, la bàn, sổ…).
App này chọn tả **vấn đề** thay vì chức năng, vì thứ khiến người ta tải về
không phải "máy tính lãi" — chỗ nào chẳng có — mà là câu hỏi *"sao tôi vay
500 triệu mà chỉ cầm về 460?"*. Đồng tiền khuyết một miếng nói đúng câu đó mà
không cần chữ, và không đụng hàng với bất kỳ icon nào trong bộ.
