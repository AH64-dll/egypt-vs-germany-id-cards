"""Slides 21–26: chapter 05 (personalization) and chapter 06 opener + Egyptian verification levels."""
from common import *

EGR = 2456 / 1508   # eg_front / eg_back aspect
DEF = 1008 / 635    # de_front aspect
DEB = 1026 / 648    # de_back aspect

def badge_at(s, x, y, w, h, fx, fy, n, d=0.3, size=11, fill=None, txt_c=None):
    cx, cy = x + fx * w, y + fy * h
    o = num_badge(s, cx, cy, n, d=d, size=size, fill=fill, txt_c=txt_c)
    effects(o, shadow=(8, 2, 90, "000000", 0.6))
    return cx, cy

# ------------------------------------------------------------------ 21 AR personalization criteria (chapter 05 opener)
def s21(D):
    s = D.new(); bg(s, "bg_opener_l.jpg")
    opener_numeral(s, 5)
    text(s, MX, 4.15, 4.0, 0.4, "التشخيص (Personalization)", size=20, font=F["ar"], bold=True, align="l", rtl=True)
    text(s, MX, 4.62, 3.95, 1.5, "إضافة صورة الحامل وبياناته المتغيرة إلى المستند بطرق الطباعة الرقمية — في جواز السفر أو بطاقة الهوية أو حتى النماذج الورقية.",
         size=13, font=F["ar_lt"], color=C["txt"], ls=1.25, align="l", rtl=True)
    text(s, MX, 5.95, 3.95, 0.8, [[("القاعدة: ", {"font": F["ar_sb"], "color": C["org"]}),
                                   ("في الهويات والجوازات تأتي التكلفة بعد الأمان والمتانة والجودة.", {})]],
         size=12, color=C["txt2"], ls=1.2, align="l", rtl=True)
    X, W = 5.3, SW - MX - 5.3
    title_ar(s, "أربعة معايير لاختيار طريقة التشخيص", w=W, size=32)
    sub(s, "معايير المحاضرة لاختيار طرق الطباعة الرقمية التي تُضيف الصورة والبيانات المتغيرة إلى المطبوعات المؤمَّنة.", X, 1.55, W, 0.7)
    cols = [
        ("01", "القدرة التأمينية", "أن تضيف الطريقة قيمة تأمينية تناسب نوع المستند، لا أن تصبح عنصرًا يُضعفه.", "الهدف الأساسي", 2.55),
        ("02", "المتانة", "أن تدوم البيانات والصور طوال عمر المستند؛ كل عناصره متكاملة ومتساوية في المتانة.", "بعمر المستند", 2.95),
        ("03", "الجودة", "أعلى جودة للبيانات والصور ليتم التحقق بلا لبس — فالمستند يمنح حقوقًا مدنية أو مالية.", "تحقق بلا لبس", 2.95),
        ("04", "التكلفة", "مهمة في المطبوعات قصيرة العمر كالتذاكر، وتتراجع أمام الأمان في الهويات والجوازات وبطاقات الائتمان.", "أولوية أدنى", 5.3),
    ]
    gap = 0.16; cw = (W - 3 * gap) / 4; base = 6.75
    for i, (n, t, d, tag, top) in enumerate(cols):
        x = SW - MX - (i + 1) * cw - i * gap
        h = base - top
        if i < 3:
            c1 = [C["org"], C["org2"], C["deep"]][i]
            rect(s, x, top, cw, h, grad=[(0, c1, 1), (100, "1A0A05", 1)], angle=90, r=0.08)
            text(s, x + 0.18, top + 0.15, cw - 0.36, 0.6, n, size=34, font=F["disp_lt"], color=C["txt"], align="r", rtl=False)
            text(s, x + 0.18, top + 0.85, cw - 0.36, 0.45, t, size=17, font=F["ar_sb"], color=C["txt"])
            text(s, x + 0.18, top + 1.35, cw - 0.36, 1.9, d, size=11.5, font=F["ar"], color=C["txt"], ls=1.25)
            chip(s, x + cw - 0.18 - 1.25, base - 0.45, tag, fill="000000", color=C["txt"], w=1.25, h=0.28, size=10)
        else:
            # cost: dashed outline = short-life prints (tickets); solid stub = ID documents
            rect(s, x, 3.35, cw, base - 3.35, line=C["mute"], lw=0.9, dash="dash", r=0.08)
            text(s, x + 0.18, 3.45, cw - 0.36, 0.6, n, size=34, font=F["disp_lt"], color=C["txt2"], align="r", rtl=False)
            text(s, x + 0.18, 4.1, cw - 0.36, 0.45, t, size=17, font=F["ar_sb"], color=C["txt"])
            text(s, x + 0.18, 4.55, cw - 0.36, 1.0, "التذاكر والمطبوعات قصيرة العمر: التكلفة أهم.", size=10.5, font=F["ar"], color=C["txt2"], ls=1.2)
            rect(s, x, top, cw, h, fill=C["s2"], line=C["line2"], lw=0.75, r=0.08)
            text(s, x + 0.15, top + 0.12, cw - 0.3, 1.0, "الهويات والجوازات وبطاقات الائتمان: تتراجع أمام الأمان والمتانة والجودة.", size=10.5, font=F["ar"], color=C["txt"], ls=1.2)
            chip(s, x + cw - 0.18 - 1.25, base - 0.45, tag, fill=C["org"], color=C["ink"], w=1.25, h=0.28, size=10)
    text(s, X, 6.82, W, 0.22, "ارتفاع الأعمدة رسم مفاهيمي لأولويات المحاضرة وليس قياسًا.", size=9, color=C["mute"], font=F["ar"])
    chrome(s, "ar", 5, 21, TOTAL, "SP2 · pp.12–17")
    notes(s,
        "معايير اختيار طرق الطباعة الرقمية لتشخيص المطبوعات في المحاضرة أربعة: (1) القدرة التأمينية: عند اختيار طريقة رقمية لإضافة صورة أو بيانات متغيرة — في الجوازات أو بطاقات الهوية أو حتى النماذج الورقية — يكون الهدف الأساسي هو القيمة التأمينية التي تضيفها الطريقة للمستند لا أن تُضعفه، ويجب أن تناسب نوع المستند. (2) المتانة: متانة مناسبة لعمر المستند حتى لا تتلف البيانات أو الصور قبل انتهاء عمره، وكل عناصر المستند متكاملة ومتساوية في المتانة. (3) الجودة: لأن هذه المستندات تمنح أصحابها حقوقًا مدنية أو مالية، يجب أن تكون البيانات والصور بأعلى جودة لضمان أقصى تحقق دون لبس. (4) التكلفة: عامل مهم، لكنه يتضاءل أمام عامل الأمان؛ فهو أهم للمطبوعات قصيرة العمر أو أحادية الاستخدام كتذاكر القطارات والمباريات، بينما يتراجع في المستندات المهمة كبطاقات الائتمان والجوازات وبطاقات الهوية أمام الأمان والمتانة والجودة، لأن قيمتها ترتبط بالأمن القومي أو بقيمة مالية. ارتفاع الأعمدة رسم مفاهيمي.",
        "The lecture's four criteria for selecting digital printing methods to personalize printed matter: (1) Security capacity — when choosing a digital method to add an image or variable data (passports, ID cards, even paper forms) the primary goal is the security value it adds, never diminishing the document's strength; it must suit the document type. (2) Durability — commensurate with the document's service life, so data and images are not damaged or erased early; all elements integrated and equally durable. (3) Quality — these documents grant civil or financial rights, so data and images must be of the highest quality for unambiguous verification. (4) Cost — important, but it pales next to security; it matters more for short-life or single-use prints (railway, venue or match tickets), while for credit cards, passports and ID cards it takes a back seat to security, durability and quality, because their value relates to national security or money. Column heights are conceptual.",
        "SP2 p.13 (four criteria), p.14 (security/insurance capacity), p.15 (durability), p.16 (quality), p.17 (cost).")
    return s

# ------------------------------------------------------------------ 22 EN Egypt personalization
def s22(D):
    s = D.new(); bg(s, "bg_glow_tr.jpg")
    title_en(s, [("PERSONALIZING THE ", False), ("EGYPTIAN", True), (" CARD", False)], y=0.78, w=11, size=40)
    sub(s, "What turns a printed blank into one citizen's card — as documented in the lecture.", MX, 1.42, 9, 0.4, size=13.5)
    CW = 5.9; CH = CW / EGR; CX, CY = MX, 1.95
    card_img(s, "eg_front.png", CX, CY, CW, EGR)
    for fx, fy, n in [(0.30, 0.15, 1), (0.935, 0.30, 2), (0.935, 0.81, 3), (0.075, 0.79, 4), (0.075, 0.93, 5)]:
        badge_at(s, CX, CY, CW, CH, fx, fy, n)
    text(s, CX, CY + CH + 0.06, CW, 0.22, "Specimen image: field labels only, no personal data (Wikimedia Commons, CC BY-SA 3.0).", size=8.5, color=C["mute"])
    # national number structure
    NY = 6.22
    label(s, MX, NY - 0.36, 3.3, "14-DIGIT NATIONAL NUMBER")
    text(s, MX + 2.75, NY - 0.35, CW - 2.75, 0.25, "placeholder letters · structure from Wikipedia (secondary)", size=8.5, color=C["mute"], align="r")
    groups = [("C", 1, "CENTURY"), ("YYMMDD", 6, "DATE OF BIRTH"), ("GG", 2, "GOVERNORATE"), ("SSSS", 4, "SERIAL · PARITY = GENDER"), ("K", 1, "CHECK")]
    bw, bg_, gg = 0.34, 0.04, 0.14; x = MX
    for gi, (chars, k, lab) in enumerate(groups):
        gx = x
        for j in range(k):
            rect(s, x, NY, bw, 0.4, fill=C["org"] if gi == 1 else C["s2"], line=C["org"] if gi != 1 else None, lw=0.6, r=0.04)
            text(s, x, NY, bw, 0.4, chars[j], size=12, font=F["disp_md"], color=C["ink"] if gi == 1 else C["txt"], align="c", anchor="ctr", rtl=False)
            x += bw + bg_
        gw = x - bg_ - gx
        text(s, gx - 0.25, NY + 0.45, gw + 0.5, 0.25, lab, size=7.5, font=F["disp_md"], color=C["txt2"], align="c", spc=40)
        x += gg
    # legend (right)
    RX = 6.95; RW = SW - MX - RX
    items = [("PORTRAIT", "Holder's photo, front left."),
             ("ARABIC DATA", "Name and address on the front; profession, gender, religion, marital status, issue & expiry dates on the back."),
             ("NATIONAL NUMBER", "14 digits, printed on front and back."),
             ("MULTI LASER IMAGE", "Below the photo, felt with the fingers; date of birth and the national emblem swap with the viewing angle."),
             ("FACTORY NUMBER", "From a secret equation, unique to each card, registered in the national ID database against the holder's name."),
             ("2D BARCODE · BACK", "The holder's data in encrypted form — decoded to compare with the printed data. PDF417 format (secondary source).")]
    y = 1.95
    for i, (t, d) in enumerate(items):
        num_badge(s, RX + 0.15, y + 0.15, i + 1, d=0.3, size=11, fill=C["org"] if i != 5 else C["txt"])
        hh = 0.4 if len(t + d) < 70 else 0.56
        text(s, RX + 0.45, y, RW - 0.45, hh, [[(t + "  ", {"font": F["disp"], "size": 13, "spc": 60, "color": C["txt"]}), (d, {})]],
             size=11, color=C["txt2"], ls=1.1)
        y += hh + 0.07
    # MLI loupe (masked lecture photo) + barcode strip
    yb = 6.3
    frame_pic(s, "eg_m_mli_lecture.png", RX, yb - 0.08, 1.35, 0.64, r=0.06)
    text(s, RX + 1.45, yb - 0.08, 1.6, 0.64, "MLI on a real card — lecture photo, data masked.", size=8.5, color=C["mute"], anchor="ctr", ls=1.05)
    frame_pic(s, "eg_m_barcode.png", RX + 3.15, yb - 0.08, RW - 3.15, 0.64, r=0.06)
    rect(s, RX, 5.42, RW, 0.62, fill=C["s1"], line=C["org"], lw=0.6, r=0.08)
    text(s, RX + 0.18, 5.42, RW - 0.36, 0.62, [[("NOT DOCUMENTED  ", {"font": F["disp_md"], "color": C["org"], "spc": 120, "size": 10}),
                                              ("The personalization process itself (laser, thermal or inkjet) is not stated by the lecture or any official source we found.", {})]],
         size=10.5, color=C["txt2"], anchor="ctr", ls=1.1)
    chrome(s, "en", 5, 22, TOTAL, "SP1 · pp.12–15 · WIKI-EG · WM-EG")
    notes(s,
        "Personalization of the Egyptian Identity Verification Card, as documented. (1) Portrait on the front left. (2) Arabic data: first name, rest of the name and address on the front; profession, gender, religion and marital status on the back, plus issue and expiry dates (expiry printed on cards issued from 2009 — secondary source). (3) The 14-digit national number on front and back. (4) The Multi Laser Image, below the citizen's photo: it can be felt with the fingers, and the visibility of the date of birth and the emblem of the Republic changes with the viewing angle. (5) The factory number: prepared according to a secret equation, linked to each individual card, cannot be duplicated, registered in the national ID database linked to the owner's name, and verified by checking that database. (6) The 2D barcode on the back holds the citizen's data in encrypted form; decoding it allows comparison with the eye-readable data and electronic transfer to other beneficiary agencies; it follows PDF417 (secondary source). National number structure (secondary source): century digit, date of birth YYMMDD, two-digit governorate code, four-digit serial whose parity marks gender, and a check digit — shown with placeholder letters only. Not documented: the personalization process (laser, thermal or inkjet) is not stated by the lecture or any official source we found.",
        "تشخيص بطاقة تحقيق الشخصية المصرية كما هو موثّق: (1) صورة الحامل على يسار الوجه. (2) البيانات العربية: الاسم الأول وباقي الاسم ومحل الإقامة على الوجه؛ والمهنة والنوع والديانة والحالة الاجتماعية وتاريخا الإصدار والانتهاء على الظهر (يُطبع تاريخ الانتهاء منذ 2009 — مصدر ثانوي). (3) الرقم القومي من 14 رقمًا على الوجهين. (4) الصورة الليزرية المتعددة أسفل صورة المواطن، بارزة تُحَس بالأصابع، ويتبادل ظهور تاريخ الميلاد وشعار الجمهورية بتغيير زاوية النظر. (5) رقم المصنع: يُعد وفق معادلة سرية ويرتبط بكل بطاقة على حدة ولا يمكن تكراره، ويُسجل على قاعدة بيانات الرقم القومي مرتبطًا باسم المواطن، ويُتحقق منه بمراجعة القاعدة. (6) الباركود ثنائي الأبعاد على الظهر يحمل بيانات المواطن مشفرة، ويمكن بفك شفرته مقارنتها بالبيانات المقروءة بالعين ونقلها إلكترونيًا للجهات المستفيدة، ونوعه PDF417 (مصدر ثانوي). بنية الرقم القومي (مصدر ثانوي): رقم القرن، ثم تاريخ الميلاد، ثم كود المحافظة، ثم رقم تسلسلي يدل فرديه أو زوجيه على النوع، ثم رقم تحقق — معروضة بحروف رمزية فقط. غير موثق: طريقة التشخيص نفسها (ليزر أو حرارية أو نفث حبر) لا تذكرها المحاضرة ولا مصدر رسمي.",
        "SP1 p.13 (MLI), p.15 (factory number, 2D barcode); WIKI-EG (national number structure, PDF417, expiry from 2009 — secondary); WM-EG specimen image (CC BY-SA 3.0); lecture card photo SP1 p.7 with personal data masked.")
    return s

# ------------------------------------------------------------------ 23 AR Germany personalization
def s23(D):
    s = D.new(); bg(s, "bg_glow_bl.jpg")
    CW = 4.4
    FX, FY = MX, 0.9; FH = CW / DEF
    BX, BY = MX, FY + FH + 0.15; BH = CW / DEB
    card_img(s, "de_front.png", FX, FY, CW, DEF)
    card_img(s, "de_back.png", BX, BY, CW, DEB)
    for fx, fy, n in [(0.06, 0.27, 1), (0.75, 0.165, 1), (0.62, 0.43, 2), (0.69, 0.81, 3), (0.86, 0.69, 3), (0.40, 0.66, 4)]:
        badge_at(s, FX, FY, CW, FH, fx, fy, n, d=0.27, size=10)
    for fx, fy, n in [(0.26, 0.20, 5), (0.62, 0.56, 6), (0.955, 0.66, 7), (0.935, 0.33, 8)]:
        badge_at(s, BX, BY, CW, BH, fx, fy, n, d=0.27, size=10)
    text(s, MX, BY + BH + 0.05, CW, 0.22, "نموذج رسمي (MUSTER) — BMI / Personalausweisportal", size=8.5, color=C["mute"], font=F["ar"], align="l")
    X, W = 5.55, SW - MX - 5.55
    title_ar(s, "تشخيص البطاقة الألمانية", w=W, size=32)
    sub(s, "البيانات داخل الخامة لا فوقها: حبر نفاث وحفر ليزري، وشريحة تحمل نسخة رقمية.", X, 1.5, W, 0.4)
    items = [
        ("de_m_inkjet_eye.png", 0.5, 0.5, "الصورة ورقم الوثيقة", "صورة ملونة ورقم الوثيقة بالحبر النفاث داخل خامة البطاقة."),
        ("de_m_laser_text.png", 0.5, 0.5, "بقية البيانات", "حفر ليزري على الوجه والظهر."),
        ("de_m_tactile_2034.png", 0.5, 0.5, "الانتهاء ورقم CAN", "حفر ليزري بارز يُحَس باللمس؛ CAN من 6 أرقام."),
        ("de_m_identigram_d.png", 0.5, 0.3, "Identigram®", "صورة هولوجرافية خضراء للحامل ونسر أحمر ثلاثي الأبعاد."),
        ("de_m_cli_portrait.png", 0.5, 0.5, "صورة الليزر المتغيرة", "تاريخ الانتهاء أو الصورة حسب زاوية النظر (الظهر)."),
        ("de_m_thread.png", 0.5, 0.5, "خيط الأمان", "قابل للفحص آليًا ومُشخَّص برقم الوثيقة والاسم."),
        ("de_back.png", None, None, "منطقة القراءة الآلية", "3 أسطر MRZ على الظهر."),
        ("de_m_eid_logo.png", 0.5, 0.5, "الشريحة اللاتلامسية", "الصورة والبيانات وبصمتا إصبعين (إلزاميتان منذ 2 أغسطس 2021)."),
    ]
    cw = (W - 0.25) / 2; rh = 0.95; y0 = 2.12
    for i, (p, fx, fy, t, d) in enumerate(items):
        col, row = i % 2, i // 2
        x = SW - MX - (col + 1) * cw - col * 0.25; y = y0 + row * (rh + 0.06)
        rect(s, x, y, cw, rh, fill=C["s1"], alpha=0.85, line=C["line"], lw=0.5, r=0.08)
        tw, th = 1.15, rh - 0.24
        if fx is None:
            zoom_pic(s, p, x + cw - 0.12 - tw, y + 0.12, tw, th, 0.5, 0.79, 0.42, r=0.06)
        else:
            frame_pic(s, p, x + cw - 0.12 - tw, y + 0.12, tw, th, fx, fy, r=0.06)
        num_badge(s, x + cw - 0.16, y + 0.16, i + 1, d=0.26, size=10)
        text(s, x + 0.12, y + 0.1, cw - tw - 0.36, 0.32, t, size=12.5, font=F["ar_sb"], color=C["txt"])
        text(s, x + 0.12, y + 0.4, cw - tw - 0.36, rh - 0.45, d, size=10.5, font=F["ar"], color=C["txt2"], ls=1.15)
    rect(s, X, 6.3, W, 0.52, fill=C["deep"], alpha=0.35, line=C["org"], lw=0.6, r=0.08)
    text(s, X + 0.18, 6.3, W - 0.36, 0.52, [[("الخصوصية: ", {"font": F["ar_sb"], "color": C["org"]}),
                                               ("تُحذف بصمات الأصابع لدى جهة التصنيع والجهة المختصة بعد تسليم البطاقة.", {})]],
         size=11, color=C["txt"], anchor="ctr")
    chrome(s, "ar", 5, 23, TOTAL, "BMI 2024 #1–3, 9, 11, 13 · PAP · BDR")
    notes(s,
        "التشخيص في البطاقة الألمانية الحالية (التصميم الصادر منذ 2 مايو 2024): (1) صورة ملونة ورقم الوثيقة مدمجان داخل خامة البطاقة بالحبر النفاث (BMI #1). (2) بقية البيانات الشخصية محفورة بالليزر على الوجه والظهر. (3) تاريخ الانتهاء ورقم الوصول CAN المكوَّن من 6 أرقام محفوران بالليزر وبارزان يُحسّان باللمس (BMI #2). (4) Identigram: بنى حركية وصورة هولوجرافية خضراء للحامل ونسر أحمر ثلاثي الأبعاد، وتظهر عناصر زرقاء بعد تدوير البطاقة 90° (BMI #3). (5) صورة الليزر المتغيرة على الظهر: تاريخ الانتهاء أو الصورة حسب زاوية النظر (BMI #9). (6) خيط أمان قابل للفحص آليًا مُشخَّص برقم الوثيقة والاسم (BMI #11). (7) منطقة القراءة الآلية من 3 أسطر على الظهر. (8) الشريحة اللاتلامسية تحفظ الصورة والبيانات المطبوعة، وبصمتي إصبعين إلزاميًا للبطاقات الصادرة منذ 2 أغسطس 2021، وتُحذف البصمات لدى المصنّع والجهة بعد التسليم. تنتج البطاقة Bundesdruckerei لصالح وزارة الداخلية الاتحادية. ذكرت المحاضرة شركة Veridos، وهي مشروع مشترك بين Giesecke+Devrient وBundesdruckerei.",
        "Personalization of the current German ID card (design issued from 2 May 2024): (1) colour photo and document number integrated into the card material by inkjet (BMI #1); (2) other personal data laser-engraved on front and back; (3) expiry date and 6-digit card access number (CAN) laser-engraved and tactile (BMI #2); (4) Identigram: kinematic structures, green holographic portrait of the holder, red 3D eagle, blue elements after a 90° turn (BMI #3); (5) variable laser image on the back — expiry date or portrait depending on angle (BMI #9); (6) machine-verifiable security thread personalised with document number and name (BMI #11); (7) 3-line machine-readable zone on the back; (8) contactless chip storing the photo and printed data, plus two fingerprints — mandatory for cards issued from 2 August 2021; fingerprints are deleted at the manufacturer and the authority after handover. The card is produced by Bundesdruckerei for the Federal Ministry of the Interior. The lecture mentions Veridos, a joint venture of Giesecke+Devrient and Bundesdruckerei.",
        "BMI flyer May 2024 (#1, #2, #3, #9, #11, #13; fingerprint deletion); PAP (chip contents, fingerprints from 2 Aug 2021); BDR (manufacturer); SP1 p.22 (Veridos). Images: BMI flyer and Personalausweisportal specimens.")
    return s

# ------------------------------------------------------------------ 24 EN four verification levels (chapter 06 opener)
def s24(D):
    s = D.new(); bg(s, "bg_opener_r.jpg")
    text(s, SW - 4.95, 0.5, 4.6, 2.95, "06", size=170, font=F["disp_lt"], color=C["txt"], rtl=False, align="r")
    label(s, MX, 0.95, 7, "CHAPTER 06 · SECURITY FEATURES")
    title_en(s, [("WHO CAN CHECK IT,", False)], y=1.3, w=8, size=46)
    title_en(s, [("AND WITH WHAT?", True)], y=1.95, w=8, size=46)
    sub(s, "The lecture sorts the Egyptian card's features into four verification levels. We map Germany's official check methods onto the same ladder.",
        MX, 2.72, 7.2, 0.7, size=13.5)
    rows = [
        ("1", "ANYONE", "naked eye · touch · tilt", ["Multi Laser Image", "Kinegram®", "Rainbow printing", "Relief “Egypt”"],
         ["Identigram®", "OVI logo", "Tactile expiry & CAN", "Variable laser image", "Surface embossing"]),
        ("2", "SPECIALISTS", "trained eye · 5× magnifier", ["Factory number", "Visible microprint", "2D barcode"],
         ["Guilloches", "± Microprint", "Inkjet photo"]),
        ("3", "SPECIALISTS + TOOLS", "UV lamp · magnifier · reader", ["Invisible UV microtext", "Guilloche", "UV-glowing eagle"],
         ["UV eagle & lettering", "UV fibres", "Security thread", "Address-label code", "eID chip"]),
        ("4", "LABORATORY", "production centre", ["Material marks", "Intentional errors", "Filter-only text"],
         ["Not published"]),
    ]
    y0 = 3.62; rh = 0.7; g = 0.07
    LW = 3.0; EX = MX + LW + 0.12; EW = 4.4; DX = EX + EW + 0.12; DW = SW - MX - DX
    text(s, EX, y0 - 0.3, EW, 0.25, "EGYPT · LECTURE", size=10, font=F["disp_md"], color=C["org"], spc=150)
    text(s, DX, y0 - 0.3, DW, 0.25, "GERMANY · BMI CHECK METHODS (OUR MAPPING)", size=10, font=F["disp_md"], color=C["txt"], spc=150)
    for i, (n, who, how, eg, de) in enumerate(rows):
        y = y0 + i * (rh + g)
        ind = i * 0.12
        rect(s, MX + ind, y, LW - ind, rh, grad=[(0, [C["org"], C["org2"], C["deep"], "4A1A0C"][i], 1), (100, "1A0A05", 1)], angle=0, r=0.06)
        text(s, MX + ind + 0.12, y, 0.45, rh, n, size=26, font=F["disp_lt"], color=C["txt"], anchor="ctr")
        text(s, MX + ind + 0.6, y + 0.08, LW - ind - 0.7, 0.3, who, size=14, font=F["disp"], spc=60)
        text(s, MX + ind + 0.6, y + 0.37, LW - ind - 0.7, 0.28, how, size=9.5, color=C["txt"], font=F["body"])
        rect(s, EX, y, EW, rh, fill=C["s1"], alpha=0.88, line=C["org"], lw=0.5, lalpha=0.5, r=0.06)
        rect(s, DX, y, DW, rh, fill=C["s1"], alpha=0.88, line=C["line2"], lw=0.5, r=0.06)
        for (X0, W0, lst, on) in [(EX, EW, eg, True), (DX, DW, de, False)]:
            lines_, cur, cx = [], [], 0
            for t in lst:
                w = len(t) * 0.062 + 0.28
                if cur and cx + w > W0 - 0.24: lines_.append(cur); cur, cx = [], 0
                cur.append((t, w)); cx += w + 0.06
            lines_.append(cur)
            ch_ = 0.25; cy = y + (rh - (len(lines_) * ch_ + (len(lines_) - 1) * 0.06)) / 2
            for ln_ in lines_:
                cx = X0 + 0.12
                for t, w in ln_:
                    mute = t == "Not published"
                    chip(s, cx, cy, t, fill=None if mute else (C["deep"] if on else C["s3"]), color=C["mute"] if mute else C["txt"],
                         w=w, h=ch_, size=8.5, line_c=C["line2"] if mute else (C["org"] if on else C["line2"]))
                    cx += w + 0.06
                cy += ch_ + 0.06
    chrome(s, "en", 6, 24, TOTAL, "SP1 · pp.11–18 · BMI 2024")
    notes(s,
        "The lecture divides the Egyptian national ID card's security features into four groups: (1) external features that can be examined by the average person — the Multi Laser Image, the Kinegram (written 'Kingram' in the lecture), rainbow printing of the back design and relief multi-angle printing of the word 'Egypt'; (2) external features examined by specialists — the factory number, visible microprint read with simple 5× magnifiers, and the 2D barcode; (3) hidden features examined by specialists using simple testing tools — invisible UV microtext, guilloche security printing checked under a magnifier, and UV-glowing ink such as the eagle on the back; (4) features tested in the laboratory by specialists at the card production centre — marks related to the materials, intentional printing errors in confidential areas, and writing visible only under certain filters. Germany's official guide does not use these levels; it lists check methods (look, tilt, touch, magnifier, UV lamp, machine/app). We placed each German feature on the lecture's ladder by its check method: tilt/touch features at level 1; guilloches, microprint and the inkjet photo (magnifier) at level 2; UV features, the machine-verifiable thread, the address-label code (app) and the eID chip (reader) at level 3; German laboratory features are not published.",
        "تقسم المحاضرة علامات تأمين البطاقة المصرية إلى أربع مجموعات: (1) علامات ظاهرة يفحصها الشخص العادي — الصورة الليزرية المتعددة، والكينجرام، والطباعة التدريجية لتصميم الظهر، والطباعة الأمنية بزوايا متعددة لكلمة «مصر»؛ (2) علامات ظاهرة يفحصها المتخصصون — رقم المصنع، والكتابة الميكرونية الظاهرة بعدسة مكبرة 5X، والباركود ثنائي الأبعاد؛ (3) علامات خفية يفحصها المتخصصون بأدوات فحص بسيطة — الكتابة الميكرونية بأحبار خفية تحت UV، والجلوشيات تحت العدسة المكبرة، والأحبار المتألقة تحت UV كالنسر على الظهر؛ (4) علامات تُفحص معمليًا بمركز إنتاج البطاقة — علامات مرتبطة بالخامات، وأخطاء طباعية مقصودة في مناطق سرية، وكتابة لا تظهر إلا تحت مرشحات معينة. الدليل الألماني الرسمي لا يستخدم هذه المستويات بل يذكر طرق الفحص (النظر، الإمالة، اللمس، العدسة، مصباح UV، الجهاز/التطبيق)، فوزعنا الخصائص الألمانية على سلم المحاضرة حسب طريقة فحصها؛ والعلامات المعملية الألمانية غير منشورة.",
        "SP1 p.11 (four levels), pp.12–13 (level 1), pp.14–15 (level 2), pp.17–18 (level 3), p.16 (laboratory); BMI flyer May 2024 (features #1–#13 and check methods). Level assignment of German features is the authors' mapping.")
    return s

def relief_loupe(s, cx, cy, d):
    """clearly labelled illustration: the word «مصر» repeated at several angles (not card artwork)."""
    oval(s, cx - d / 2, cy - d / 2, d, d, fill=C["s1"], line=C["org"], lw=1.5)
    for k, (dy, rot) in enumerate([(-0.28, -18), (0.0, 0), (0.28, 18)]):
        tb = text(s, cx - 0.42, cy + dy - 0.17, 0.84, 0.34, "مصر  مصر", size=8.5, font=F["ar_sb"], color=C["peach"] if k == 1 else C["org2"], align="c")
        tb.rotation = rot
    num_badge(s, cx + d * 0.36, cy - d * 0.36, 4, d=0.27, size=10)
    text(s, cx - d / 2, cy + d / 2 + 0.01, d, 0.2, "رسم توضيحي", size=8, font=F["ar"], color=C["mute"], align="c")

# ------------------------------------------------------------------ 25 AR Egypt level 1 hero
def s25(D):
    s = D.new(); bg(s, "bg_glow_tl.jpg")
    BW = 5.55; BH = BW / EGR; BX, BY = MX, 1.25
    card_img(s, "eg_back.png", BX, BY, BW, EGR)
    FW = 2.55; FH = FW / EGR; FX, FY = MX, BY + BH + 0.3
    card_img(s, "eg_front.png", FX, FY, FW, EGR)
    text(s, FX + FW + 0.15, FY + 0.1, BW - FW - 0.15, 1.3, "صور البطاقة: نموذج Wikimedia بلا بيانات شخصية. تكبير الصورة الليزرية من صورة المحاضرة بعد إخفاء البيانات.",
         size=9, color=C["mute"], font=F["ar"], align="l", ls=1.15)
    LX = 6.55; D_ = 1.08
    loupes = [("eg_m_mli_lecture.png", 0.5, 0.5, (FX, FY, FW, FH, 0.07, 0.80)),
              ("eg_m_kinegram.png", 0.5, 0.45, (BX, BY, BW, BH, 0.14, 0.22)),
              ("eg_m_relief_scene.png", 0.5, 0.3, (BX, BY, BW, BH, 0.50, 0.24)),
              (None, 0, 0, (BX, BY, BW, BH, 0.28, 0.50))]
    items = [("الصورة الليزرية المتعددة", "Multi Laser Image", "أسفل صورة المواطن، بارزة تُحَس بالأصابع؛ يتبادل ظهور تاريخ الميلاد وشعار الجمهورية بتغيير زاوية النظر."),
             ("طابع الكينجرام", "KINEGRAM®", "منفذ بظهر البطاقة يُرى منه رأس تمثال توت عنخ آمون بأبعاده المختلفة بتغيير زاوية النظر رأسيًا وأفقيًا."),
             ("الطباعة التدريجية", "Rainbow printing", "لتصميم البطاقة من الخلف — من أعقد التقنيات الطباعية."),
             ("طباعة أمنية بزوايا متعددة", "Relief", "تُصمَّم ببرامج معقدة يصعب تزويرها، وتُقرأ منها كلمة «مصر» على التصميم الخلفي كاملًا.")]
    TX = LX + D_ + 0.3; TW = SW - MX - TX
    title_ar(s, "المستوى الأول: يفحصه أي شخص", w=TW + 1.4, size=30)
    sub(s, "علامات ظاهرة بجسم البطاقة تكفي فيها العين واللمس وتغيير الزاوية.", TX - 1.4, 1.42, TW + 1.4, 0.4, size=13)
    for i, ((p, fx, fy, (cx0, cy0, cw0, ch0, ax, ay)), (t, en, d)) in enumerate(zip(loupes, items)):
        y = 2.05 + i * 1.22
        lcx, lcy = LX + D_ / 2, y + D_ / 2
        tx, ty = cx0 + ax * cw0, cy0 + ay * ch0
        badge_at(s, cx0, cy0, cw0, ch0, ax, ay, i + 1, d=0.3)
        if p is None:
            relief_loupe(s, lcx, lcy, D_)
        else:
            loupe(s, p, lcx, lcy, D_, fx, fy, n=i + 1)
        text(s, TX, y + 0.02, TW, 0.36, [[(t, {"font": F["ar_sb"], "size": 15, "color": C["txt"]}), ("   " + en, {"font": F["disp_md"], "size": 11, "color": C["org"], "rtl": False})]], size=15)
        text(s, TX, y + 0.42, TW, 0.75, d, size=11.5, font=F["ar"], color=C["txt2"], ls=1.2)
    chrome(s, "ar", 6, 25, TOTAL, "SP1 · pp.12–13, 19 · WM-EG")
    notes(s,
        "أهم العلامات التأمينية الظاهرة بجسم البطاقة والتي يمكن فحصها بمعرفة الشخص العادي: (1) الصورة الليزرية المتعددة Multi Laser Image: موجودة بالجزء الأسفل لصورة المواطن ويمكن تحسسها بارزة بأصابع اليد، وتتبادل درجة رؤية تاريخ ميلاد المواطن وشعار الجمهورية من خلالها بتغيير زاوية النظر. (2) طابع الكينجرام: منفذ على الجزء الخلفي للبطاقة يمكن من خلاله رؤية رأس تمثال توت عنخ آمون بأبعاده المختلفة من خلال التغيير الرأسي والأفقي لزاوية النظر. الاسم الصحيح للمنتج KINEGRAM® (كُتب «Kingram» في المحاضرة). (3) الطباعة التدريجية لتصميم البطاقة من الخلف Rainbow printing: من التقنيات الطباعية المعقدة. (4) الطباعة الأمنية بنظام الكتابة بزوايا متعددة Relief: تُصمم ببرامج معقدة يصعب تزويرها ويُقرأ من خلالها كلمة «مصر» على التصميم الخلفي للبطاقة بالكامل. الدوائر المكبرة تُظهر مواضع العلامات على نموذج البطاقة، ولا تُظهر الأثر البصري المتغير نفسه.",
        "Level 1 — the most important visible security marks on the card body that the average person can examine: (1) Multi Laser Image — located at the bottom of the citizen's photo, can be felt easily with the fingers; the visibility of the date of birth and the emblem of the Republic changes with the viewing angle. (2) Kinegram stamp — an opening on the back through which the head of the statue of Tutankhamun can be seen in its different dimensions by changing the vertical and horizontal viewing angle; correct product name KINEGRAM® ('Kingram' in the lecture). (3) Rainbow printing of the card's back design — one of the most sophisticated printing techniques. (4) Relief — multi-angle security printing designed with complex, hard-to-counterfeit software, letting the word 'Egypt' be read across the entire back design. The loupes show where each mark sits on the specimen; they cannot show the optically variable effect itself.",
        "SP1 p.12 (Arabic feature list), p.13 (English descriptions), p.19 (labelled feature map); G6 (KINEGRAM® spelling). Images: WM-EG specimen (CC BY-SA 3.0); MLI crop from lecture photo SP1 p.7, data masked.")
    return s

# ------------------------------------------------------------------ 26 EN Egypt levels 2–4
def s26(D):
    s = D.new(); bg(s, "bg_quiet.jpg")
    title_en(s, [("BEYOND THE NAKED EYE: ", False), ("LEVELS 2–4", True)], y=0.78, w=11, size=40)
    sub(s, "Egypt's remaining features need training, a tool — or the production centre's laboratory.", MX, 1.42, 10, 0.4, size=13.5)
    cols = [
        ("02", "SPECIALISTS", "TRAINED EYE · 5× MAGNIFIER", [
            (("zoom", "eg_front.png", 0.12, 0.93, 0.32), "FACTORY NUMBER", "Secret equation; unique per card; registered in the national ID database against the holder's name."),
            (("zoom", "eg_front.png", 0.62, 0.94, 0.3), "VISIBLE MICROPRINT", "Lower front; read with a simple 5× magnifier: “Ministry of Interior – Civil Status Sector”."),
            (("pic", "eg_m_barcode.png", 0.5, 0.5), "2D BARCODE", "Back; holder data encrypted — decoded to compare with printed data and shared with other agencies.")]),
        ("03", "SPECIALISTS + TOOLS", "UV LAMP · MAGNIFIER", [
            (("pic", "eg_m_rainbow_bg.png", 0.55, 0.2), "INVISIBLE UV MICROTEXT", "Tiny lettering in inks visible only under UV: “Ministry of Interior – Civil Status Sector”."),
            (("zoom", "eg_front.png", 0.42, 0.06, 0.3), "GUILLOCHE", "Precise designs from software sold only to governments; continuous lines, not dots, under a magnifier."),
            (("pic", "eg_m_eagle.png", 0.5, 0.35), "UV-GLOWING INK", "Visible to the naked eye yet glowing under UV — e.g. the eagle on the back.")]),
        ("04", "LABORATORY", "CARD PRODUCTION CENTRE", [
            (None, "MATERIAL MARKS", "Related to the nature of the materials used to print and manufacture the card."),
            (None, "INTENTIONAL ERRORS", "Deliberate printing errors in confidential areas of the security design."),
            (None, "FILTER-ONLY TEXT", "Writing visible only under certain types of filters.")]),
    ]
    gap = 0.22; cw = (SW - 2 * MX - 2 * gap) / 3; y0 = 2.05
    for ci, (n, who, tool, items) in enumerate(cols):
        x = MX + ci * (cw + gap)
        rect(s, x, y0, cw, 4.8, fill=C["s1"], alpha=0.9, line=C["org"] if ci == 2 else C["line"], lw=0.6, r=0.1)
        text(s, x + 0.2, y0 + 0.08, 0.9, 0.7, n, size=36, font=F["disp_lt"], color=C["org"])
        text(s, x + 1.05, y0 + 0.17, cw - 1.2, 0.3, who, size=16, font=F["disp"], spc=60)
        text(s, x + 1.05, y0 + 0.47, cw - 1.2, 0.25, tool, size=9.5, font=F["disp_md"], color=C["txt2"], spc=120)
        line(s, x + 0.2, y0 + 0.88, x + cw - 0.2, y0 + 0.88, C["line2"], 0.5)
        yy = y0 + 1.03
        for (im, t, d) in items:
            tw, th = 1.15, 0.92
            if im is None:
                rect(s, x + 0.2, yy, tw, th, fill=C["coal"], line=C["line2"], lw=0.6, dash="dash", r=0.06)
                text(s, x + 0.2, yy, tw, th, "UNDISCLOSED", size=8.5, font=F["disp_md"], color=C["mute"], align="c", anchor="ctr", spc=120)
            elif im[0] == "zoom":
                zoom_pic(s, im[1], x + 0.2, yy, tw, th, im[2], im[3], im[4], r=0.06)
            else:
                frame_pic(s, im[1], x + 0.2, yy, tw, th, im[2], im[3], r=0.06)
            text(s, x + 0.2 + tw + 0.15, yy - 0.02, cw - tw - 0.55, 0.3, t, size=12, font=F["disp"], spc=50)
            text(s, x + 0.2 + tw + 0.15, yy + 0.26, cw - tw - 0.55, 0.85, d, size=10, color=C["txt2"], ls=1.08)
            yy += th + 0.28
    text(s, MX, 6.9, SW - 2 * MX, 0.2, "Thumbnails show where each feature sits on the specimen — not the feature under magnification or UV.", size=8.5, color=C["mute"])
    chrome(s, "en", 6, 26, TOTAL, "SP1 · pp.14–18")
    notes(s,
        "Level 2 — external features examined by specialists: the factory number, prepared according to a secret equation, linked to each individual card, impossible to duplicate, registered in the national ID database linked to the owner's name and verified by reviewing that database; visible microprints — extremely small inscriptions on the lower part of the card's face, seen with simple 5× magnifiers, reading 'Ministry of Interior – Civil Status Sector'; the two-dimensional barcode on the back, holding the citizen's data in encrypted form, which can be decoded, compared with the eye-readable data and transferred electronically to other beneficiary entities. Level 3 — hidden features examined by specialists with simple testing tools: micronized invisible-ink printing, tiny inks visible under UV that read 'Ministry of Interior – Civil Status Sector'; guilloche security printing — precise designs prepared with special software sold only to governments, whose lines appear connected, unlike other printing methods that appear as adjacent dots, examined under a magnifying glass; UV-glowing ink — special inks that glow under UV although visible to the naked eye, such as the eagle on the back. Level 4 — security marks tested in a laboratory: marks related to the nature of the materials used in printing and manufacturing the card, intentional printing errors in some confidential areas of the security design, and writing visible only under certain filters. Thumbnails show locations on the specimen only.",
        "المستوى الثاني — علامات ظاهرة يفحصها المتخصصون: رقم المصنع (معادلة سرية، مرتبط بكل بطاقة، لا يتكرر، مسجل على قاعدة بيانات الرقم القومي باسم المواطن ويُتحقق منه بمراجعتها)؛ والكتابة الميكرونية الظاهرة أسفل وجه البطاقة وتُقرأ بعدسة مكبرة بسيطة 5X: «وزارة الداخلية – قطاع الأحوال المدنية»؛ والباركود ثنائي الأبعاد على الظهر ببيانات مشفرة يمكن فك شفرتها ومقارنتها بالبيانات المقروءة ونقلها إلكترونيًا للجهات المستفيدة. المستوى الثالث — علامات خفية يفحصها المتخصصون بأدوات بسيطة: كتابة ميكرونية بأحبار خفية تُرى تحت الأشعة فوق البنفسجية وتُقرأ «وزارة الداخلية – قطاع الأحوال المدنية»؛ وطباعة الجلوشيات بتصميمات دقيقة ببرامج خاصة لا تُباع إلا للحكومات، خطوطها متصلة على عكس الطباعات الأخرى التي تظهر نقاطًا متجاورة، وتُفحص بالعدسة المكبرة؛ وأحبار تتألق تحت UV رغم ظهورها بالعين المجردة كالنسر المطبوع على الظهر. المستوى الرابع — علامات تُفحص معمليًا: علامات مرتبطة بطبيعة خامات الطباعة والتصنيع، وأخطاء طباعية مقصودة في مناطق سرية من التصميم الأمني، وكتابة لا تظهر إلا تحت أنواع معينة من المرشحات. الصور المصغرة تبين المواضع فقط.",
        "SP1 p.14–15 (level 2), p.16 (laboratory), pp.17–18 (level 3), p.19 (feature map). Images: WM-EG specimen (CC BY-SA 3.0).")
    return s

SLIDES = [s21, s22, s23, s24, s25, s26]
