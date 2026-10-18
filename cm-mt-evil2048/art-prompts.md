# Evil 2048 — Art Prompts & Raster Assets Documentation

Tài liệu ghi nhận quy trình, prompt AI, thông số và pipeline xử lý đồ họa raster (App Icon, Adaptive Launcher Icon, Feature Graphic) cho game **Evil 2048** (`cm.mt.evil2048`).

---

## 1. Mascot Character Concept

- **Tên nhân vật**: Evil Imp / Tiểu ác ma tím
- **Đặc điểm nhận diện**:
  - Thân hình mập tròn đáng yêu (chubby cute purple devil/imp), màu tím neon (`#9b30ff` / `#b347eb`).
  - Cặp sừng đỏ nhỏ xíu (`#e02040`), cánh dơi nhỏ tím sẫm, đuôi quỷ hình mũi tên nhọn.
  - Khuôn mặt cười ranh mãnh, mắt to hoạt hình, răng nanh nhỏ nhô ra một bên.
  - Viền sticker trắng dày bao quanh toàn bộ nhân vật (sticker aesthetic).
- **Phong cách nghệ thuật**:
  - 3D cartoon candy / mobile puzzle aesthetic (tương tự phong cách của Supercell / Brawl Stars / Candy Crush).
  - Ánh sáng bóng bẩy (glossy highlights), tương phản cao, màu sắc tươi vui hấp dẫn giới trẻ (15–25 tuổi).

---

## 2. App Icon & Launcher Icons

### 2.1. Generation Prompt
- **Tool**: Imagen 3 (`generate_image`)
- **Aspect Ratio**: `1:1`
- **Prompt**:
  > Cute cartoon app icon for mobile puzzle game 'Evil 2048'. A cheeky, adorable chubby purple baby devil mascot with little red horns, tiny bat wings, and a cute pointy devil tail, hugging a glossy 3D golden yellow square candy tile with the number '2048' boldly printed on it in white. Clean thick white sticker border outline around character and tile. Rich dark purple circular vignette background (#16112c). Supercell and Candy Crush art style, playful mischievous expression, high contrast, vibrant saturated colors, soft lighting, 3D vector aesthetic.

### 2.2. Post-Processing Pipeline (`Pillow`)
1. **Mascot Alpha Masking**:
   - Tách nền bằng floodfill từ tọa độ biên ngoài qua dải màu nền tối (`#181331` / `R<60, G<50, B<80`).
   - Lọc component trung tâm kết hợp bounding box, làm mịn mép bằng Gaussian blur (`sigma=0.8`).
   - Kết quả là sprite mascot ôm khối 2048 viền sticker trắng trong suốt sắc nét.

2. **Play Store App Icon** (`playstore/cm-mt-evil2048/playstore-app-icon.png`):
   - Kích thước: `512 × 512 px`, 24-bit RGB PNG.
   - Nền: Gradient xuyên tâm từ tím đậm `#2a1c50` ở tâm ra tím đen `#140f28` ở các góc.
   - Mascot: Thu phóng vừa vặn `415 px`, căn giữa hoàn hảo kèm đổ bóng mờ (drop shadow `sigma=10`, alpha `140`).
   - Khoảng đệm an toàn: ~48px từ mép ngoài, đảm bảo khi Google Play bo góc tự động (squircle) không bị chạm viền sticker.

3. **Android Adaptive Icons** (`games/cm.mt.evil2048/assets/icon/`):
   - `adaptive_bg.png`: `432 × 432 px` RGB, nền tím sẫm đồng nhất `#16112c`.
   - `adaptive_fg.png`: `432 × 432 px` RGBA trong suốt.
   - **Vùng an toàn (Safe Zone)**: Đường kính 264px (bán kính 132px tính từ tâm `(216, 216)`).
   - Mascot được tính toán scale tự động để bán kính xa nhất từ tâm đạt tối đa `127.6px` (< `132px`). Cam kết 100% không bị cắt phạm vi trên mọi launcher Android (tròn, squircle, giọt nước, pebble).

4. **Project Icon** (`games/cm.mt.evil2048/assets/icon/icon_192.png`):
   - Kích thước: `192 × 192 px`, RGBA.
   - Dùng cho launcher Android cũ (< 8.0) và icon cửa sổ / Godot editor.

---

## 3. Feature Graphic (Ảnh bìa Google Play)

### 3.1. Thông số kỹ thuật
- Đường dẫn: `playstore/cm-mt-evil2048/feature-image.png`
- Kích thước: `1024 × 500 px`, 24-bit RGB PNG (không có kênh alpha, dung lượng < 15MB).

### 3.2. Generation Prompt
- **Tool**: Imagen 3 (`generate_image`)
- **Aspect Ratio**: `16:9`
- **Prompt**:
  > Cartoon mobile game feature banner illustration, landscape banner. On the right side, a cute chubby purple baby devil mascot with little red horns, tiny bat wings, cute devil tail, smiling cheekily. Floating around are glossy 3D candy-like number tiles (2, 4, 8, 16, 2048) in vibrant candy colors (golden yellow, cyan, hot pink, orange) with playful sparks and yellow starbursts. Deep dark navy purple gaming background (#16112c) with soft purple radial vignette and subtle comic rays. The left half is relatively open with dark background space. Vibrant cute mobile puzzle game banner art, Supercell and Candy Crush style, bold clean lighting.

### 3.3. Typography & Compositing Pipeline
- **Font chữ**: `Baloo 2 ExtraBold` (`shared-assets/fonts/Baloo2-Variable.ttf`).
- **Xử lý đồ họa chữ "EVIL 2048"**:
  - **Chữ "EVIL"**:
    - Font size: `138px`. Góc nghiêng: `-3°`.
    - Gradient bề mặt: Hồng neon `#ff78b9` (đỉnh) → Đỏ hồng tươi `#ff2373` (giữa) → Hồng ngọc sẫm `#c30a50` (đáy).
    - Vệt bóng sáng trắng (inner shine) 45% nửa trên.
    - Hiệu ứng vát khối 3D (extrude): màu rượu chát sẫm `#320c28` dày `11px`.
    - Viền sticker trắng dày `13px` bao bọc bên ngoài.
  - **Số "2048"**:
    - Font size: `150px`. Góc nghiêng: `+2°`.
    - Gradient bề mặt: Vàng chanh sáng `#fffab2` (đỉnh) → Vàng kẹo ngọt `#ffc314` (giữa) → Cam tươi `#f07d00` (đáy).
    - Vệt bóng sáng trắng (inner shine) 45% nửa trên.
    - Hiệu ứng vát khối 3D (extrude): màu nâu cam sẫm `#4b2805` dày `13px`.
    - Viền sticker trắng dày `13px` bao bọc bên ngoài.
  - **Hiệu ứng đổ bóng & Ánh sáng nền (Back Glow)**:
    - Bầu sáng tím hào quang (radial purple aura `#5f2396`) tỏa nhẹ phía sau cụm chữ trên nền tia comic tối, giúp toàn bộ tiêu đề nổi bật rõ ràng, đọc tốt ngay cả ở kích thước xem trước thu nhỏ trên điện thoại.

---

## 4. Tích hợp trong cấu hình dự án

1. **`export_presets.cfg`**:
   ```ini
   launcher_icons/main_192x192="res://assets/icon/icon_192.png"
   launcher_icons/adaptive_foreground_432x432="res://assets/icon/adaptive_fg.png"
   launcher_icons/adaptive_background_432x432="res://assets/icon/adaptive_bg.png"
   launcher_icons/adaptive_monochrome_432x432=""
   ```

2. **`project.godot`**:
   ```ini
   boot_splash/bg_color=Color(0.0862745, 0.0666667, 0.172549, 1)
   config/icon="res://assets/icon/icon_192.png"
   ```
