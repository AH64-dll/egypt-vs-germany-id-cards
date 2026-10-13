"""Generate current static reading previews from the matching PDF (not an Office render)."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw

output = Path(__file__).resolve().parents[1] / "output"
renders = output / "renders"
renders.mkdir(exist_ok=True)
doc = fitz.open(output / "Egypt-vs-Germany-ID-Cards.pdf")
for page, slide in enumerate(doc, 1):
    pixmap = slide.get_pixmap(matrix=fitz.Matrix(2, 2))
    pixmap.save(renders / f"s{page:02d}.png")
for path in renders.glob("s*.png"):
    if int(path.stem[1:]) > len(doc):
        path.unlink()
for part in range(2):
    sheet = Image.new("RGB", (1600, 3 * 248), "#252525")
    draw = ImageDraw.Draw(sheet)
    for slot in range(12):
        index = part * 12 + slot
        pixmap = doc[index].get_pixmap(matrix=fitz.Matrix(.4, .4))
        image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
        x, y = slot % 4 * 400, slot // 4 * 248
        sheet.paste(image, (x + 8, y + 23))
        draw.text((x + 10, y + 6), f"{index + 1:02d}", fill="white")
    sheet.save(output / f"contact_sheet_{part + 1}.jpg", quality=90)
obsolete = output / "English-contact-sheet.jpg"
if obsolete.exists():
    obsolete.unlink()
print("Rendered 24 PDF reading previews and two contact sheets.")
