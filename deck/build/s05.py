"""Slides 27–32: Germany's feature set, four tests, digital layer, roadmap (ch06); finishing (ch07); design (ch08 opener)."""
import json
from common import *
from pptx.enum.shapes import MSO_SHAPE

EGR = 2456 / 1508
DEF = 1008 / 635
DEB = 1026 / 648
SWATCH = json.loads((PROC / "swatches.json").read_text())

def badge_at(s, x, y, w, h, fx, fy, n, d=0.27, size=10, fill=None, txt_c=None):
    o = num_badge(s, x + fx * w, y + fy * h, n, d=d, size=size, fill=fill, txt_c=txt_c)
    effects(o, shadow=(8, 2, 90, "000000", 0.6))
    return o

def arrow(s, x, y, w=0.26, h=0.22, color=None, left=False):
    return shape(s, MSO_SHAPE.LEFT_ARROW if left else MSO_SHAPE.RIGHT_ARROW, x, y, w, h, fill=color or C["org"])

# ------------------------------------------------------------------ 27 AR Germany: 13 features × official check methods
BMI_FEATURES = [  # (name, methods: visual, magnifier, touch, tilt, above, oblique, uv, app)
    ("التشخيص: حبر نفاث + ليزر", [1, 1, 0, 0, 1, 0, 0, 0]),
    ("أرقام ملموسة: الانتهاء وCAN", [1, 0, 1, 0, 0, 1, 0, 0]),
    ("Identigram®", [1, 1, 0, 1, 1, 0, 0, 0]),
    ("علامات UV بطباعة قزحية", [1, 0, 0, 0, 0, 0, 1, 0]),
    ("حبر متغير بصريًا OVI", [1, 0, 0, 1, 1, 1, 0, 0]),
    ("طباعة أمنية وجلوشيات", [1, 1, 0, 0, 1, 0, 0, 0]),
    ("كتابة ميكرونية ±", [1, 1, 0, 0, 1, 0, 0, 0]),
    ("بروز سطحي وخريطة ألمانيا", [1, 1, 1, 0, 1, 1, 0, 0]),
    ("صورة الليزر المتغيرة", [1, 0, 1, 1, 1, 0, 0, 0]),
    ("ألياف أمان تتألق بـ UV", [1, 0, 0, 0, 0, 0, 1, 0]),
    ("خيط أمان مُشخَّص", [1, 1, 0, 1, 1, 0, 0, 0]),
    ("ملصق تغيير العنوان", [1, 0, 0, 0, 1, 0, 0, 1]),
    ("شعار eID", [1, 0, 0, 0, 1, 0, 0, 1]),
]
METHODS_AR = ["نظر", "عدسة", "لمس", "إمالة", "ضوء علوي", "ضوء مائل", "UV", "تطبيق"]

def s27(D):
    s = D.new(); bg(s, "bg_glow_bl.jpg")
    CW = 4.25; FX, FY = MX, 0.95; FH = CW / DEF; BX, BY = MX, FY + FH + 0.18; BH = CW / DEB
    card_img(s, "de_front.png", FX, FY, CW, DEF)
    card_img(s, "de_back.png", BX, BY, CW, DEB)
    for fx, fy, n in [(0.20, 0.88, 1), (0.86, 0.69, 2), (0.42, 0.30, 3), (0.25, 0.14, 4), (0.535, 0.125, 5), (0.93, 0.62, 6), (0.95, 0.24, 7)]:
        badge_at(s, FX, FY, CW, FH, fx, fy, n)
    for fx, fy, n in [(0.21, 0.18, 8), (0.34, 0.31, 9), (0.47, 0.63, 10), (0.57, 0.63, 11), (0.87, 0.12, 12), (0.94, 0.33, 13)]:
        badge_at(s, BX, BY, CW, BH, fx, fy, n, fill=C["txt"])
    text(s, MX, BY + BH + 0.05, CW, 0.22, "مواضع العلامات وفق دليل BMI (مايو 2024) — نموذج رسمي", size=8.5, color=C["mute"], font=F["ar"], align="l")
    X = 5.25; W = SW - MX - X
    title_ar(s, "ألمانيا: 13 علامة تأمين رسمية", w=W, size=32)
    sub(s, "ترقيم دليل وزارة الداخلية الاتحادية وطرق الفحص التي يحددها لكل علامة.", X, 1.45, W, 0.4, size=13)
    NW = 2.75; MW = (W - NW) / 8; y0 = 2.0; hh = 0.48; rh = 0.3
    nx = SW - MX - NW
    for j, m in enumerate(METHODS_AR):
        cx = nx - (j + 1) * MW
        text(s, cx, y0, MW, hh, m, size=9.5, font=F["ar_md"], color=C["txt"] if j else C["txt2"], align="c", anchor="b", ls=0.95)
    text(s, nx, y0, NW, hh, [[("■ ", {"color": C["org"], "rtl": False}), ("الوجه   ", {}), ("■ ", {"color": C["txt"], "rtl": False}), ("الظهر", {})]],
         size=9.5, color=C["txt2"], font=F["ar"], anchor="b")
    line(s, X, y0 + hh + 0.05, SW - MX, y0 + hh + 0.05, C["line2"], 0.75)
    yy = y0 + hh + 0.1
    for i, (nm, ms) in enumerate(BMI_FEATURES):
        if i % 2 == 0:
            rect(s, X, yy, W, rh, fill=C["s1"], alpha=0.65, r=0.04)
        if i == 7:
            line(s, X, yy - 0.01, SW - MX, yy - 0.01, C["line2"], 0.75, dash="dash")
        num_badge(s, SW - MX - 0.16, yy + rh / 2, i + 1, d=0.23, size=9, fill=C["org"] if i < 7 else C["txt"])
        text(s, nx, yy, NW - 0.36, rh, nm, size=10.5, font=F["ar"], color=C["txt"], anchor="ctr", align="r")
        for j, on in enumerate(ms):
            cx = nx - (j + 0.5) * MW
            if on: oval(s, cx - 0.075, yy + rh / 2 - 0.075, 0.15, 0.15, fill=C["org"] if i < 7 else C["txt"])
            else: oval(s, cx - 0.025, yy + rh / 2 - 0.025, 0.05, 0.05, fill=C["line2"])
        yy += rh
    line(s, X, yy + 0.04, SW - MX, yy + 0.04, C["line2"], 0.75)
    totals = [sum(f[1][j] for f in BMI_FEATURES) for j in range(8)]
    text(s, nx, yy + 0.08, NW - 0.36, 0.32, "عدد العلامات", size=10.5, font=F["ar_sb"], color=C["org"], anchor="ctr")
    for j, tv in enumerate(totals):
        text(s, nx - (j + 1) * MW, yy + 0.08, MW, 0.32, str(tv), size=14, font=F["disp_md"], color=C["org"], align="c", anchor="ctr", rtl=False)
    chrome(s, "ar", 6, 27, TOTAL, "BMI 2024 · features #1–13 & verification icons")
    notes(s,
        "يرقّم دليل وزارة الداخلية الاتحادية (مايو 2024) ثلاث عشرة علامة: على الوجه — (1) التشخيص: الصورة الملونة ورقم الوثيقة بالحبر النفاث داخل الخامة وبقية البيانات بالحفر الليزري؛ (2) علامات ملموسة: تاريخ الانتهاء ورقم CAN محفوران بالليزر؛ (3) Identigram: بنى حركية وصورة هولوجرافية خضراء ونسر أحمر ثلاثي الأبعاد وعناصر زرقاء بعد التدوير 90°؛ (4) علامات UV: النسر الاتحادي وكتابة متعددة الألوان بطباعة قزحية؛ (5) حبر متغير بصريًا: شعار «chip inside» يتغير بين الأخضر والأزرق؛ (6) طباعة أمنية: أنماط معقدة وجلوشيات متعددة الألوان وبنى ضد النسخ؛ (7) كتابة ميكرونية موجبة وسالبة بأحجام مختلفة. وعلى الظهر — (8) بروز سطحي ملموس فيه كتابة ميكرونية وخريطة ألمانيا؛ (9) صورة ليزر متغيرة: تاريخ الانتهاء أو صورة الحامل حسب الزاوية؛ (10) ألياف أمان شفافة تتألق تحت UV؛ (11) خيط أمان قابل للفحص آليًا مُشخَّص برقم الوثيقة والاسم؛ (12) ملصق تغيير العنوان، وقد يحمل باركود ثنائي الأبعاد يُفحص بتطبيق؛ (13) شعار eID. المصفوفة تنقل رموز الفحص الرسمية في الدليل لكل علامة: النظر لكل العلامات، والضوء العلوي لعشر، والعدسة لست، والإمالة لأربع، واللمس والضوء المائل لثلاث لكل منهما، وUV والتطبيق لعلامتين لكل منهما.",
        "The Federal Ministry of the Interior's guide (May 2024) numbers thirteen features. Front: (1) personalisation — colour photo and document number integrated by inkjet into the card material, all other data laser-engraved; (2) tactile expiry date and CAN; (3) Identigram — kinematic structures, green holographic portrait, red 3D eagle, blue elements after a 90° turn; (4) UV features — federal eagle and multicolour luminescent lettering in rainbow printing; (5) optically variable ink — the ICAO 'chip inside' logo shifts green↔blue; (6) security printing — complex patterns, multicoloured guilloches, anti-copy structures; (7) positive and negative microprint in varying sizes. Back: (8) tactile surface embossing with microprint and a map of Germany; (9) variable laser image — expiry date or portrait by angle; (10) transparent security fibres, luminescent under UV; (11) machine-verifiable security thread personalised with document number and name; (12) change-of-address label, optionally with a 2D barcode checked by a smartphone app; (13) eID logo. The matrix reproduces the guide's verification icons for each feature: visual for all 13, light from above for 10, magnifier for 6, tilting for 4, touch and oblique light for 3 each, UV and app for 2 each.",
        "BMI flyer 'Security features of the German identity card', May 2024 (features #1–#13 and verification icons: visual, magnifying glass, touch, tilting, light from above, oblique light, UV illumination, app). Card images: Personalausweisportal (front), BMI flyer (back).")
    return s

# ------------------------------------------------------------------ 28 EN four tests side by side
def s28(D):
    s = D.new(); bg(s, "bg_quiet.jpg")
    title_en(s, [("FOUR TESTS, ", False), ("TWO CARDS", True)], y=0.78, w=11, size=40)
    sub(s, "The same everyday checks reveal different features on each card.", MX, 1.42, 10, 0.4, size=13.5)
    tests = [
        ("TILT", "change the viewing angle",
         ("pic", "eg_m_kinegram.png", 0.5, 0.42), "Kinegram® (Tutankhamun) · Multi Laser Image · multi-angle relief",
         ("pic", "de_m_ovi_logo.png", 0.5, 0.5), "OVI logo (green ↔ blue) · Identigram® · variable laser image · thread"),
        ("UV LIGHT", "ultraviolet lamp",
         ("pic", "eg_m_eagle.png", 0.5, 0.3), "Eagle glows under UV · invisible microtext (daylight image)",
         ("pic", "de_m_uv_eagle.png", 0.5, 0.45), "Eagle & multicolour lettering · security fibres"),
        ("MAGNIFIER", "simple loupe",
         ("zoom", "eg_front.png", 0.62, 0.935, 0.22), "Microprint at 5× · guilloche lines continuous, not dots",
         ("pic", "de_m_microprint.png", 0.5, 0.5), "± microprint · guilloches · inkjet photo · embossing"),
        ("TOUCH", "run a finger over it",
         ("pic", "eg_m_mli_lecture.png", 0.7, 0.5), "Multi Laser Image, felt with the fingers (lecture photo, masked)",
         ("pic", "de_m_tactile_2034.png", 0.5, 0.5), "Tactile expiry & CAN · surface embossing · laser image"),
    ]
    gap = 0.2; cw = (SW - 2 * MX - 3 * gap) / 4; y0 = 1.95; ih = 1.2
    for i, (nm, how, eim, ecap, dim, dcap) in enumerate(tests):
        x = MX + i * (cw + gap)
        text(s, x, y0, cw, 0.45, nm, size=24, font=F["disp"], spc=60)
        text(s, x, y0 + 0.45, cw, 0.25, how.upper(), size=9.5, font=F["disp_md"], color=C["txt2"], spc=120)
        line(s, x, y0 + 0.74, x + cw, y0 + 0.74, C["org"], 1.25)
        for k, (im, cap, tag, col) in enumerate([(eim, ecap, "EG", C["org"]), (dim, dcap, "DE", C["txt"])]):
            yy = y0 + 0.88 + k * (ih + 0.66)
            if im[0] == "zoom":
                zoom_pic(s, im[1], x, yy, cw, ih, im[2], im[3], im[4], r=0.08, line_c=col)
            else:
                p = frame_pic(s, im[1], x, yy, cw, ih, im[2], im[3], r=0.08, line_c=col)
            rect(s, x + 0.1, yy + 0.1, 0.42, 0.24, fill=col, r=0.04)
            text(s, x + 0.1, yy + 0.1, 0.42, 0.24, tag, size=10, font=F["disp"], color=C["ink"], align="c", anchor="ctr")
            text(s, x, yy + ih + 0.05, cw, 0.55, cap, size=10, color=C["txt2"], ls=1.05)
    text(s, MX, 6.72, SW - 2 * MX, 0.22, "Germany's guide names eight check methods: visual, magnifier, touch, tilting, light from above, oblique light, UV and app (BMI 2024).",
         size=9, color=C["mute"])
    chrome(s, "en", 6, 28, TOTAL, "SP1 · pp.12–18 · BMI 2024")
    notes(s,
        "Four everyday tests applied to both cards. Tilt: on the Egyptian card the Kinegram shows Tutankhamun's head in different dimensions as the vertical and horizontal angle changes, the Multi Laser Image swaps the date of birth and the emblem, and the relief printing is designed for multiple viewing angles; on the German card the Identigram (kinematic structures, green holographic portrait, red 3D eagle), the OVI 'chip inside' logo (green↔blue), the variable laser image and the security thread are checked by tilting. UV light: Egypt — UV-glowing ink such as the eagle on the back, and invisible microtext visible only under UV; Germany — the federal eagle and multicolour luminescent lettering in rainbow printing, and transparent fibres that luminesce. Magnifier: Egypt — visible microprint read at 5×, guilloche lines that stay continuous instead of breaking into dots; Germany — positive/negative microprint, guilloches, the inkjet photo and the embossing. Touch: Egypt — the Multi Laser Image can be felt with the fingers; Germany — tactile expiry date and CAN, surface embossing and the variable laser image. Egyptian images show the feature locations on a specimen in daylight; the German UV image is the BMI's own UV photograph.",
        "أربعة اختبارات يومية على البطاقتين. الإمالة: في البطاقة المصرية يُظهر الكينجرام رأس توت عنخ آمون بأبعاده المختلفة، وتتبادل الصورة الليزرية المتعددة تاريخ الميلاد والشعار، وتُصمَّم طباعة Relief للقراءة من زوايا متعددة؛ وفي الألمانية تُفحص بالإمالة Identigram وشعار OVI والصورة الليزرية المتغيرة وخيط الأمان. الأشعة فوق البنفسجية: مصر — أحبار متألقة كالنسر على الظهر وكتابة ميكرونية خفية؛ ألمانيا — النسر الاتحادي وكتابة متعددة الألوان بطباعة قزحية وألياف شفافة متألقة. العدسة المكبرة: مصر — كتابة ميكرونية تُقرأ بتكبير 5X وخطوط جلوشيات متصلة لا نقاط؛ ألمانيا — كتابة ميكرونية موجبة وسالبة وجلوشيات والصورة بالحبر النفاث والبروز. اللمس: مصر — الصورة الليزرية المتعددة بارزة تُحَس بالأصابع؛ ألمانيا — تاريخ الانتهاء وCAN البارزان والبروز السطحي وصورة الليزر. الصور المصرية تبين المواضع في ضوء النهار، أما صورة UV الألمانية فهي من دليل الوزارة نفسه.",
        "SP1 pp.12–13, 15, 18 (Egyptian features); BMI flyer May 2024 (#2–#11, verification icons). Images: WM-EG specimen; lecture photo (masked); BMI macro images.")
    return s

# ------------------------------------------------------------------ 29 AR digital layer
def s29(D):
    s = D.new(); bg(s, "bg_center.jpg")
    title_ar(s, "الطبقة الرقمية: باركود مطبوع أم شريحة؟", w=10, size=32)
    sub(s, "مصر تحمل البيانات مشفرة في باركود مطبوع؛ ألمانيا تضيف شريحة لاتلامسية وهوية إلكترونية.", SW - MX - 10, 1.45, 10, 0.4, size=13)
    half = (SW - 2 * MX - 0.35) / 2
    panels = [  # (x, title, color, image, steps)
        (SW - MX - half, "مصر · باركود ثنائي الأبعاد PDF417", C["org"], "eg_m_barcode.png",
         ["البطاقة", "قراءة الباركود", "فك التشفير", "مقارنة ونقل"]),
        (MX, "ألمانيا · شريحة لاتلامسية + eID", C["txt"], "de_m_eid_logo.png",
         ["البطاقة", "قارئ أو هاتف", "رقم PIN", "هوية رقمية"]),
    ]
    for k, (x, t, col, im, steps) in enumerate(panels):
        y = 2.05
        rect(s, x, y, half, 2.05, fill=C["s1"], alpha=0.9, line=col, lw=0.75, lalpha=0.7, r=0.1)
        text(s, x + 0.2, y + 0.12, half - 0.4, 0.35, t, size=14, font=F["ar_sb"], color=col)
        if k == 0:
            frame_pic(s, im, x + 0.2, y + 0.55, 1.6, 0.72, r=0.05)
        else:
            frame_pic(s, im, x + 0.2 + 0.44, y + 0.55, 0.72, 0.72, r=0.05)
        # RTL flow of steps (right → left), boxes to the right of the image
        fx0 = x + 2.0; fw = half - 2.2; sw = (fw - 3 * 0.28) / 4
        for j, st in enumerate(steps):
            bx = x + half - 0.2 - (j + 1) * sw - j * 0.28
            rect(s, bx, y + 0.62, sw, 0.6, fill=C["s2"] if j < 3 else (C["org"] if k == 0 else C["txt"]), line=C["line2"] if j < 3 else None, lw=0.5, r=0.06)
            text(s, bx, y + 0.62, sw, 0.6, st, size=9.5, font=F["ar_md"], color=C["txt"] if j < 3 else C["ink"], align="c", anchor="ctr")
            if j < 3: arrow(s, bx - 0.24, y + 0.81, 0.2, 0.22, col, left=True)
        cap = ("يحمل الباركود بيانات المواطن مشفرة؛ بفك الشفرة تُقارن بالبيانات المقروءة بالعين وتُنقل إلكترونيًا لقواعد بيانات الجهات المستفيدة." if k == 0
               else "تحفظ الشريحة الصورة والبيانات وبصمتي إصبعين؛ وللاستخدام عبر الإنترنت يلزم البطاقة ورقم PIN مع تحقق متبادل بشهادة رسمية.")
        text(s, x + 0.2, y + 1.38, half - 0.4, 0.62, cap, size=10.5, font=F["ar"], color=C["txt2"], ls=1.15)
    rows = [["", "مصر", "ألمانيا"],
            ["وسيط البيانات", "باركود مطبوع على الظهر (PDF417 — مصدر ثانوي)", "شريحة لاتلامسية مدمجة (منذ 1 نوفمبر 2010)"],
            ["المحتوى", "بيانات المواطن الموجودة على البطاقة، مشفرة", "الصورة والبيانات المطبوعة + بصمتا إصبعين"],
            ["الهوية الإلكترونية", "غير موثقة في المحاضرة", "وظيفة eID مع PIN للخدمات الحكومية والتجارية"],
            ["القياسات الحيوية", "ضمن رؤية مستقبلية في المحاضرة", "بصمتان إلزاميتان منذ 2 أغسطس 2021، تُحذفان بعد التسليم"],
            ["القراءة", "فك الشفرة ومقارنة البيانات", "قارئ لاتلامسي أو هاتف وتطبيق؛ والملصق عبر تطبيق"]]
    table(s, MX, 4.3, SW - 2 * MX, [2.0, 5.065, 5.065], rows, rtl=True, row_h=0.4, size=11, header_size=11,
          fills=lambda r, c: C["s1"] if r == 0 else None)
    chrome(s, "ar", 6, 29, TOTAL, "SP1 · pp.15, 21 · WIKI-EG · BMI 2024 · PAP")
    notes(s,
        "الطبقة الرقمية في مصر — بحسب المحاضرة — باركود ثنائي الأبعاد على ظهر البطاقة يحمل بيانات المواطن الموجودة بجسم البطاقة بصورة مشفرة، يمكن بفك شفرته مقارنتها بالبيانات المقروءة بالعين المجردة ونقلها إلكترونيًا لقواعد بيانات الجهات المستفيدة؛ ونوعه PDF417 بحسب مصدر ثانوي. أما استخدام البطاقة الذكية اللاتلامسية والقياسات الحيوية (البصمات والقزحية والوجه) فهي ضمن الرؤية المستقبلية في المحاضرة. في ألمانيا: شريحة لاتلامسية منذ 1 نوفمبر 2010 تحفظ الصورة والبيانات المطبوعة، وبصمتي إصبعين إلزاميًا منذ 2 أغسطس 2021 تُحذفان من سجلات المصنّع والجهة بعد التسليم؛ ووظيفة الهوية الإلكترونية eID للخدمات الرقمية الحكومية والتجارية تتطلب البطاقة ورقم PIN، مع تحقق متبادل بشهادة رسمية للجهة الطالبة. ويمكن لملصق تغيير العنوان أن يحمل باركود يُفحص بتطبيق على الهاتف.",
        "Egypt's digital layer, per the lecture: a 2D barcode on the back holding the citizen's data from the card body in encrypted form; decoding it lets officials compare it with the eye-readable data and transfer it electronically to beneficiary agencies' databases; its symbology is PDF417 according to a secondary source. Contactless smart-card technology and biometrics (fingerprints, iris, face) appear only in the lecture's future vision. Germany: a contactless chip since 1 November 2010 storing the photo and printed data, plus two fingerprints mandatory since 2 August 2021, deleted from the manufacturer's and authority's records after handover; the eID function for digital government and business services needs the card plus a PIN, with mutual authentication using a state-issued certificate for the requesting service. The change-of-address label can carry a 2D barcode checked with a smartphone app.",
        "SP1 p.15 (2D barcode), p.21 (future vision: contactless, biometrics); WIKI-EG (PDF417 — secondary); BMI flyer May 2024 (chip, fingerprints, deletion, eID, address label); PAP (introduction 1 Nov 2010, fingerprints from 2 Aug 2021, eID + PIN, certificates).")
    return s

# ------------------------------------------------------------------ 30 EN Egypt roadmap vs Germany today
def s30(D):
    s = D.new(); bg(s, "bg_glow_tr.jpg")
    title_en(s, [("EGYPT'S ROADMAP, ", False), ("GERMANY'S PRESENT", True)], y=0.78, w=12, size=40)
    sub(s, "The lecture's future vision for the Egyptian card, checked item by item against the current German card.", MX, 1.42, 11, 0.4, size=13.5)
    LX, LW = MX, 4.75; MX2, MW2 = MX + LW + 0.2, 2.0; RX = MX2 + MW2 + 0.2; RW = SW - MX - RX
    y0 = 2.0
    text(s, LX, y0, LW, 0.25, "EGYPT · LECTURE ROADMAP", size=10, font=F["disp_md"], color=C["org"], spc=150)
    text(s, MX2, y0, MW2, 0.25, "STATUS IN GERMANY", size=10, font=F["disp_md"], color=C["txt2"], spc=150, align="c")
    text(s, RX, y0, RW, 0.25, "GERMANY · TODAY (2024 DESIGN)", size=10, font=F["disp_md"], color=C["txt"], spc=150)
    rows = [
        ("UV rainbow effect — iridescent overlapping fluorescent inks", "IN USE", "Federal eagle and multicolour luminescent lettering in rainbow printing (BMI #4)"),
        ("Embedded transparent hologram or Kinegram", "COMPARABLE", "Identigram®: holographic portrait, 3D eagle, kinematic structures (BMI #3)"),
        ("Tactile cold-laser factory card number", "COMPARABLE", "Tactile laser-engraved expiry date and 6-digit CAN (BMI #2)"),
        ("IR-reactive ink", "NOT PUBLISHED", "No infrared feature in the public BMI guide"),
        ("Contactless smart-card technology", "IN USE", "Contactless chip since 1 November 2010 (PAP)"),
        ("Many agencies' services on the card: health, social security, social insurance", "COMPARABLE", "eID online identity for digital government and business services (BMI, PAP)"),
        ("Biometrics: fingerprints, iris, facial recognition", "PARTLY", "Facial image + 2 fingerprints on the chip (mandatory since 2 Aug 2021); iris not listed"),
    ]
    rh, g = 0.56, 0.07; y = y0 + 0.35
    for i, (eg, st, de) in enumerate(rows):
        rect(s, LX, y, LW, rh, fill=C["s1"], alpha=0.9, line=C["org"], lw=0.5, lalpha=0.5, r=0.06)
        text(s, LX + 0.12, y, 0.4, rh, f"{i+1:02d}", size=12, font=F["disp_md"], color=C["org"], anchor="ctr")
        text(s, LX + 0.55, y, LW - 0.65, rh, eg, size=11, color=C["txt"], anchor="ctr", ls=1.05)
        line(s, LX + LW, y + rh / 2, RX, y + rh / 2, C["line2"], 0.75)
        cw_ = 1.55
        fill = {"IN USE": C["org"], "PARTLY": C["deep"]}.get(st)
        colr = {"IN USE": C["ink"], "PARTLY": C["txt"], "COMPARABLE": C["txt"], "NOT PUBLISHED": C["mute"]}[st]
        chip(s, MX2 + (MW2 - cw_) / 2, y + (rh - 0.3) / 2, st, fill=fill or C["coal"], color=colr, w=cw_, h=0.3, size=9.5,
             line_c=None if fill else (C["org"] if st == "COMPARABLE" else C["line2"]))
        rect(s, RX, y, RW, rh, fill=C["s1"], alpha=0.9, line=C["line2"], lw=0.5, r=0.06)
        text(s, RX + 0.15, y, RW - 0.3, rh, de, size=11, color=C["txt2"] if st == "NOT PUBLISHED" else C["txt"], anchor="ctr", ls=1.05)
        y += rh + g
    text(s, MX, y + 0.02, SW - 2 * MX, 0.22, "No new Egyptian card design had been announced as of May 2026 (secondary source: Annahar fact-check). “Comparable” = similar purpose, different technology.",
         size=9, color=C["mute"])
    chrome(s, "en", 6, 30, TOTAL, "SP1 · pp.20–21 · BMI 2024 · PAP · NAH")
    notes(s,
        "The lecture's future vision for developing the national ID project: first, new security features — iridescent overlapping fluorescent inks (UV rainbow effect), an embedded transparent hologram or Kinegram, a tactile cold laser for the factory card number, and IR-reactive ink; second, contactless smart-card technology; third, involving numerous government agencies in citizen services through applications on the card (most importantly health, social security and social insurance); fourth, adding the citizen's biometric data (fingerprints, iris scans, facial recognition) to prevent fraud and identity theft. Germany today: UV eagle and multicolour lettering in rainbow printing (in use); the Identigram holographic element (comparable to an embedded hologram); tactile laser-engraved expiry date and CAN (comparable to a tactile laser number); no IR feature in the public guide (may exist undisclosed); a contactless chip since 2010 (in use); the eID function for digital government and business services (comparable to multi-agency applications); facial image and two fingerprints on the chip, mandatory since 2 August 2021 — iris is not listed (partly). As of May 2026 no new Egyptian card design had been announced, according to a secondary fact-check source.",
        "الرؤية المستقبلية في المحاضرة لتطوير مشروع الرقم القومي: أولًا علامات تأمين جديدة — أحبار فلورية متداخلة قزحية (UV Rainbow)، وهولوجرام أو كينجرام شفاف مدمج، وليزر بارد ملموس لرقم المصنع، وأحبار تتفاعل مع الأشعة تحت الحمراء؛ ثانيًا تقنية البطاقة الذكية اللاتلامسية؛ ثالثًا إشراك جهات حكومية عديدة عبر تطبيقات على البطاقة (الصحة والضمان الاجتماعي والتأمينات)؛ رابعًا إضافة القياسات الحيوية (البصمات والقزحية والتعرف على الوجه). ألمانيا اليوم: نسر وكتابة UV بطباعة قزحية (مستخدم)، وIdentigram (مماثل للهولوجرام المدمج)، وتاريخ انتهاء وCAN بارزان بالليزر (مماثل)، ولا توجد علامة IR في الدليل العام، وشريحة لاتلامسية منذ 2010 (مستخدم)، ووظيفة eID للخدمات الرقمية (مماثل)، وصورة الوجه وبصمتان على الشريحة منذ 2 أغسطس 2021 دون ذكر القزحية (جزئيًا). وحتى مايو 2026 لم يُعلن تصميم جديد للبطاقة المصرية بحسب تدقيق صحفي (مصدر ثانوي).",
        "SP1 p.20 (new security features), p.21 (contactless, agencies, biometrics); BMI flyer May 2024 (#2, #3, #4, chip, eID); PAP (chip since 1 Nov 2010; fingerprints from 2 Aug 2021); NAH (Annahar FactCheck, May 2026 — secondary).")
    return s

# ------------------------------------------------------------------ 31 AR finishing & durability (chapter 07 opener)
def s31(D):
    s = D.new(); bg(s, "bg_opener_l.jpg")
    opener_numeral(s, 7)
    text(s, MX, 4.15, 4.0, 0.4, "التشطيب والمتانة", size=20, font=F["ar"], bold=True, align="l", rtl=True)
    text(s, MX, 4.62, 3.95, 1.6, "الطبقة الرابعة — وقد لا تكون ضرورية — ألواح شفافة أو بعلامات متغيرة بصريًا كالهولوجرام الشفاف، موضعية أو تغطي السطح كله، لزيادة التأمين وحماية البيانات من العبث.",
         size=12.5, font=F["ar_lt"], color=C["txt"], ls=1.25, align="l", rtl=True)
    X, W = 5.3, SW - MX - 5.3
    title_ar(s, "مصمَّمة لتدوم طوال صلاحيتها", w=W, size=32)
    sub(s, "مبدأ المحاضرة: كل عناصر المستند متكاملة ومتساوية في المتانة طوال عمره.", X, 1.5, W, 0.4)
    stats = [("7", "سنوات", "صلاحية البطاقة المصرية", "مصدر ثانوي", C["org"]),
             ("10", "سنوات", "صلاحية البطاقة الألمانية — 6 سنوات قبل سن 24، دون تمديد", "PAuswG §6", C["txt"]),
             ("3–5", "سنوات", "العمر المتوقع لبطاقات PVC بحسب المحاضرة", "SP2 · p.24", C["mute"])]
    sw_ = (W - 2 * 0.2) / 3
    for i, (n, u, d, src, col) in enumerate(stats):
        x = SW - MX - (i + 1) * sw_ - i * 0.2
        rect(s, x, 2.15, sw_, 1.85, fill=C["s1"], alpha=0.9, line=col if i < 2 else C["line2"], lw=0.75, r=0.1)
        text(s, x + 0.2, 2.2, sw_ - 0.4, 0.95, [[(n, {"font": F["disp_lt"], "size": 60, "color": col if i < 2 else C["txt2"], "rtl": False}),
                                                ("  " + u, {"font": F["ar_md"], "size": 14, "color": C["txt"]})]], align="r")
        text(s, x + 0.2, 3.15, sw_ - 0.4, 0.55, d, size=11, font=F["ar"], color=C["txt"], ls=1.15)
        text(s, x + 0.2, 3.68, sw_ - 0.4, 0.25, src, size=9, font=F["ar"] if is_ar(src) else F["body"], color=C["mute"], rtl=is_ar(src), align="r")
    # finishing comparison
    bw = (W - 0.2) / 2
    boxes = [(SW - MX - bw, "مصر — تشطيب موضعي", C["org"], "eg_m_kinegram.png",
              "طابع كينجرام شفاف في منفذ على الظهر برأس توت عنخ آمون — لوح محدد الموقع والأبعاد."),
             (X, "ألمانيا — حماية السطح كله", C["txt"], "de_m_identigram_blue.png",
              "Identigram® هولوجرافي، وطلاء حماية على السطح كله يمنع التلف في الاستخدام العادي، وبروز سطحي ملموس على الظهر.")]
    for x, t, col, im, d in boxes:
        rect(s, x, 4.2, bw, 1.55, fill=C["s1"], alpha=0.9, line=col, lw=0.75, lalpha=0.7, r=0.1)
        frame_pic(s, im, x + 0.15, 4.35, 1.1, 1.25, 0.5, 0.4, r=0.06)
        text(s, x + 1.4, 4.32, bw - 1.55, 0.35, t, size=13.5, font=F["ar_sb"], color=col)
        text(s, x + 1.4, 4.7, bw - 1.55, 1.0, d, size=11, font=F["ar"], color=C["txt2"], ls=1.15)
    rect(s, X, 5.95, W, 0.85, fill=C["deep"], alpha=0.35, line=C["org"], lw=0.6, r=0.08)
    text(s, X + 0.2, 5.95, W - 0.4, 0.85, [[("من المحاضرة: ", {"font": F["ar_sb"], "color": C["org"]}),
                                            ("عمر بطاقات PVC أقصر من بطاقات الهوية لضعف مقاومتها للحرارة والأحمال والثني والأشعة فوق البنفسجية؛ والبولي كربونات يميل إلى الهشاشة والتشقق مع كثرة الاستخدام.", {})]],
         size=11.5, color=C["txt"], anchor="ctr", ls=1.2)
    chrome(s, "ar", 7, 31, TOTAL, "SP2 · pp.11, 15, 21, 24 · PAuswG §6 · WIKI-EG · PAP")
    notes(s,
        "التشطيب في المحاضرة هو الطبقة الرابعة والأخيرة، وقد تكون غير ضرورية أحيانًا: ألواح شفافة أو ألواح شفافة بعلامات متغيرة بصريًا كالهولوجرام الشفاف، محددة الموقع والأبعاد أو تغطي سطح المستند كله، لزيادة التأمين وحماية البيانات من العبث، بعملية تشبه التغليف. ومبدأ المتانة: يجب أن تكون طريقة التشخيص متينة بما يناسب عمر المستند، وأن تكون كل عناصر المستند متكاملة ومتساوية في المتانة طوال عمره. الصلاحية: البطاقة المصرية 7 سنوات (مصدر ثانوي)، والألمانية 10 سنوات، و6 سنوات لمن هم دون 24 عامًا، دون تمديد (قانون بطاقة الهوية §6). ومن المحاضرة: العمر المتوقع لبطاقات PVC بين 3 و5 سنوات، وهو أقصر من بطاقات الهوية ورخص القيادة بسبب ضعف مقاومتها؛ والبولي كربونات يميل إلى الهشاشة وسطحه عرضة للتشقق مع كثرة الاستخدام. مصر: كينجرام موضعي؛ ألمانيا: Identigram وطلاء حماية على السطح كله وبروز سطحي.",
        "Finishing in the lecture is the fourth and final layer, sometimes unnecessary: transparent panels, or transparent panels with visually variable markings such as transparent holograms, either specific in location and dimension or covering the whole surface, increasing security and protecting data from tampering — similar to lamination. Durability principle: the personalization method must be durable for the document's service life, and all elements must be integrated and equally durable throughout its lifetime. Validity: the Egyptian card 7 years (secondary source); the German card 10 years, 6 years for holders under 24, with no extension (PAuswG §6). From the lecture: PVC cards have an expected life of 3–5 years — shorter than ID cards and driving licences because of their lower resistance; polycarbonate tends to become brittle and its surface may crack with frequent use. Egypt: a local Kinegram panel; Germany: Identigram, protective lacquer over the whole surface, tactile surface embossing.",
        "SP2 p.11 (fourth layer), p.15 (durability), p.21 (polycarbonate brittleness), p.24 (PVC 3–5 years); PAuswG §6 (validity); WIKI-EG (7 years — secondary); PAP (protective lacquer); BMI flyer (#3, #8).")
    return s

# ------------------------------------------------------------------ 32 EN design & visual identity (chapter 08 opener)
def s32(D):
    s = D.new(); bg(s, "bg_opener_r.jpg")
    text(s, SW - 4.95, 0.5, 4.6, 2.95, "08", size=170, font=F["disp_lt"], color=C["txt"], rtl=False, align="r")
    label(s, MX, 0.95, 7, "CHAPTER 08 · VERDICT — DESIGN FIRST")
    title_en(s, [("DESIGN &", False)], y=1.3, w=8, size=46)
    title_en(s, [("VISUAL IDENTITY", True)], y=1.95, w=8, size=46)
    sub(s, "Design carries national identity — and much of the security.", MX, 2.72, 7.4, 0.4, size=13.5)
    rows = [
        ("LANGUAGE", "Arabic only, right-to-left; calligraphic title; data in Eastern Arabic numerals (lecture card).",
         "Labels in German, English and French; Latin data in capitals; 3-line MRZ."),
        ("MOTIFS", "Giza pyramids & Sphinx (front); pharaonic relief scene, Tutankhamun Kinegram, eagle emblem (back).",
         "Federal eagle (front), Brandenburg Gate (back), EU flag with “DE”; map of Germany embossed."),
        ("PORTRAIT", "One portrait, front left; the Multi Laser Image shows date of birth and emblem, not the face.",
         "Portrait three times: inkjet colour photo, green holographic Identigram, variable laser image."),
    ]
    y = 3.55; cw = 3.05; lx = MX; ex = MX + 1.25; dx = ex + cw + 0.2
    text(s, ex, y - 0.32, cw, 0.25, "EGYPT", size=10, font=F["disp_md"], color=C["org"], spc=150)
    text(s, dx, y - 0.32, cw, 0.25, "GERMANY", size=10, font=F["disp_md"], color=C["txt"], spc=150)
    for nm, eg, de in rows:
        line(s, lx, y, dx + cw, y, C["line"], 0.5)
        text(s, lx, y + 0.08, 1.2, 0.3, nm, size=12, font=F["disp"], spc=80, color=C["txt2"])
        text(s, ex, y + 0.07, cw, 0.75, eg, size=10.5, color=C["txt"], ls=1.08)
        text(s, dx, y + 0.07, cw, 0.75, de, size=10.5, color=C["txt"], ls=1.08)
        y += 0.8
    line(s, lx, y, dx + cw, y, C["line"], 0.5)
    text(s, lx, y + 0.1, 1.2, 0.3, "COLOUR", size=12, font=F["disp"], spc=80, color=C["txt2"])
    for k, (key, xx) in enumerate([("eg", ex), ("de", dx)]):
        sws = SWATCH[key]; sw_ = (cw - 4 * 0.06) / 5
        for j, (nm, hx) in enumerate(sws):
            rect(s, xx + j * (sw_ + 0.06), y + 0.1, sw_, 0.42, fill=hx, line=C["line2"], lw=0.5, r=0.04)
            text(s, xx + j * (sw_ + 0.06) - 0.03, y + 0.55, sw_ + 0.06, 0.32, nm, size=7, color=C["txt2"], align="c", ls=0.95)
    text(s, lx, y + 0.9, dx + cw - lx, 0.22, "Swatches sampled from the specimen images (screen colours, not ink specifications).", size=8.5, color=C["mute"])
    # cards (right)
    card_img(s, "eg_front.png", 8.55, 3.45, 3.25, EGR)
    card_img(s, "de_front.png", 9.45, 4.7, 3.25, DEF)
    text(s, 8.55, 6.82, SW - MX - 8.55, 0.2, "Specimens: Wikimedia (EG) · Personalausweisportal (DE)", size=8.5, color=C["mute"], align="r")
    chrome(s, "en", 8, 32, TOTAL, "SP1 · pp.7, 12–19 · BMI 2024 · PAP · WM-EG")
    notes(s,
        "Design is one of the three axes of the assignment. Language: the Egyptian card is Arabic only, written right to left, with a calligraphic title 'Arab Republic of Egypt — Identity Verification Card'; the lecture's sample card shows the data in Eastern Arabic numerals. The German card labels every field in German, English and French, prints data in Latin capitals and carries a three-line machine-readable zone. Motifs: Egypt uses the Giza pyramids and the Sphinx on the front and, on the back, a pharaonic relief scene, the Tutankhamun Kinegram and the eagle emblem; Germany uses the federal eagle on the front, the Brandenburg Gate on the back, the EU flag with 'DE', and an embossed map of Germany. Portrait: Egypt shows one portrait at the front left, and its Multi Laser Image shows the date of birth and emblem; Germany repeats the portrait three times — the inkjet colour photo, the green holographic portrait in the Identigram and the variable laser image. Colour swatches were sampled from the specimen images; they are screen colours, not ink specifications.",
        "التصميم أحد محاور المقارنة الثلاثة في التكليف. اللغة: البطاقة المصرية بالعربية فقط من اليمين لليسار، بعنوان بخط عربي «جمهورية مصر العربية — بطاقة تحقيق الشخصية»، وتظهر البيانات في بطاقة المحاضرة بالأرقام العربية المشرقية. والبطاقة الألمانية تكتب كل حقل بالألمانية والإنجليزية والفرنسية، والبيانات بحروف لاتينية كبيرة، مع منطقة قراءة آلية من ثلاثة أسطر. الرموز: مصر — الأهرامات وأبو الهول على الوجه، ومشهد فرعوني بارز وكينجرام توت عنخ آمون وشعار النسر على الظهر؛ ألمانيا — النسر الاتحادي على الوجه، وبوابة براندنبورغ على الظهر، وعلم الاتحاد الأوروبي بحرفي DE، وخريطة ألمانيا البارزة. الصورة الشخصية: مصر — صورة واحدة على يسار الوجه، والصورة الليزرية المتعددة تُظهر تاريخ الميلاد والشعار؛ ألمانيا — تتكرر الصورة ثلاث مرات: الصورة الملونة بالحبر النفاث، والصورة الهولوجرافية في Identigram، وصورة الليزر المتغيرة. الألوان مأخوذة من صور النماذج وهي ألوان شاشة لا مواصفات أحبار.",
        "SP1 p.7 (lecture card, Eastern Arabic numerals), pp.12–19 (Egyptian design elements); WM-EG specimen; BMI flyer May 2024 (#1, #3, #8, #9; back specimen); PAP (front specimen). Swatches sampled by the authors.")
    return s

SLIDES = [s27, s28, s29, s30, s31, s32]
