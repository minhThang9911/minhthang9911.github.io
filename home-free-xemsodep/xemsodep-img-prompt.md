# Prompt sinh ảnh cho Xem Số Đẹp (home.free.xemsodep)

Dán vào Google Nano Banana (gemini.google.com hoặc aistudio.google.com).
Sinh 3–4 biến thể mỗi prompt rồi chọn.

**Màu chủ đạo lấy từ code** (`seedColor: const Color(0xFF880E4F)` trong `lib/main.dart`):
đỏ đô `#880E4F` → đỏ rượu trầm `#4A0025`. Giữ nguyên mã hex trong prompt để icon khớp giao diện app.

Sau khi có ảnh, áp icon bằng một lệnh:

```bash
python3 assets-shared/icons/apply_icon.py xemsodep <đường-dẫn-ảnh-icon>.png
```

Icon hiện tại là **icon hình học tạm** sinh bằng `gen_icons.py xemsodep`.
Chạy script xoá watermark của Nano Banana (nếu có) trước khi áp:

```bash
python3 assets-shared/icons/remove_watermark.py <ảnh.png>
```

---

## A. APP ICON — bản chính (khuyên dùng)

Ý tưởng: **Vòng tròn phong thuỷ với quẻ Kinh Dịch bằng vàng kim trên nền đỏ đô sang trọng, kết hợp các chữ số phát sáng tinh tế** — thể hiện sự minh bạch, chuẩn xác và đậm nét phong thuỷ Á Đông.

```
App icon for a Vietnamese numerology and feng shui phone number analyzer app. A circular golden oriental medallion set against a deep wine red background #880E4F to dark burgundy #4A0025. Inside the medallion, an elegant, crisp I Ching trigram (Li hexagram / Fire trigram symbolizing clarity and light) crafted from polished gold, surrounded by subtle glowing numeric digits arranged in a balanced geometric circle. Flat minimal vector aesthetic with soft ambient occlusion and premium metallic gold highlights, no clutter, no text, no letters. Centered composition, icon symbol fills 72% of the frame, square 1:1, no rounded corner mask.
```

## B. APP ICON — biến thể 2 (Bát quái & Bàn phím số)

```
App icon for a feng shui mobile number analyzer app. A stylized minimalist smartphone dial pad grid seamlessly merging into an ancient octagonal Bagua symbol. Clean pure white and gold lines, minimalist, flat vector with subtle soft shadows. Background: rich burgundy gradient #880E4F to deep dark maroon #4A0025. Square 1:1, centered, symbol fills 70%, no corner mask, no text.
```

## C. APP ICON — biến thể 3 (Quẻ Dịch & Thẻ phong thuỷ)

```
App icon for a Vietnamese phone number feng shui app. A sleek modern square jade/gold talisman inscribed with ancient I Ching hexagram lines and lucky Asian numbers (6, 8, 9). Minimal vector, elegant luxury design, high contrast. Background: smooth diagonal gradient from deep ruby red #880E4F to dark mahogany. Square 1:1, centered, no text, no corner mask.
```

---

## D. FEATURE GRAPHIC 1024×500

```
Google Play feature graphic, 1024x500 banner, for a Vietnamese phone number feng shui analyzer app. Left third: a glowing gold circular oriental medallion featuring clear I Ching hexagram lines and subtle geometric numbers, radiating soft elegant light. Right two thirds: calm, clean space reserved for promotional text. Background: rich horizontal gradient from wine red #880E4F to dark burgundy #4A0025 with faint, delicate watermark patterns of ancient celestial constellations and Lo Shu magic square grid. Flat vector, luxury oriental style, high contrast, wide banner composition, no text in the image itself.
```

Feature graphic tạm đang dùng sinh bằng:

```bash
python3 assets-shared/icons/gen_feature.py xemsodep
```
