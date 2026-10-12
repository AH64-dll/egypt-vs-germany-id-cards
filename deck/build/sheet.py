import sys, glob, os
from PIL import Image, ImageDraw
pattern, out = sys.argv[1], sys.argv[2]; tw = int(sys.argv[3]) if len(sys.argv) > 3 else 470
fs = sorted(glob.glob(pattern)); W = 1500
sheet = Image.new('RGB', (W, 6000), (25, 25, 25)); d = ImageDraw.Draw(sheet); x = y = 10; rh = 0
for f in fs:
    im = Image.open(f)
    if im.mode == 'RGBA':
        bg = Image.new('RGBA', im.size, (12, 12, 12, 255)); bg.alpha_composite(im); im = bg
    im = im.convert('RGB'); im.thumbnail((tw, int(tw * 0.65)))
    if x + im.width > W: x = 10; y += rh + 28; rh = 0
    sheet.paste(im, (x, y)); d.text((x, y + im.height + 3), os.path.basename(f), fill=(255, 150, 90))
    x += im.width + 14; rh = max(rh, im.height)
sheet.crop((0, 0, W, y + rh + 30)).save(out, quality=85)
