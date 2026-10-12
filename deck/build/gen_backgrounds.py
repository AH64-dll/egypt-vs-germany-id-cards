"""Ember backgrounds: near-black base, soft orange light, fine grain (hides banding)."""
import numpy as np
from PIL import Image
W, H = 3840, 2160
rng = np.random.default_rng(7)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
BASE = np.array([9, 9, 9], np.float32)
EMBER = np.array([255, 90, 31], np.float32); DEEP = np.array([143, 39, 13], np.float32)

def glow(cx, cy, rx, ry, power=1.6):
    d = np.sqrt(((xx - cx * W) / (rx * W)) ** 2 + ((yy - cy * H) / (ry * H)) ** 2)
    return np.clip(1 - d, 0, 1) ** power

def render(name, layers, grain=3.2, vignette=0.35):
    img = np.tile(BASE, (H, W, 1))
    for col, g, a in layers:
        img = img + (col - img) * (g[..., None] * a)
    # vignette
    d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    img *= (1 - vignette * np.clip(d - 0.55, 0, 1) ** 1.2)[..., None]
    img += rng.normal(0, grain, (H, W, 1)).astype(np.float32)
    Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(f"assets/art/{name}.jpg", quality=93, subsampling=0)
    print(name)

render("bg_cover", [(DEEP, glow(0.18, 1.05, 0.75, 1.15, 1.4), 0.95), (EMBER, glow(0.22, 1.08, 0.42, 0.62, 1.8), 0.85),
                    (DEEP, glow(1.0, -0.1, 0.5, 0.7, 2.0), 0.35)])
render("bg_cover_rtl", [(DEEP, glow(0.82, 1.05, 0.75, 1.15, 1.4), 0.95), (EMBER, glow(0.78, 1.08, 0.42, 0.62, 1.8), 0.85),
                        (DEEP, glow(0.0, -0.1, 0.5, 0.7, 2.0), 0.35)])
render("bg_glow_br", [(DEEP, glow(1.02, 1.1, 0.6, 0.9, 1.7), 0.75), (EMBER, glow(1.0, 1.15, 0.3, 0.45, 2.2), 0.45)])
render("bg_glow_bl", [(DEEP, glow(-0.02, 1.1, 0.6, 0.9, 1.7), 0.75), (EMBER, glow(0.0, 1.15, 0.3, 0.45, 2.2), 0.45)])
render("bg_glow_tr", [(DEEP, glow(1.0, -0.12, 0.55, 0.8, 1.8), 0.6)])
render("bg_glow_tl", [(DEEP, glow(0.0, -0.12, 0.55, 0.8, 1.8), 0.6)])
render("bg_center", [(DEEP, glow(0.5, 0.62, 0.55, 0.75, 1.6), 0.55), (EMBER, glow(0.5, 0.66, 0.25, 0.35, 2.2), 0.25)])
render("bg_quiet", [(DEEP, glow(0.5, 1.25, 0.9, 0.7, 2.0), 0.35)], vignette=0.25)
# chapter opener: strong ember wash on one side (like ref-2 orange panels)
render("bg_opener_r", [(DEEP, glow(1.05, 0.5, 0.75, 1.3, 1.1), 1.0), (EMBER, glow(1.1, 0.55, 0.45, 0.9, 1.4), 0.9)])
render("bg_opener_l", [(DEEP, glow(-0.05, 0.5, 0.75, 1.3, 1.1), 1.0), (EMBER, glow(-0.1, 0.55, 0.45, 0.9, 1.4), 0.9)])
