# Prompt sinh ảnh cho Chấm Công (home.free.chamcong)

Dán vào Google Nano Banana (gemini.google.com hoặc aistudio.google.com).
Sinh 3–4 biến thể mỗi prompt rồi chọn.

**Màu chủ đạo lấy từ code** (`ChamCongApp.seed` trong `lib/main.dart`):
Xanh thợ blue `#1565C0` → blue đậm `#0D47A1`. Giữ nguyên mã hex trong prompt để
icon khớp giao diện app.

Sau khi có ảnh, áp icon bằng lệnh:

```bash
python3 assets-shared/icons/apply_icon.py chamcong <đường-dẫn-ảnh-icon>.png
```

---

## A. APP ICON — bản chính (khuyên dùng)

Ý tưởng: **Lịch làm việc kết hợp mặt đồng hồ đo giờ** — thể hiện rõ nét hai yếu tố cốt lõi: ngày công đi làm và số giờ tăng ca/làm đêm của người lao động.

```
App icon for a shift worker timecard and overtime calculator app. A bold white minimal desk calendar with rounded corners; on the bottom-right corner of the calendar is a clean white circular clock face showing 9 o'clock, symbolizing tracked work hours and night shifts; on the left side of the calendar page are three neatly embossed horizontal attendance check marks. Clean geometric flat vector style with subtle inner shadows and gentle depth. Background: smooth diagonal gradient from vibrant worker blue #1565C0 to deep navy #0D47A1. Centered composition, the symbol fills 68% of the frame, crisp clean edges, instantly readable at 48px, high contrast, dependable and professional Play Store app icon, square 1:1, full-bleed background with no rounded corners, no text, no numbers, no letters, no watermark, no phone mockup.
```

## B. APP ICON — biến thể 3D clay (hiện đại, nổi bật trên Google Play VN)

```
App icon for a shift attendance and overtime salary app, modern 3D clay render style with soft studio lighting and tactile smooth matte finish. A cute rounded clay wall calendar in white and sky blue, with a rounded clay clock perched on its lower corner, casting gentle soft shadows. Material: smooth plasticine / matte ceramic. Background: smooth diagonal gradient from blue #1565C0 to deep blue #0D47A1. Centered composition, fills 65% of the frame, friendly yet trustworthy aesthetic, square 1:1, no text, no watermark, no border.
```

## C. FEATURE GRAPHIC (1024x500)

```
Google Play Store feature graphic banner for a work attendance and overtime pay app named 'Chấm Công'. Dimensions: 1024x500 horizontal landscape. Left side: floating 3D clay calendar with a stylish clock and subtle overtime badge. Right side: bold typography 'Chấm Công' and subtitle 'Tăng ca · Ca đêm · Bảng lương' in clean modern Vietnamese typography. Background: elegant gradient from royal blue #1565C0 to deep midnight blue #0D47A1 with subtle geometric ambient waves and soft glows. High contrast, professional fintech / productivity banner, clean, no cluttered elements, no stock photo watermarks.
```
