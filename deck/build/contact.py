"""Contact sheets of the slide renders: python -P build/contact.py"""
from PIL import Image, ImageDraw
import glob, os
files = sorted(glob.glob('output/renders/s*.png'))
tw, th, cols, pad = 480, 270, 5, 10
for part, (a, b) in enumerate([(0, 20), (20, 37)]):
    fs = files[a:b]; rows = (len(fs) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * (tw + pad) + pad, rows * (th + pad + 18) + pad), (20, 20, 20)); d = ImageDraw.Draw(sheet)
    for i, f in enumerate(fs):
        im = Image.open(f).convert('RGB').resize((tw, th), Image.LANCZOS)
        x = pad + (i % cols) * (tw + pad); y = pad + (i // cols) * (th + pad + 18)
        sheet.paste(im, (x, y)); d.text((x, y + th + 3), os.path.basename(f), fill=(200, 200, 200))
    sheet.save(f'output/contact_sheet_{part + 1}.jpg', quality=88)
print('ok')
