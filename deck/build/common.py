"""Shared slide helpers."""
import json
from lib import *

ANCH = json.loads((ART / "anchors.json").read_text())
TOTAL = 37

def anchor_xy(name, i, side, x, y, w, h):
    fx, fy = ANCH[name][i][side]
    return x + fx * w, y + fy * h

def stat(s, x, y, w, num, label, ar=False, num_size=44, color=None, label_size=None, label_h=0.6):
    text(s, x, y, w, 0.8, num, size=num_size, font=F["disp_lt"], color=color or C["txt"], align="r" if ar else "l", rtl=False)
    text(s, x, y + 0.80, w, label_h, label, size=label_size or (12.5 if ar else 11.5), color=C["txt2"],
         font=F["ar"] if ar else F["body"], align="r" if ar else "l", ls=1.05)

def title_en(s, parts, x=MX, y=0.78, w=8.5, size=40, h=0.8):
    runs = [(t, {"color": C["org"]}) if hi else (t, {}) for t, hi in parts]
    return text(s, x, y, w, h, [runs], size=size, font=F["disp"], caps=True, ls=0.9)

def title_ar(s, t, y=0.78, w=8.5, size=32, x=None, h=0.8, color=None):
    x = SW - MX - w if x is None else x
    return text(s, x, y, w, h, t, size=size, font=F["ar"], bold=True, color=color)

def sub(s, t, x, y, w, h=0.8, size=None, color=None, ar=None):
    a = is_ar(t) if ar is None else ar
    return text(s, x, y, w, h, t, size=size or (15 if a else 14), color=color or C["txt2"],
                font=F["ar_lt"] if a else F["body"], ls=1.2)

def label(s, x, y, w, t, color=None, size=None, align=None):
    a = is_ar(t)
    return text(s, x, y, w, 0.28, t, size=size or (11 if a else 10.5), color=color or C["org"],
                font=F["ar_sb"] if a else F["disp_md"], spc=0 if a else 200, align=align)

def loupe(s, path, cx, cy, d, fx=0.5, fy=0.5, ring=None, n=None, ar=False):
    p = img_cover(s, path, cx - d / 2, cy - d / 2, d, d, fx, fy)
    circle_pic(p); pic_line(p, ring or C["org"], 1.5); pic_effects(p, shadow=(16, 5, 90, "000000", 0.65))
    if n is not None:
        num_badge(s, cx + d * 0.36, cy - d * 0.36, n, d=0.27, size=10)
    return p

def img_zoom(s, path, x, y, w, h, cx, cy, zw):
    """show a zoomed region of an image: centre (cx, cy) as fractions, zw = fraction of source width shown."""
    from PIL import Image
    p = ART / path if (ART / path).exists() else PROC / path
    iw, ih = Image.open(p).size
    rw = zw * iw; rh = rw * h / w
    if rh > ih: rh = ih; rw = rh * w / h
    l = min(max(cx * iw - rw / 2, 0), iw - rw); t = min(max(cy * ih - rh / 2, 0), ih - rh)
    return img(s, p, x, y, w, h, crop=(l / iw, t / ih, 1 - (l + rw) / iw, 1 - (t + rh) / ih))

def zoom_pic(s, path, x, y, w, h, cx, cy, zw, r=0.1, line_c=None, circle=False):
    p = img_zoom(s, path, x, y, w, h, cx, cy, zw)
    if circle: circle_pic(p)
    else: round_pic(p, r)
    pic_line(p, line_c or C["line2"], 0.75 if not circle else 1.5)
    return p

def frame_pic(s, path, x, y, w, h, fx=0.5, fy=0.5, r=0.1, line_c=None):
    p = img_cover(s, path, x, y, w, h, fx, fy); round_pic(p, r)
    pic_line(p, line_c or C["line2"], 0.75)
    return p

def card_img(s, path, x, y, w, ratio, shadow=True):
    p = img(s, path, x, y, w, w / ratio)
    if shadow: pic_effects(p, shadow=(20, 7, 90, "000000", 0.65))
    return p

def leader(s, x1, y1, x2, y2, color=None, w=0.9, dot_start=True):
    line(s, x1, y1, x2, y2, color or C["org"], w, alpha=0.9)
    if dot_start: dot(s, x1, y1, 0.08)

def chip(s, x, y, t, fill=None, color=None, w=None, h=0.27, size=None, line_c=None):
    a = is_ar(t)
    w = w or (len(t) * (0.075 if not a else 0.085) + 0.3)
    rect(s, x, y, w, h, fill=fill, line=line_c if line_c else (None if fill else C["line2"]), lw=0.75, r=h / 2)
    text(s, x, y, w, h, t, size=size or (9.5 if not a else 10), color=color or C["txt2"],
         font=F["ar_md"] if a else F["disp_md"], align="c", anchor="ctr", spc=0 if a else 120)
    return w

def opener_numeral(s, n, side="l", color=None, alpha=None):
    x = 0.35 if side == "l" else SW - 4.95
    return text(s, x, 0.45, 4.6, 3.95, f"{n:02d}", size=230, font=F["disp_lt"], color=color or C["txt"], rtl=False,
                align="l" if side == "l" else "r")

def bullet_rows(s, x, y, w, items, gap=0.08, size=None, ar=False, num=True, title_size=None, row_h=None, color=None):
    """items: list of (title, body). Stacked editorial rows with hairlines."""
    yy = y
    for i, (t, b) in enumerate(items):
        h = row_h or 0.7
        line(s, x, yy, x + w, yy, C["line"], 0.5)
        if num:
            if ar:
                text(s, x + w - 0.45, yy + 0.08, 0.45, 0.3, f"{i+1:02d}", size=12, font=F["disp_md"], color=C["org"], align="r", rtl=False)
            else:
                text(s, x, yy + 0.08, 0.45, 0.3, f"{i+1:02d}", size=12, font=F["disp_md"], color=C["org"])
        tx, tw = (x, w - 0.55) if ar else (x + 0.55, w - 0.55)
        if not num: tx, tw = x, w
        text(s, tx, yy + 0.06, tw, h - 0.06, [[(t + ("  " if b else ""), {"font": F["ar_sb"] if ar else F["body_sb"], "color": C["txt"]}),
                                               (b, {"color": color or C["txt2"]})]], size=size or (13 if ar else 12.5), ls=1.12)
        yy += h + gap
    line(s, x, yy, x + w, yy, C["line"], 0.5)
    return yy
