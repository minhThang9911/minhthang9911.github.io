# Ảnh gốc AI cho Tile Match (không đóng vào APK)

- `single/<name>.png` (hoặc `tile_<name>.png`) — icon lẻ 2048×2048, nền trắng — ĐÃ CÓ 36 file. `app-icon-2048.png`, `feature-2976x1440.png`, `bg_pattern-2048.png` là ảnh gốc của icon app / feature / nền. Tên theo bảng trong `plan/tile-match-icon-procedural-prompts.md`.
- `sheets/sheet_NN.png` + `sheets/sheet_NN.txt` — bảng 3×3 và 9 tên theo hàng (trái→phải, trên→dưới).

Sau khi bỏ ảnh vào: chạy ở root repo
    ./scripts/tile-icons-import.sh
→ cắt sheet (nếu có), resize 256×256, ghi vào `games/cm.mt.tilematch/assets/tiles/tile_<name>.png`.
`single/` ưu tiên hơn `sheets/` khi trùng tên.
