# Prompt sinh ảnh cho Thước Lỗ Ban (home.free.thuocluban)

Dán vào Google Nano Banana (gemini.google.com hoặc aistudio.google.com).
Sinh 3–4 biến thể mỗi prompt rồi chọn.

**Màu chủ đạo lấy từ code** (`ThuocLuBanApp.seed` trong `lib/main.dart`):
xanh xám thép `#546E7A` → `#30424C`. Giữ nguyên mã hex trong prompt để icon
khớp giao diện app.

Sau khi có ảnh, áp icon bằng một lệnh:

```bash
python3 assets-shared/icons/apply_icon.py thuocluban <đường-dẫn-ảnh-icon>.png
```

Icon hiện tại là **glyph tạm** sinh bằng `gen_icons.py thuocluban` (bốn ô cung
đặc–rỗng + mũi tên). Dùng được, nhưng ảnh thật sẽ nổi hơn trên Play.

---

## A. APP ICON — bản chính (khuyên dùng)

Ý tưởng: **dải thước chia cung, có ô tốt ô xấu, và một mũi tên chỉ vào ô tốt**
— đúng việc app làm: không chỉ nói số bạn định lấy là xấu, mà chỉ luôn chỗ đẹp.

```
App icon for a Vietnamese Lo Ban feng shui ruler app. A short horizontal
ruler segment seen head-on, divided into four equal cells with small tick
marks along its top edge; two cells are filled solid white and two are hollow
outlines, giving a clear alternating rhythm; a bold white arrow below points
up into one of the filled cells. Minimal flat vector style with subtle depth
and soft inner shadows, no text, no numbers. Background: smooth diagonal
gradient from steel blue-grey #546E7A to deep slate #30424C. Centered
composition, the symbol fills 70% of the frame, crisp clean edges, high
contrast, square 1:1, no rounded corner mask.
```

## B. APP ICON — biến thể 2 (thước cuộn)

```
App icon for a carpenter's measuring app. A white retractable tape measure
blade curving gently across the frame, its edge marked with graduation ticks,
and four larger segment blocks printed on the blade — two solid, two hollow.
Flat vector, minimal, no text. Background: diagonal gradient steel blue-grey
#546E7A to #30424C. Square 1:1, symbol fills 70%, no corner mask.
```

## C. APP ICON — biến thể 3 (khung cửa)

```
App icon for a house-building measurement app. A simple white doorway outline
seen straight on, with a horizontal dimension arrow spanning its clear inner
width and small tick marks along the arrow. Flat minimal vector, no text.
Background: diagonal gradient #546E7A to #30424C. Square 1:1, centered,
symbol fills 68%, no corner mask.
```

---

## D. FEATURE GRAPHIC 1024×500

```
Google Play feature graphic, 1024x500, for a Vietnamese Lo Ban ruler app.
Left third: a large white ruler-segment symbol with alternating solid and
hollow cells and an arrow pointing into a solid cell. Right two thirds: empty
space reserved for text, kept visually calm. Background: horizontal gradient
from steel blue-grey #546E7A to deep slate #30424C, with a faint pattern of
thin vertical measurement ticks. Flat vector, no text in the image itself,
wide banner composition.
```

Feature graphic tạm đang dùng sinh bằng:

```bash
python3 assets-shared/icons/gen_feature.py thuocluban
```
