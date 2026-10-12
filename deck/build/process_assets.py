"""Turn raw source images into presentation-ready assets (assets/processed)."""
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import numpy as np, pathlib
RAW = pathlib.Path("assets/raw"); OUT = pathlib.Path("assets/processed"); OUT.mkdir(exist_ok=True)

def rounded(im, radius_frac=0.037):
    im = im.convert("RGBA"); w, h = im.size; r = int(w * radius_frac)
    big = Image.new("L", (w * 4, h * 4), 0)
    ImageDraw.Draw(big).rounded_rectangle([0, 0, w * 4 - 1, h * 4 - 1], r * 4, fill=255)
    im.putalpha(big.resize((w, h), Image.LANCZOS)); return im

def crop_frac(im, box):
    w, h = im.size; x0, y0, x1, y1 = box
    return im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))

def save(im, name, q=None):
    p = OUT / name
    (im if name.endswith(".png") else im.convert("RGB")).save(p, **({"quality": q} if q else {}))
    print(name, im.size)

# ---------- Egypt (Wikimedia, field labels in place of personal data) ----------
eg = Image.open(RAW / "web/Egyptian_ID_Card.jpg").convert("RGB")
EGF = eg.crop((59, 72, 2515, 1580)); EGB = eg.crop((60, 1705, 2519, 3211))
save(rounded(EGF), "eg_front.png"); save(rounded(EGB), "eg_back.png")
# macro crops (fractions of each face)
save(crop_frac(EGB, (0.035, 0.035, 0.205, 0.335)), "eg_m_kinegram.png")
save(crop_frac(EGB, (0.835, 0.030, 0.995, 0.370)), "eg_m_eagle.png")
save(crop_frac(EGB, (0.395, 0.000, 0.575, 0.360)), "eg_m_relief_scene.png")
save(crop_frac(EGB, (0.040, 0.590, 0.960, 0.950)), "eg_m_barcode.png")
save(crop_frac(EGF, (0.300, 0.230, 0.990, 0.840)), "eg_m_pyramids.png")
save(crop_frac(EGF, (0.450, 0.020, 0.900, 0.230)), "eg_m_title.png")
save(crop_frac(EGF, (0.010, 0.885, 0.330, 0.990)), "eg_m_guilloche_band.png")
save(crop_frac(EGF, (0.300, 0.300, 0.670, 0.700)), "eg_m_rainbow_bg.png")

# ---------- Egypt lecture photos (real data -> masked) ----------
def mask_boxes(im, boxes, mode="pixel"):
    im = im.convert("RGB")
    for (x0, y0, x1, y1) in boxes:
        reg = im.crop((x0, y0, x1, y1))
        if mode == "pixel":
            sw, sh = max(1, (x1 - x0) // 9), max(1, (y1 - y0) // 6)
            reg = reg.resize((sw, sh), Image.BILINEAR).resize((x1 - x0, y1 - y0), Image.NEAREST)
        else:
            reg = reg.filter(ImageFilter.GaussianBlur(9))
        im.paste(reg, (x0, y0))
    return im
lec = Image.open(RAW / "lectures/sp1/sp1_p19_0_724x444.png").convert("RGB")
save(lec, "_lec19_full.png")

# ---------- Germany (official specimens) ----------
def cut_card(im, thr=246):
    a = np.asarray(im.convert("L")); m = a < thr
    ys = np.where(m.mean(1) > 0.5)[0]; xs = np.where(m.mean(0) > 0.5)[0]
    return im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
def_front = Image.open(RAW / "bmi/pap_details_de_poster.jpg").convert("RGB")
print("de front raw", def_front.size)
save(rounded(def_front.crop((2, 2, def_front.width - 2, def_front.height - 2)), 0.045), "de_front.png")
back = Image.open(RAW / "bmi/flyer/x43_513x324.png").convert("RGB")
back2 = back.resize((back.width * 2, back.height * 2), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2, 60, 2))
save(rounded(back2, 0.045), "de_back.png")
fr_ov = Image.open(RAW / "bmi/flyer/x45_513x324.png").convert("RGB")
save(rounded(fr_ov.resize((1026, 648), Image.LANCZOS), 0.045), "de_front_identigram_overlay.png")
macros = {"x47_125x64": "de_m_guilloche1", "x49_125x64": "de_m_guilloche2", "x51_126x63": "de_m_microprint",
          "x53_125x125": "de_m_ovi_logo", "x55_126x125": "de_m_uv_fibres", "x57_125x126": "de_m_emboss_map",
          "x59_126x63": "de_m_cli_portrait", "x61_126x64": "de_m_thread", "x63_126x64": "de_m_cli_date",
          "x67_125x126": "de_m_uv_eagle", "x71_126x64": "de_m_thread_muster", "x75_125x125": "de_m_eid_logo",
          "x77_125x64": "de_m_tactile_can", "x79_126x65": "de_m_tactile_2034", "x81_124x64": "de_m_inkjet_eye",
          "x83_125x63": "de_m_laser_text", "x85_63x125": "de_m_identigram_d", "x87_64x125": "de_m_identigram_blue",
          "x89_125x64": "de_m_guilloche3", "x69_125x63": "de_m_address_label"}
for k, v in macros.items():
    f = next((RAW / "bmi/flyer").glob(k + "*.png"))
    im = Image.open(f).convert("RGB"); im = im.resize((im.width * 3, im.height * 3), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.5, 50, 2))
    save(im, v + ".png")
# crops from the 1012px front specimen
F = def_front
save(crop_frac(F, (0.030, 0.030, 0.640, 0.180)), "de_m_header.png")
save(crop_frac(F, (0.620, 0.150, 0.990, 0.700)), "de_m_eagle_guilloche.png")
save(crop_frac(F, (0.040, 0.200, 0.420, 0.960)), "de_m_photo.png")
save(crop_frac(F, (0.760, 0.730, 0.960, 0.840)), "de_m_can.png")
save(crop_frac(F, (0.680, 0.030, 0.985, 0.110)), "de_m_docno.png")

# ---------- Egypt lecture card (SP1 p7) — real person: mask identity data ----------
L = Image.open(RAW / "lectures/sp1/sp1_p07_0_436x267.png").convert("RGB")
face = L.crop((12, 8, 128, 152)).filter(ImageFilter.GaussianBlur(10)); L.paste(face, (12, 8))
L = mask_boxes(L, [(250, 72, 432, 168), (170, 198, 426, 236), (12, 236, 140, 262), (16, 188, 92, 222)], "pixel")
L2 = L.resize((L.width * 3, L.height * 3), Image.LANCZOS)
save(rounded(L2, 0.04), "eg_lecture_masked.png")
save(L2.crop((0, 165 * 3, 150 * 3, 236 * 3)), "eg_m_mli_lecture.png")

# ---------- extra crops + sampled colour swatches ----------
save(crop_frac(EGB, (0.010, 0.380, 0.330, 0.570)), "eg_m_back_texture.png")
save(crop_frac(EGB, (0.220, 0.020, 0.800, 0.560)), "eg_m_back_upper.png")
import json
def avg(im, box):
    a = np.asarray(crop_frac(im, box).convert("RGB")).reshape(-1, 3).mean(0)
    return "%02X%02X%02X" % tuple(int(v) for v in a)
sw = {
  "eg": [("Sky", avg(EGF, (0.30, 0.05, 0.40, 0.12))), ("Sand", avg(EGF, (0.50, 0.45, 0.60, 0.55))),
         ("Title green", avg(EGF, (0.62, 0.07, 0.64, 0.09))), ("Guilloche band", avg(EGF, (0.60, 0.90, 0.80, 0.97))),
         ("Back parchment", avg(EGB, (0.25, 0.42, 0.35, 0.52)))],
  "de": [("Card ground", avg(def_front, (0.86, 0.45, 0.93, 0.55))), ("Guilloche ochre", avg(def_front, (0.92, 0.80, 0.98, 0.88))),
         ("Header blue", avg(def_front, (0.22, 0.05, 0.40, 0.08))), ("EU blue", avg(def_front, (0.05, 0.05, 0.08, 0.15))),
         ("Laser black", avg(def_front, (0.45, 0.44, 0.47, 0.46)))]}
(OUT / "swatches.json").write_text(json.dumps(sw, indent=1)); print(sw)
