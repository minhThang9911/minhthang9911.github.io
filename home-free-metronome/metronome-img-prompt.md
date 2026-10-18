# Image Generation Prompts for Metronome (home.free.metronome)

Dán vào Google Nano Banana (gemini.google.com hoặc aistudio.google.com).
Sinh 3–4 biến thể mỗi prompt rồi chọn.

**Màu chủ đạo lấy từ code** (`MetronomeApp.seed` trong `lib/main.dart`):
Teal `#00838F` → deep teal `#005662`. Giữ nguyên mã hex trong prompt để icon khớp hoàn toàn giao diện app.

Sau khi có ảnh, áp icon bằng một lệnh:

```bash
python3 assets-shared/icons/apply_icon.py metronome <đường-dẫn-ảnh-icon>.png
```

---

## A. APP ICON — bản chính (khuyên dùng)

Ý tưởng: **Con lắc nhịp metronome hình tháp cơ học cổ điển kết hợp phong cách vector phẳng hiện đại** — biểu tượng vượt thời gian của nhịp độ âm nhạc chính xác.

```
App icon for a precise musical metronome app. A bold white minimalist silhouette of a classic pyramid mechanical metronome body with an angled swinging pendulum rod and a metallic sliding weight bob near the top; subtle rhythmic pulse arcs emanate faintly from the swinging tip. Minimal flat vector style with subtle depth, soft inner shadows, and clean geometric lines. Background: smooth diagonal gradient from vivid teal #00838F to deep teal #005662. Centered composition, the metronome symbol fills 68% of the frame, crisp clean edges, high contrast, musical elegance and precision timing mood, professional Google Play Store app icon, square 1:1, full-bleed background with no rounded corners, no text, no numbers, no letters, no watermark, no musical notes lettering, no phone mockup.
```

## B. APP ICON — biến thể: chấm phách nhịp & con lắc tương tác

Bám sát trực quan cốt lõi của app: hàng chấm phách tương tác và con lắc chuyển động.

```
App icon for a rhythm and tempo metronome app. A stylized white metronome pendulum rod angled dynamically across the center with an adjustable sliding weight, framed at the base by an arc of four distinct glowing circular beat indicator dots with the first beat accented and brightly illuminated. Minimal flat vector illustration, clean modern aesthetic, sharp silhouette with soft ambient rim glow. Background: smooth diagonal gradient from rich teal #00838F to dark cyan #005662. Centered composition, symbol fills 65% of the frame, instantly recognizable at tiny launcher sizes, professional Play Store app icon, square 1:1, full-bleed background, no rounded corners, no text, no letters, no numbers, no watermark.
```

## C. APP ICON — biến thể 3D clay (hiện đại, mềm mại)

```
App icon for a musician metronome app, premium 3D clay render style with soft studio lighting and tactile smooth plasticine material. A matte white miniature mechanical metronome with a silver sliding weight on its swinging pendulum arm, cast with gentle soft shadows, highlighted with a delicate teal rim light. Background: rich diagonal gradient from teal #00838F to deep teal #005662. Centered composition, the object fills 66% of the frame, realistic soft shadows, tactile, clean and friendly music utility aesthetic, professional Play Store app icon, square 1:1, full-bleed background, no rounded corners, no text, no letters, no watermark.
```

---

## D. FEATURE GRAPHIC 1024×500 — bản chính

```
Wide 1024x500 mobile app store feature banner, landscape 2:1 ratio. On the left third, a clean white mechanical metronome silhouette with an angled pendulum arm and subtle rhythmic motion blur arcs radiating outwards; across the center bottom, a minimalist horizontal sequence of glowing circular rhythm beat dots with subtle audio waveform ripples fading softly to the right. Background: smooth horizontal gradient from bright teal #00838F on the left to deep ocean teal #005662 on the right, with a very faint musical measure grid pattern fading into the dark background. The right third is clean empty gradient space reserved for typography. Modern premium flat vector illustration with soft glow and subtle depth, sophisticated musical mood. Key visual elements contained within the central 80% safe zone. Absolutely no text, no numbers, no letters, no watermark, no phone mockup, no store badges.
```

## E. FEATURE GRAPHIC — biến thể tối giản (tuyệt đối an toàn mép crop)

```
Wide 1024x500 mobile app store feature banner, landscape 2:1 ratio. A bold minimalist white metronome pendulum silhouette floating on the left third with a soft glow, with thin glowing horizontal speed lines and rhythmic pulse circles trailing gracefully toward the center. Background: smooth horizontal gradient from teal #00838F to deep teal #005662. The right half is completely clean empty gradient space for title placement. Crisp vector lines, soft glows, refined aesthetic. All graphical elements within the central 80% safe zone. No text, no letters, no numbers, no watermark, no phone mockup.
```

---

## Lưu ý khi dùng

- **Tuyệt đối không để AI chèn chữ "Metronome" vào ảnh** — AI hay sinh chữ méo hoặc lỗi font. Sinh ảnh hoàn toàn không chữ (`no text, no letters`), sau đó thêm chữ bằng Figma/Canva nếu cần.
- **Icon**: xuất kích thước 512×512 PNG, **không bo góc** (Google Play tự áp dụng mặt nạ squircle). Chạy script `apply_icon.py` để tự động bo góc và cắt cho các thư mục launcher mipmap.
- **Feature graphic**: đúng **1024×500**, PNG 24-bit hoặc JPG, **không có kênh alpha** (RGB).
- Đặt file icon đã duyệt vào thư mục này với tên `icon.png` và `play-feature-image.png` để hệ thống tự động nhận diện và nhúng vào trang chính sách quyền riêng tư.
