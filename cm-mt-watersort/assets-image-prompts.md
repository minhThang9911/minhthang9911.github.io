# Water Sort — Assets & Art Prompts Documentation

Tài liệu phân tích hình ảnh nghệ thuật từ `feature-image.png`, đề xuất kiến trúc đồ họa và tập hợp các **AI Prompts** chi tiết để tạo bộ assets (ống nghiệm, mặt nước, dòng chảy, hiệu ứng hạt lấp lánh) bằng **Google Banana (ImageFX / Imagen)** cho game **Water Sort** (`cm.mt.watersort`).

---

## 1. Phân tích chi tiết `feature-image.png`

| Thành phần | Đặc điểm thị giác trong `feature-image.png` | Cách thể hiện trong Godot |
|---|---|---|
| **Vỏ ống nghiệm (Test Tube)** | • Viền ngoài dày, đậm màu (dark chocolate / navy đen ~6px) tạo cảm giác sticker nổi khối 2D cao cấp.<br>• Miệng ống có vành bo tròn (collar/lip) mở rộng nhẹ ra hai bên, có viền highlight trắng xanh.<br>• Thân ống có vệt phản quang (specular shine) màu trắng-cyan sắc nét chạy dọc mép trái.<br>• Đáy ống bo tròn U-bottom bán nguyệt hoàn hảo. | Sử dụng sprite lớp phủ `tube_glass_front.png` đè lên trên các lớp nước; hoặc vẽ vector kết hợp shader kính. |
| **Nước trong ống (Liquid Layers)** | • Màu sắc tươi sáng, bão hoà cao phong cách hoạt hình (Đỏ, Xanh dương, Xanh lá, Vàng, Cam).<br>• Lớp nước đáy uốn cong ôm khít theo đáy U của ống.<br>• Khi ống đứng yên: các lớp xếp phẳng nằm ngang, có viền mép khum nhẹ.<br>• **Khi ống nghiêng rót**: mặt nước lớp trên cùng nghiêng theo trọng lực hướng về phía miệng ống, tạo cảm giác chất lỏng tự nhiên thay vì một khối cứng. | `CanvasGroup` hoặc `Polygon2D` được mask trong lòng ống. Tính toán góc nghiêng mặt nước (`tilt_angle`) khi ống xoay. |
| **Dòng rót nước (Pour Stream)** | • Dòng nước có **thể tích** (bề dày ~18–24px), liền mạch như dải ruy-băng chất lỏng chứ không phải sợi chỉ mảnh.<br>• Uốn cong mềm mại từ mép trong miệng ống nghiêng, vồng nhẹ lên rồi đổ thẳng xuống ống nhận.<br>• Bo góc tròn mượt mà ở điểm xuất phát và điểm tiếp xúc. | Đường cong Bezier bậc 2 (`Polygon2D` hoặc `Line2D` dày viền bo tròn) với texture chất lỏng đồng màu. |
| **Mặt nước ống nhận (Splash / Surge)** | • Khi nước đổ vào, mặt nước ống nhận không phẳng lì mà **dâng sóng / tạo gợn splash nhô lên ở mép** theo lực va đập của dòng nước. | Tween dao động sóng nước (wave oscillation) hoặc polygon nước gợn sóng khi nhận dòng chảy. |
| **Hiệu ứng lấp lánh (Sparkles ✨)** | • Ngôi sao 4 cánh (✦) màu trắng tinh khiết, phát sáng nhẹ quanh miệng ống rót và lơ lửng trong ống đã đầy nước. | `CPUParticles2D` phát hạt `sparkle.png` tại đỉnh dòng rót và khi hoàn thành ống. |

---

## 2. Kiến trúc tích hợp vào Godot 4.7

Để đạt được chất lượng đồ họa như trong ảnh mà vẫn đảm bảo hiệu năng 60 FPS mượt mà trên mọi thiết bị Android:

```
TubeView (Node2D)
├── ShadowSprite          # Bóng đổ elip mềm dưới chân ống (đậm dần khi đặt xuống, mờ dần khi nhấc lên)
├── TubeBackSprite        # Mặt lưng kính trong mờ (tube_glass_back.png)
├── LiquidMaskContainer   # CanvasGroup / ClipChildren mask theo lòng ống (tube_mask.png)
│   ├── LiquidLayers      # Các lớp màu (Polygon2D / ColorRect bo đáy)
│   └── DynamicSloshTop   # Đỉnh nước tự do: xoay góc đối ứng khi ống nghiêng
├── TubeFrontSprite       # Vỏ kính phía trước (tube_glass_front.png: vành miệng + vệt sáng kính + viền đen)
├── SparkleEmitter        # CPUParticles2D bắn sao 4 cánh khi hoàn thành
└── CompleteCheckmark     # Huy hiệu ✓ vàng sáng hoặc nút bần (cork) đậy miệng ống
```

Dòng nước rót (`board_view.gd`):
- Sử dụng dải dầy Bezier (`Line2D` bề rộng 20–24px, bo góc tròn `round_cap`) nối từ miệng ống nghiêng xuống tâm ống nhận.
- Kết hợp `CPUParticles2D` tại điểm rót nước với hạt sao lấp lánh `sparkle.png`.

---

## 3. Danh sách AI Prompts cho Google Banana (ImageFX / Imagen)

> **Mẹo tạo ảnh:** 
> - Sao chép nguyên văn prompt tiếng Anh bên dưới vào ô nhập của **Google Banana / ImageFX**.
> - Chọn tỉ lệ khung hình (Aspect Ratio) theo chỉ dẫn của từng prompt.
> - Sau khi tạo, tải ảnh PNG gốc độ phân giải cao về lưu vào thư mục `playstore/cm-mt-watersort/art-src/`.

---

### Prompt 1: Vỏ ống nghiệm thủy tinh (Test Tube Glass Frame - Front Overlay)

*Dùng để làm lớp viền mặt trước của ống nghiệm, bao gồm vành miệng, vệt sáng bóng thuỷ tinh dọc thân và viền đen dày.*

- **Aspect Ratio**: `1:1` hoặc `9:16`
- **Tên file mục tiêu**: `tube_glass_front.png`
- **Prompt**:
```text
A single 2D cartoon test tube glass container for mobile puzzle game, vertical orientation, isolated on solid pure white background. Thick bold dark outline, rounded cylindrical body with a smooth hemispherical U-shaped bottom. At the top, a prominent rounded glass lip rim collar that slightly widens outward with bright white-cyan specular highlight reflections. Down the left inner edge of the tube, a crisp vertical glossy white glass reflection stripe. Fully transparent interior body ready for liquid, clean vector art style, high contrast, smooth clean edges, mobile game asset, flat 2D vector graphic with glossy 3D highlights, no shadow on the floor, perfectly centered.
```

---

### Prompt 2: Ống nghiệm hoàn chỉnh chứa nước màu (Reference & Concept Sheet)

*Dùng làm ảnh tham chiếu tổng thể và kiểm tra độ tương phản giữa các tầng màu và vỏ kính.*

- **Aspect Ratio**: `1:1` hoặc `3:4`
- **Tên file mục tiêu**: `tube_concept_reference.png`
- **Prompt**:
```text
A row of four 2D cartoon glass test tubes filled with colorful liquid layers for a mobile sorting puzzle game, isolated on solid dark navy background (#161b2e). Each test tube has a thick smooth dark border, a glossy rounded white glass lip at the top, a vertical white reflection shine on the left edge, and a rounded U-bottom. The tubes contain horizontal flat vibrant layers of liquid in distinct colors: red, royal blue, bright green, sunshine yellow, and vibrant orange. Clean vector cartoon style, super smooth finish, cute casual mobile game aesthetic, high contrast, glossy highlights, 4k resolution.
```

---

### Prompt 3: Ống nghiệm đang nghiêng rót nước (Tilted Pouring Tube & Stream)

*Dùng để cắt sprite dòng chảy uốn lượn và hiệu ứng mặt nước nghiêng khi rót.*

- **Aspect Ratio**: `1:1`
- **Tên file mục tiêu**: `pouring_stream_concept.png`
- **Prompt**:
```text
2D game asset of a cartoon glass test tube tilted at a 45 degree angle pouring vibrant orange liquid into a vertical test tube, isolated on solid dark navy background. The pouring liquid forms a smooth, thick curved fluid stream arching out of the tilted tube's mouth down into the receiving tube. Small white 4-pointed sparkle stars twinkling near the pour arc. Glossy cartoon vector style, thick smooth dark outlines, bright playful colors, fluid dynamic pouring motion, clean edges, mobile casual game art style.
```

---

### Prompt 4: Hạt sao 4 cánh lấp lánh (Sparkle Star Particle)

*Dùng làm hạt particle trong `CPUParticles2D` cho hiệu ứng rót nước và ăn mừng chiến thắng.*

- **Aspect Ratio**: `1:1`
- **Tên file mục tiêu**: `sparkle.png`
- **Prompt**:
```text
A single 4-pointed diamond sparkle star icon, glittering shine twinkle glint, pure bright white with soft cyan-blue outer glow halo, isolated on solid pure black background (#000000). Perfectly symmetrical, sharp pointed tips, crisp clean vector graphic, mobile game VFX particle asset, high contrast, centered.
```
*(Lưu ý: Ảnh nền đen rất dễ tách kênh alpha hoặc dùng chế độ blend Additive trong Godot).*

---

### Prompt 5: Nắp bần / Nút gỗ đậy ống nghiệm (Wooden Cork Stopper)

*Tùy chọn: dùng để đậy kín miệng ống nghiệm khi người chơi đã hoàn thành ống (đầy 1 màu), tăng cảm giác hoàn tất thỏa mãn.*

- **Aspect Ratio**: `1:1`
- **Tên file mục tiêu**: `cork_stopper.png`
- **Prompt**:
```text
A cute 2D cartoon wooden cork stopper for a test tube bottle, isolated on solid pure white background. Slightly tapered cylindrical shape, warm textured cork wood grain, soft top rim highlight, thick smooth dark cartoon outline, casual mobile puzzle game asset, flat design with 3D bevel shading, clean edges, centered.
```

---

### Prompt 6: Huy hiệu hoàn tất mạ vàng (Golden Checkmark Badge)

*Dùng hiển thị phía trên ống nghiệm khi đã hoàn thành 4 lớp cùng màu.*

- **Aspect Ratio**: `1:1`
- **Tên file mục tiêu**: `gold_check_badge.png`
- **Prompt**:
```text
A glossy 3D golden checkmark badge icon for mobile puzzle game, isolated on solid pure white background. Circular smooth amber-gold medallion with an embossed glowing white checkmark symbol in the center. Thick smooth dark outline, glossy specular reflections, vibrant warm golden yellow tones (#FFB703), cute casual puzzle reward UI icon, clean edges, centered.
```

---

## 4. Quy trình xử lý hậu kỳ (Post-Processing Pipeline)

Sau khi bạn tạo ảnh bằng Google Banana và lưu vào thư mục `playstore/cm-mt-watersort/art-src/`:

1. **Tách nền trong suốt (Alpha Cutout)**:
   - Sử dụng script Python `Pillow` (tự động) để xóa nền trắng hoặc nền đen của ảnh, chuyển thành PNG 32-bit RGBA trong suốt.
2. **Cắt & Đóng gói Spritesheet / 9-patch**:
   - Vỏ ống nghiệm sẽ được căn chỉnh kích thước chuẩn `width = 160px`, `height = 480px` để khớp hoàn hảo với tỉ lệ lưới `TubeView` hiện tại trong Godot.
3. **Cập nhật script `tube_view.gd` & `board_view.gd`**:
   - Gắn texture vỏ ống nghiệm, vành kính và hiệu ứng hạt sao lấp lánh vào game.
   - Thêm chuyển động nghiêng mặt nước (slosh) và tăng bề dày dòng rót uốn lượn.
