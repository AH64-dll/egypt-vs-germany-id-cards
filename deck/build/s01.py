"""Slides 1–6: cover, roadmap, chapter 01 (context)."""
import json
from lib import *

ANCH = json.loads((ART / "anchors.json").read_text())
TOTAL = 37

def stat(s, x, y, w, num, label, ar=False, num_size=44, color=None, label_size=None):
    text(s, x, y, w, 0.75, num, size=num_size, font=F["disp_lt"], color=color or C["txt"], align="r" if ar else "l", rtl=False)
    text(s, x, y + 0.78, w, 0.6, label, size=label_size or (12.5 if ar else 11.5), color=C["txt2"],
         font=F["ar"] if ar else F["body"], align="r" if ar else "l", ls=1.05)

def anchor_xy(name, i, side, x, y, w, h):
    fx, fy = ANCH[name][i][side]
    return x + fx * w, y + fy * h

# ------------------------------------------------------------------ 01 AR cover
def s01(D):
    s = D.new(); bg(s, "bg_cover.jpg")
    g = img(s, "guilloche_rosette2.png", -5.2, -5.6, 10.4, 10.4); pic_alpha(g, 0.6)
    img(s, "cover_cards.png", -0.35, 1.05, 7.7, 5.13)
    X, W = 7.05, SW - MX - 7.05
    text(s, X, 0.42, W, 0.3, "برنامج التصميم الجرافيكي والوسائط المتعددة · الجامعة المصرية الصينية", size=10.5, color=C["txt2"], font=F["ar"])
    eyebrow_pill(s, SW - MX - 2.25, 1.22, "دراسة مقارنة · 2026/2027", ar=True, w=2.25)
    text(s, X, 1.72, W, 2.75, ["بطاقتان.", "دولتان.", [("لغة أمان واحدة.", {"color": C["org"]})]],
         size=50, font=F["ar"], bold=True, ls=0.98)
    text(s, X, 4.42, W, 1.05, "بطاقة تحقيق الشخصية المصرية في مواجهة بطاقة الهوية الألمانية: الخامات، الطباعة، التشخيص، وعلامات التأمين.",
         size=16, font=F["ar_lt"], color=C["txt2"], ls=1.15)
    line(s, X, 5.68, SW - MX, 5.68, C["line2"], 0.75)
    cols = [("إعداد", "[اسم الطالب / الطلاب]"), ("إشراف", "د. رانيا محمد"), ("المقرر", ["الطباعة الآمنة", "GDM5313"])]
    cw = W / 3
    for i, (lab, val) in enumerate(cols):
        cx = SW - MX - (i + 1) * cw
        text(s, cx, 5.82, cw - 0.12, 0.3, lab, size=10.5, color=C["org"], font=F["ar_md"])
        text(s, cx, 6.12, cw - 0.12, 0.6, val, size=13, color=C["txt"], font=F["ar"], ls=1.0)
    text(s, MX, 6.95, 6.2, 0.3, "صور مرجعية: النموذج الرسمي الألماني (BMI) · بطاقة مصرية بحقول عناوين بدل البيانات (Wikimedia Commons)",
         size=8.5, color=C["mute"], font=F["ar"], align="l")
    notes(s,
        "مرحبًا بكم. يقارن هذا العرض بين بطاقة تحقيق الشخصية المصرية وبطاقة الهوية الألمانية (Personalausweis) من زاوية مقرري الطباعة الآمنة وتقنيات ما قبل الطباعة: من خامة جسم البطاقة، إلى طباعة الخلفيات الأمنية، ثم تشخيص البيانات، وأخيرًا علامات التأمين وطرق فحصها. العرض ثنائي اللغة: كل شريحة بلغة واحدة، وملاحظات المتحدث تحمل المحتوى نفسه باللغة الأخرى.",
        "Welcome. This presentation compares the Egyptian Identity Verification Card with the German national identity card (Personalausweis) through the lens of the Security Printing and Pre-Press Technologies courses: card-body material, security background printing, personalization, and security features with their verification methods. Slides alternate Arabic and English; each slide's notes carry the same content in the other language.",
        "Images — German specimen: Personalausweisportal/BMI (fictional holder Erika Mustermann). Egyptian card: Wikimedia Commons, Heshamdiab16, CC BY-SA 3.0 (personal fields replaced by field labels by the uploader). Course: GDM5313/GDM5310, Dr. Rania Mohamed, ECU 2026/27.")
    return s

# ------------------------------------------------------------------ 02 EN roadmap
def s02(D):
    s = D.new(); bg(s, "bg_glow_tr.jpg")
    text(s, MX, 0.95, 5.4, 1.5, ["THE ROUTE", [("THROUGH A CARD", {"color": C["org"]})]], size=50, font=F["disp"], ls=0.88, caps=True)
    text(s, MX, 2.55, 4.9, 1.1, "Eight chapters follow the life-cycle of a secure document — the same order in which the lecture builds one: card body, print, personalize, finish.",
         size=14.5, color=C["txt2"], ls=1.18)
    rows = [("01", "Context", "03–06"), ("02", "Materials", "07–09"), ("03", "Layers & construction", "10–13"), ("04", "Printing technologies", "14–20"),
            ("05", "Personalization", "21–23"), ("06", "Security & authentication", "24–30"), ("07", "Finishing & durability", "31"), ("08", "Verdict", "32–36")]
    y0 = 3.85
    for i, (n, name, pg) in enumerate(rows):
        y = y0 + i * 0.37
        line(s, MX, y, MX + 4.9, y, C["line"], 0.5)
        text(s, MX, y + 0.05, 0.6, 0.3, n, size=15, font=F["disp_md"], color=C["org"])
        text(s, MX + 0.62, y + 0.06, 3.3, 0.3, name, size=13.5, font=F["body_md"], color=C["txt"])
        text(s, MX + 3.9, y + 0.07, 1.0, 0.3, pg, size=11, font=F["disp_md"], color=C["mute"], align="r", spc=80)
    line(s, MX, y0 + 8 * 0.37, MX + 4.9, y0 + 8 * 0.37, C["line"], 0.5)
    # pyramid with labels
    PX, PY, PW = 5.95, 1.0, 5.25; PH = PW * 1100 / 1200
    img(s, "pyramid_all.png", PX, PY, PW, PH)
    labels = [("CARD BODY", "Ch. 02 – 03", "material & construction"), ("PRINT", "Ch. 04", "prepress & offset backgrounds"),
              ("PERSONALIZE", "Ch. 05", "photo & holder data"), ("FINISHING", "Ch. 07", "protective layers & durability")]
    for i, (lab, ch, desc) in enumerate(labels):
        ax, ay = anchor_xy("pyramid_all", i, "right", PX, PY, PW, PH)
        lx = 10.95
        line(s, ax + 0.06, ay, lx - 0.08, ay, C["org"], 0.75, alpha=0.8); dot(s, ax + 0.06, ay, 0.07)
        text(s, lx, ay - 0.30, 1.85, 0.3, lab, size=15, font=F["disp"], color=C["txt"], spc=120)
        text(s, lx, ay - 0.02, 1.85, 0.5, [[(ch + "  ", {"color": C["org"], "font": F["disp_md"]}), (desc, {})]], size=10.5, color=C["txt2"], ls=1.0)
    text(s, 6.3, 6.45, 6.4, 0.45, "Chapters 01 · 06 · 08 wrap the stack: context, the security features that span all four layers, and the verdict.",
         size=10.5, color=C["mute"], align="r")
    chrome(s, "en", 0, 2, TOTAL, "SP2 · p.5 — document structure", eyebrow="ROADMAP")
    notes(s,
        "The lecture's 'document structure' pyramid (Card body → Print → Personalize → Finishing) is our map. Chapters 02–03 cover the card body and how layers are built; chapter 04 covers prepress and offset printing that create security backgrounds; chapter 05 covers personalization; chapter 07 covers finishing. Chapter 06 spans every layer — security features live in all four.",
        "هرم «بنية المستند» من المحاضرة (جسم البطاقة ← الطباعة ← التشخيص ← التشطيب) هو خريطتنا. الفصلان 02–03 لجسم البطاقة وبناء الطبقات، والفصل 04 لتقنيات ما قبل الطباعة والأوفست التي تُنتج الخلفيات الأمنية، والفصل 05 للتشخيص، والفصل 07 للتشطيب. أما الفصل 06 (التأمين) فيمتد عبر الطبقات الأربع كلها.",
        "SP2 p.5 (Document Structure), p.6 and p.8 (layers in chronological order of the life cycle). SP1 p.23 assignment 'Create a 3D sample of an ID card': answered by the original 3D renders in this deck (layer pyramid, exploded card, floating cards).")
    return s

# ------------------------------------------------------------------ 03 AR chapter 01 — valuable vs secure documents
def s03(D):
    s = D.new(); bg(s, "bg_opener_l.jpg")
    text(s, 0.35, 0.55, 4.6, 3.95, "01", size=230, font=F["disp_lt"], color=C["txt"], rtl=False, align="l")
    text(s, MX, 4.15, 3.9, 0.3, "هدف المقرر", size=11, font=F["ar_sb"], color=C["txt"], align="l", rtl=True)
    text(s, MX, 4.5, 3.95, 2.3, "مفهوم الطباعة الآمنة، والمواصفات الفنية لخاماتها، وتقنيات التأمين وتوظيفها، وتقنيات إنتاج العملات الورقية وبطاقات الهوية والطوابع والشهادات والأوراق الحكومية ووسائل تأمينها.",
         size=12.5, font=F["ar_lt"], color=C["txt"], ls=1.25, align="l", rtl=True)
    X, W = 5.15, SW - MX - 5.15
    text(s, X, 0.95, W, 0.8, "القيمة تستدعي التأمين", size=40, font=F["ar"], bold=True)
    text(s, X, 1.85, W, 0.45, "ما الفرق بين المستندات ذات القيمة والمستندات المؤمَّنة؟", size=16, font=F["ar_md"], color=C["org"])
    text(s, X, 2.35, W, 1.0, "القيمة هي ما تمثله الوثيقة: مال، أو حق مدني، أو هوية. والتأمين هو ما يحمي هذه القيمة: علامات تجعل الوثيقة سهلة التحقق وصعبة الاستنساخ. كل ما يلي «مطبوعات ذات قيمة» تتطلب طباعة آمنة.",
         size=14, font=F["ar_lt"], color=C["txt2"], ls=1.22)
    items = ["الأوراق النقدية (الورقية)", "العملات البوليمرية (البلاستيكية)", "رخص القيادة", "شهادات الميلاد", "شهادات القيادة",
             "الشهادات العسكرية", "شهادات الوفاة", "بطاقات تحقيق الشخصية", "تذاكر النقل (برًا وبحرًا وجوًا)", "الشيكات البنكية",
             "بطاقات العضوية", "جميع أنواع الدمغات", "كروت الهاتف مسبقة الدفع", "جميع أنواع طوابع البريد", "بطاقات الدخول والخروج",
             "بطاقات الهوية", "رخص السلاح", "التذاكر المدفوعة", "بطاقات الائتمان البنكية"]
    hi = {7, 15}
    text(s, X, 3.55, W, 0.3, "أنواع المطبوعات ذات القيمة — 19 نوعًا وفق المحاضرة", size=11, font=F["ar_sb"], color=C["txt2"])
    cols, rh = 4, 0.56; cw = W / cols
    for i, it in enumerate(items):
        r, c = divmod(i, cols)
        x = SW - MX - (c + 1) * cw; y = 3.95 + r * rh
        on = i in hi
        rect(s, x + 0.05, y, cw - 0.1, rh - 0.08, fill=C["org"] if on else C["s1"], alpha=None if on else 0.92, line=None if on else C["line"], lw=0.5, r=0.06)
        text(s, x + 0.12, y, cw - 0.24, rh - 0.08, it, size=11.5, font=F["ar_md"] if on else F["ar"], color=C["ink"] if on else C["txt"], anchor="ctr")
    chrome(s, "ar", 1, 3, TOTAL, "SP1 · pp.3–8")
    notes(s,
        "تطرح المحاضرة سؤالين: ما الفرق بين المستندات ذات القيمة والمستندات المؤمنة؟ وما المطبوعات الآمنة ذات القيمة؟ ثم تعدّد 19 نوعًا من المطبوعات ذات القيمة. محور عرضنا هو «بطاقات تحقيق الشخصية / بطاقات الهوية» (المظللة). صياغة الفرق في الشريحة هي ربطنا لسؤال المحاضرة بمبدأ «سهولة التحقق وصعوبة الاستنساخ» من المحاضرة الثانية.",
        "The lecture asks: what distinguishes valuable documents from secure documents, and what are valuable secure printed documents? It then lists 19 types of valuable printed matter: paper banknotes, polymer currencies, driving licences, birth certificates, 'leadership' certificates, military certificates, death certificates, personal identification cards, transport tickets (land, sea, air), bank cheques, membership cards, all types of stamps, prepaid phone cards, all postage stamps, entry/exit cards, identification cards, weapon licences, paid tickets, bank credit cards. Our focus is the highlighted ID cards. The framing 'value = what the document represents; security = what protects it' links the lecture's question to the 'easy to verify / difficult to reproduce' principle (SP2 p.4). Course aim (SP1 p.3): the concept of security printing, material specifications, securing technologies, and production of currencies, ID cards, stamps, certificates and government papers.",
        "SP1 p.3 (course aim), pp.4–5 (questions), p.6 (types), pp.7–8 (Egyptian certificates, driving licence, ID card; stamps, ticket, cheque). Item names translated from the lecture's list.")
    return s

# ------------------------------------------------------------------ 04 EN easy to verify
def s04(D):
    s = D.new(); bg(s, "bg_quiet.jpg")
    p = img_cover(s, "uv_macro.jpg", 7.35, 0, SW - 7.35, SH, fx=0.35)
    rect(s, 7.35, SH - 1.4, SW - 7.35, 1.4, grad=[(0, C["ink"], 0.0), (100, C["ink"], 0.92)], angle=90)
    rect(s, 7.35, 0, 2.6, SH, grad=[(0, C["ink"], 1.0), (100, C["ink"], 0.0)], angle=0)
    rect(s, 7.35, 0, SW - 7.35, 1.0, grad=[(0, C["ink"], 0.85), (100, C["ink"], 0.0)], angle=90)
    text(s, 9.6, 6.72, 3.13, 0.3, "Security document under UV light · BMI press image", size=8.5, color=C["txt2"], align="r")
    text(s, MX, 0.95, 7.2, 0.3, "THE CORNERSTONE OF DOCUMENT SECURITY", size=11, font=F["disp_md"], color=C["org"], spc=250)
    text(s, MX, 1.32, 7.4, 2.5, ["EASY TO VERIFY.", [("DIFFICULT TO", {"color": C["org"]})], [("REPRODUCE.", {"color": C["org"]})]],
         size=54, font=F["disp"], ls=0.84, caps=True)
    text(s, MX, 3.98, 6.2, 0.75, "Any method of identifying a document must have both properties — the lecture calls them the cornerstone of security and identification.",
         size=14, color=C["txt2"], ls=1.18)
    steps = [("01", "HANDWRITING", "Data entered by hand"), ("02", "ANALOG", "Mechanical copying machines"), ("03", "DIGITAL", "Digital identification & data printing")]
    for i, (n, h, d) in enumerate(steps):
        x = MX + i * 2.15
        line(s, x, 4.85, x + 1.95, 4.85, C["org"] if i == 2 else C["line2"], 1.5)
        text(s, x, 4.97, 1.9, 0.3, n, size=12, font=F["disp_md"], color=C["org"])
        text(s, x, 5.25, 1.95, 0.32, h, size=17, font=F["disp"], spc=80)
        text(s, x, 5.58, 1.95, 0.5, d, size=11, color=C["txt2"], ls=1.05)
    rect(s, MX, 6.12, 6.25, 0.78, fill=C["s1"], line=C["line"], lw=0.5, r=0.08)
    text(s, MX + 0.2, 6.12, 5.9, 0.78, [[("THEN   ", {"font": F["disp_md"], "color": C["org"], "spc": 150}), ("photo fixed with stickers or a metal pin — easy to swap", {})],
                                        [("NOW    ", {"font": F["disp_md"], "color": C["org"], "spc": 150}), ("portrait integrated into the card structure", {})]],
         size=11.5, color=C["txt"], anchor="ctr", ls=1.15)
    chrome(s, "en", 1, 4, TOTAL, "SP2 · p.4")
    notes(s,
        "Identification of official documents evolved from handwriting, to analog methods such as mechanical copying machines, to today's digital identification and data printing. The holder's photograph evolved too: it used to be attached with stickers or a metal pin, which made tampering, changing or replacing the image easy. Every identification method must therefore be easy to verify and difficult to reproduce — the cornerstone of document security.",
        "تطورت طرق تعريف الوثائق الرسمية من الكتابة اليدوية، إلى الطرق التناظرية كآلات النسخ الميكانيكية، ثم إلى التعريف الرقمي وطباعة البيانات رقميًا. وتطورت كذلك طريقة إضافة الصورة الشخصية: كانت تُثبَّت بملصقات أو دبوس معدني مما سهّل العبث بها أو تغييرها أو استبدالها. لذلك يجب أن تتمتع أي طريقة تعريف بخاصيتين هما حجر الأساس: سهولة التحقق وصعوبة الاستنساخ.",
        "SP2 p.4. Image: BMI press photograph of a German security document under UV light (used as illustration only; not one of the compared ID cards).")
    return s

# ------------------------------------------------------------------ 05 AR meet the two cards
def s05(D):
    s = D.new(); bg(s, "bg_center.jpg")
    text(s, MX, 0.72, SW - 2 * MX, 0.6, "تعرّف على البطاقتين", size=30, font=F["ar"], bold=True, align="c")
    line(s, SW / 2, 1.55, SW / 2, 6.75, C["line2"], 0.75)
    # Egypt (right)
    RX, RW = SW / 2 + 0.35, SW / 2 - 0.35 - MX
    text(s, RX, 1.40, RW, 0.55, [[("مصر", {"color": C["org"], "bold": True, "size": 26}), ("   بطاقة تحقيق الشخصية", {"size": 15, "color": C["txt"]})]], align="r")
    img(s, "float_eg_front.png", RX + 0.05, 1.75, 5.1, 5.1 * 860 / 1200)
    sw = RW / 3
    for i, (n, l) in enumerate([("1995", "بداية البطاقات البلاستيكية"), ("7", "سنوات مدة الصلاحية"), ("14", "رقمًا للرقم القومي")]):
        stat(s, SW - MX - (i + 1) * sw + 0.1, 5.0, sw - 0.2, n, l, ar=True, num_size=38, color=C["org"] if i == 1 else C["txt"])
    text(s, RX, 6.45, RW, 0.45, "قطاع الأحوال المدنية · وزارة الداخلية — قانون الأحوال المدنية رقم 143 لسنة 1994", size=10.5, color=C["txt2"], font=F["ar"])
    # Germany (left)
    LX, LW = MX, SW / 2 - 0.35 - MX
    text(s, LX, 1.45, LW, 0.55, [[("ألمانيا", {"color": C["txt"], "bold": True, "size": 26}), ("   Personalausweis", {"size": 15, "color": C["txt2"], "font": F["body"]})]], align="r")
    img(s, "float_de_front.png", LX + 0.05, 1.75, 5.1, 5.1 * 860 / 1200)
    for i, (n, l) in enumerate([("2010", "إطلاق البطاقة ذات الشريحة"), ("10", "سنوات مدة الصلاحية"), ("2024", "التصميم الحالي منذ 2 مايو")]):
        stat(s, LX + LW - (i + 1) * sw + 0.1, 5.0, sw - 0.2, n, l, ar=True, num_size=38, color=C["org"] if i == 1 else C["txt"])
    text(s, LX, 6.45, LW, 0.45, "تنتجها Bundesdruckerei لصالح وزارة الداخلية الاتحادية · 6 سنوات فقط قبل سن 24", size=10.5, color=C["txt2"], font=F["ar"])
    chrome(s, "ar", 1, 5, TOTAL, "SP1 · WIKI-EG · HRW · PAP · PAuswG §6 · BMI 2024")
    notes(s,
        "مصر: «بطاقة تحقيق الشخصية» تصدرها مصلحة/قطاع الأحوال المدنية بوزارة الداخلية بموجب قانون الأحوال المدنية 143 لسنة 1994، وبدأت البطاقات البلاستيكية المميكنة عام 1995، ومدة صلاحيتها 7 سنوات، وتحمل رقمًا قوميًا من 14 رقمًا. ألمانيا: بطاقة Personalausweis ذات الشريحة صدرت أول مرة في 1 نوفمبر 2010، وتنتجها Bundesdruckerei لصالح وزارة الداخلية الاتحادية، وصلاحيتها 10 سنوات (6 سنوات قبل بلوغ 24 عامًا)، والتصميم المعتمد حاليًا يصدر منذ 2 مايو 2024. ملاحظة: معلومات مصر عن القانون والصلاحية مصدرها ثانوي (ويكيبيديا/هيومن رايتس ووتش).",
        "Egypt: the 'Identity Verification Card' is issued by the Civil Status/Civil Registry sector of the Ministry of Interior under Civil Status Law 143 of 1994; computerised plastic cards began in 1995; validity is 7 years; it carries a 14-digit national number. Germany: the chip-based Personalausweis was first issued on 1 November 2010, is produced by Bundesdruckerei for the Federal Ministry of the Interior, is valid for 10 years (6 years before age 24), and the current design has been issued since 2 May 2024. Note: the Egyptian law/validity facts come from secondary sources (Wikipedia, HRW).",
        "WIKI-EG (law 143/1994, 7-year validity, 14 digits); HRW 2007 (plastic cards 1995); PAP (introduced 1 Nov 2010); PAuswG §6 (10 / 6 years); BMI flyer May 2024 (design from 2 May 2024); BDR (manufacturer).")
    return s

# ------------------------------------------------------------------ 06 EN anatomy at a glance
def s06(D):
    s = D.new(); bg(s, "bg_quiet.jpg")
    text(s, MX, 0.72, 7, 0.75, [[("TWO CARDS", {}), (" · FOUR FACES", {"color": C["org"]})]], size=40, font=F["disp"], caps=True)
    text(s, 7.8, 0.82, SW - MX - 7.8, 0.6, "Where each element sits — front and back. Numbers are zones, detailed in chapters 05–06.",
         size=12, color=C["txt2"], align="r", ls=1.1)
    cards = [
        ("EGYPT · FRONT", "eg_front.png", 1.629, MX, 1.55, [(0.16, 0.30, "Portrait"), (0.70, 0.12, "Calligraphic title"), (0.78, 0.48, "Data fields (Arabic)"),
                                                  (0.45, 0.62, "Pyramids & Sphinx background"), (0.20, 0.80, "Multi Laser Image"), (0.25, 0.94, "Factory no. band")]),
        ("EGYPT · BACK", "eg_back.png", 1.633, MX, 4.13, [(0.12, 0.21, "Kinegram (Tutankhamun)"), (0.50, 0.17, "Relief scene / rainbow print"), (0.91, 0.22, "Eagle emblem (UV)"),
                                                  (0.62, 0.42, "Data fields"), (0.50, 0.80, "2D barcode (PDF417)")]),
        ("GERMANY · FRONT", "de_front.png", 1.587, 6.85, 1.55, [(0.22, 0.55, "Colour portrait (inkjet)"), (0.60, 0.48, "Laser-engraved data"), (0.85, 0.06, "Document number"),
                                                  (0.88, 0.80, "CAN (tactile)"), (0.93, 0.30, "Guilloche · federal eagle"), (0.07, 0.10, "EU flag 'DE'")]),
        ("GERMANY · BACK", "de_back.png", 1.583, 6.85, 4.13, [(0.62, 0.10, "Address & data"), (0.34, 0.33, "Variable laser image"), (0.55, 0.64, "Security thread"),
                                                  (0.94, 0.43, "eID logo"), (0.955, 0.86, "Machine-readable zone")]),
    ]
    CW = 3.45
    for title, f, ratio, x, y, zones in cards:
        h = CW / ratio
        text(s, x, y - 0.02, 2.5, 0.25, title, size=10.5, font=F["disp_md"], color=C["org"], spc=180)
        p = img(s, f, x, y + 0.3, CW, h)
        pic_effects(p, shadow=(18, 6, 90, "000000", 0.6))
        lx = x + CW + 0.22
        for k, (fx, fy, lab) in enumerate(zones):
            num_badge(s, x + fx * CW, y + 0.3 + fy * h, k + 1, d=0.22, size=9)
            text(s, lx, y + 0.3 + k * 0.335, 2.25, 0.3, [[(f"{k+1:02d}  ", {"font": F["disp_md"], "color": C["org"]}), (lab, {})]], size=11, color=C["txt"])
    text(s, MX, 6.76, 12.1, 0.25, "Egyptian image: personal fields replaced by field labels by the Wikimedia uploader (CC BY-SA 3.0). German: official specimen 'Erika Mustermann' (BMI / Personalausweisportal; back from BMI flyer, May 2024).",
         size=8.5, color=C["mute"])
    chrome(s, "en", 1, 6, TOTAL, "SP1 · p.19 · BMI 2024 · WM-EG")
    notes(s,
        "An overview of both faces of both cards. Egypt front: portrait, calligraphic title 'Arab Republic of Egypt – Identity Verification Card', Arabic data fields, the Giza pyramids and Sphinx security background, the Multi Laser Image below the portrait, and the factory-number band with microprint. Egypt back: Kinegram with Tutankhamun's head, a pharaonic relief scene printed with rainbow printing, the eagle emblem that glows under UV, data fields (issue/expiry date, profession, gender, religion, marital status) and the encrypted 2D barcode. Germany front: inkjet-integrated colour portrait, laser-engraved data, document number, tactile CAN, guilloches around the federal eagle, EU flag with 'DE'. Germany back: address and data, variable laser image, security thread, eID logo, machine-readable zone.",
        "نظرة عامة على وجهي البطاقتين. الوجه الأمامي المصري: الصورة الشخصية، والعنوان بالخط العربي «جمهورية مصر العربية – بطاقة تحقيق الشخصية»، وحقول البيانات العربية، وخلفية الأهرامات وأبو الهول الأمنية، والصورة الليزرية المتعددة أسفل الصورة، وشريط رقم المصنع بالكتابة الميكرونية. الظهر المصري: الكينجرام برأس توت عنخ آمون، ومشهد فرعوني بالطباعة التدريجية، والنسر الذي يتألق تحت الأشعة فوق البنفسجية، وحقول البيانات (تاريخ الإصدار والانتهاء، المهنة، النوع، الديانة، الحالة الاجتماعية)، والباركود ثنائي الأبعاد المشفر. الوجه الألماني: صورة ملونة مدمجة بالحبر النفاث، وبيانات محفورة بالليزر، ورقم الوثيقة، ورقم CAN البارز، وزخارف جيلوشية حول النسر الاتحادي، وعلم الاتحاد الأوروبي مع «DE». الظهر الألماني: العنوان والبيانات، وصورة الليزر المتغيرة، وخيط الأمان، وشعار eID، ومنطقة القراءة الآلية.",
        "SP1 p.19 (labelled map of the Egyptian card); BMI flyer May 2024 (German features); WM-EG image (field labels by uploader).")
    return s

SLIDES = [s01, s02, s03, s04, s05, s06]
