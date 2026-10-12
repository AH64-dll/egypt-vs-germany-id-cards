"""Slides 7–13: chapter 02 (materials) and 03 (layers & construction)."""
from common import *

# ------------------------------------------------------------------ 07 AR ISO formats (chapter 02 opener)
def s07(D):
    s = D.new(); bg(s, "bg_opener_l.jpg")
    opener_numeral(s, 2)
    text(s, MX, 4.15, 4.0, 0.4, "الخامات وجسم البطاقة", size=20, font=F["ar"], bold=True, align="l", rtl=True)
    text(s, MX, 4.62, 3.95, 1.4, "جسم البطاقة هو القاعدة الأولى في بنية أي مستند مؤمَّن، ويبدأ تعريفه بالمقاس الذي يحدده معيار ISO.",
         size=13, font=F["ar_lt"], color=C["txt"], ls=1.25, align="l", rtl=True)
    X, W = 5.1, SW - MX - 5.1
    title_ar(s, "المقاس: معيار ISO/IEC 7810", w=W, size=32)
    sub(s, "البطاقات الرقمية ليست بطاقات الهوية وحدها، بل كل ما له شكل البطاقة بأبعاد محددة في معايير الجودة الدولية ISO.", X, 1.55, W, 0.75)
    rows = [["النوع", "الأبعاد الاسمية (مم)", "العرض (مم)", "الارتفاع (مم)", "السُّمك (مم)"],
            ["ID-0 *", "25 × 15", "24.90 – 25.10", "14.90 – 15.10", "0.68 – 0.84"],
            [("ID-1", {"color": C["org"]}), "85.60 × 53.98", "85.47 – 85.90", "53.92 – 54.18", "0.68 – 0.84"],
            ["ID-2", "105 × 74", "104.80 – 105.30", ("74.70 – 74.30 **", {"color": C["peach"]}), "0.68 – 0.84"],
            ["ID-3", "125 × 88", "124.80 – 125.30", "87.70 – 88.30", "0.68 – 0.84"]]
    table(s, X, 2.35, W, [1.25, 1.55, 1.65, 1.65, 1.53], rows, rtl=True, row_h=0.42, size=11.5, header_size=10.5,
          fills=lambda r, c: C["s1"] if r == 0 else None)
    text(s, X, 4.55, W, 0.55, "* يسمّيه المعيار ID-000 (مقاس شريحة الهاتف).   ** الحد الأدنى في جدول المحاضرة أكبر من الأقصى؛ الارتفاع الاسمي 74 مم والأرجح أن المقصود 73.70.",
         size=9.5, color=C["txt2"], font=F["ar"], ls=1.15)
    # to-scale outlines (bottom-left aligned)
    k = 0.0172; bx, by = X, 6.85
    for nm, wmm, hmm, col, fa in [("ID-3", 125, 88, C["line2"], None), ("ID-2", 105, 74, C["mute"], None), ("ID-1", 85.6, 53.98, C["org"], 0.22), ("ID-000", 25, 15, C["txt2"], None)]:
        w, h = wmm * k, hmm * k
        rect(s, bx, by - h, w, h, fill=C["org"] if fa else None, alpha=fa, line=col, lw=1.25 if nm == "ID-1" else 0.75, r=0.05 if nm != "ID-000" else 0.02)
        text(s, bx + w - 0.75, by - h + 0.03, 0.7, 0.22, nm, size=9.5 if nm != "ID-000" else 7, font=F["disp_md"], color=col if nm != "ID-1" else C["peach"], rtl=False, align="r")
    text(s, bx + 0.55, by - 53.98 * k / 2 - 0.12, 0.9, 0.25, "البطاقتان", size=10, font=F["ar_sb"], color=C["txt"], align="c")
    text(s, bx, 5.18, 125 * k, 0.25, "رسم بمقياس حقيقي للأبعاد الاسمية", size=9, color=C["mute"], font=F["ar"], align="l")
    NX = X + 125 * k + 0.35; NW = SW - MX - NX
    rect(s, NX, 5.45, NW, 1.4, fill=C["s1"], line=C["line"], lw=0.5, r=0.08)
    text(s, NX + 0.2, 5.45, NW - 0.4, 1.4, [[("ألمانيا: ", {"font": F["ar_sb"], "color": C["txt"]}), ("مقاس ID-1 رسميًا (8.6 × 5.4 سم).", {})],
                                           [("مصر: ", {"font": F["ar_sb"], "color": C["org"]}), ("تظهر البطاقة بالنسبة نفسها تقريبًا (1.6 : 1)، ولا تنشر الجهة المصدرة مواصفة رسمية لمقاسها.", {})]],
         size=12, color=C["txt2"], anchor="ctr", ls=1.25, after=4)
    chrome(s, "ar", 2, 7, TOTAL, "SP2 · pp.18–19 · ISO/IEC 7810 · PAP")
    notes(s,
        "تقول المحاضرة إن البطاقات الرقمية ليست بطاقات الهوية فقط، بل أي شيء على شكل بطاقة بأبعاد يحددها معيار ISO، وتعرض جدول الأبعاد لأنواع ID-0 وID-1 وID-2 وID-3 (العرض والارتفاع والسمك بحد أدنى وأقصى). عرضنا قيم المحاضرة كما هي، وأضفنا الأبعاد الاسمية من ISO/IEC 7810، مع ملاحظة أن الحد الأدنى لارتفاع ID-2 (74.70) أكبر من الحد الأقصى (74.30) في المحاضرة، والأرجح أنه 73.70. النوع الأصغر يسميه المعيار ID-000 (مقاس شريحة الهاتف). البطاقة الألمانية بمقاس ID-1 رسميًا (8.6 × 5.4 سم)، أما المصرية فنسبتها في الصور قرابة 1.6:1 دون مواصفة رسمية منشورة.",
        "The lecture states that digital cards are not only ID cards but anything card-shaped with dimensions specified by ISO, and gives a table for ID-0, ID-1, ID-2 and ID-3 (min/max width, height and thickness 0.68–0.84 mm). We show the lecture values unchanged and add the ISO/IEC 7810 nominal sizes (ID-1 85.60 × 53.98 mm; ID-2 105 × 74; ID-3 125 × 88; the smallest is called ID-000 in the standard). Note: the lecture's ID-2 minimum height (74.70) exceeds its maximum (74.30) — likely 73.70. Germany: ID-1, 8.6 × 5.4 cm (official portal). Egypt: the card appears in the same ~1.6:1 proportion, but no official size specification is published.",
        "SP2 p.18 (card personalization / ISO), p.19 (dimension table); ISO/IEC 7810 nominal dimensions; PAP (8.6 × 5.4 cm).")
    return s

# ------------------------------------------------------------------ 08 EN material families
def slab_icon(s, x, y, n, w=1.0):
    for i in range(n):
        yy = y + (n - 1 - i) * 0.16
        c = [C["org"], C["org2"], C["deep"]][i % 3]
        rect(s, x + i * 0.08, yy, w, 0.13, grad=[(0, c, 1), (100, C["deep"], 1)], angle=0, r=0.04)

def s08(D):
    s = D.new(); bg(s, "bg_glow_br.jpg")
    title_en(s, [("FROM SECURE PAPER", False)], y=0.82, w=4.6, size=40)
    title_en(s, [("TO ENGINEERED", True)], y=1.42, w=4.6, size=40)
    title_en(s, [("POLYMER", True)], y=2.02, w=4.6, size=40)
    sub(s, "From the 1970s, plastics took the lead in secure documents — more secure, reliable and durable than paper. Accumulated experience then put them first for digital cards.",
        MX, 2.85, 4.1, 1.4, size=13.5)
    # mini timeline
    tl = [("ORIGIN", "Secure paper"), ("1970s", "Plastics take over"), ("TODAY", "PVC · polyester · composites · polycarbonate")]
    for i, (a, b) in enumerate(tl):
        y = 4.5 + i * 0.68
        dot(s, MX + 0.06, y + 0.13, 0.12, fill=C["org"] if i else C["mute"])
        if i < 2: line(s, MX + 0.06, y + 0.22, MX + 0.06, y + 0.72, C["line2"], 1)
        text(s, MX + 0.3, y, 1.0, 0.3, a, size=13, font=F["disp"], color=C["org"] if i else C["txt2"], spc=100)
        text(s, MX + 1.2, y + 0.02, 3.0, 0.5, b, size=12, color=C["txt"])
    cols = [
        ("PVC", "POLYVINYL CHLORIDE", 1, "3–5", "YEARS EXPECTED LIFE",
         [("Cost", "the least expensive card plastic"), ("Uses", "telecom & contactless cards"), ("Weak", "lower resistance to heat, load, bending, UV"),
          ("Fails by", "layer separation, partial damage, surface erosion")]),
        ("POLYESTER", "MODIFIED · PETG · PETF", 2, "↑", "DURABILITY OF THE CARD BODY",
         [("Why", "modified to reach higher card specifications"), ("Gains", "resists bending & warping"), ("Heat", "withstands high temperatures"),
          ("Chemistry", "excellent solvent resistance")]),
        ("COMPOSITE", "MULTI-MATERIAL BUILD", 3, "2+", "MATERIALS IN ONE CONFIGURATION",
         [("Idea", "more than one material in a single build"), ("Gains", "properties no single material reaches"), ("Balance", "competitive quality and affordability")]),
    ]
    cw, gap, x0, y0 = 2.5, 0.17, 5.05, 0.85
    for i, (nm, subn, n, big, bigl, rows) in enumerate(cols):
        x = x0 + i * (cw + gap)
        rect(s, x, y0, cw, 5.85, fill=C["s1"], alpha=0.85, line=C["line"], lw=0.5, r=0.1)
        slab_icon(s, x + 0.25, y0 + 0.3, n, 1.1)
        text(s, x + 0.25, y0 + 0.95, cw - 0.4, 0.5, nm, size=26, font=F["disp"])
        text(s, x + 0.25, y0 + 1.42, cw - 0.4, 0.3, subn, size=10, font=F["disp_md"], color=C["org"], spc=150)
        yy = y0 + 1.9
        for k, b in rows:
            line(s, x + 0.25, yy, x + cw - 0.25, yy, C["line"], 0.5)
            text(s, x + 0.25, yy + 0.06, cw - 0.5, 0.75, [[(k.upper() + "  ", {"font": F["disp_md"], "color": C["txt2"], "spc": 120, "size": 9.5}), (b, {})]], size=11.5, ls=1.08)
            yy += 0.72
        text(s, x + 0.25, y0 + 4.7, cw - 0.4, 0.75, big, size=46, font=F["disp_lt"], color=C["org"])
        text(s, x + 0.25, y0 + 5.4, cw - 0.4, 0.4, bigl, size=9, font=F["disp_md"], color=C["txt2"], spc=120)
    text(s, 5.05, 6.76, 7.7, 0.2, "Polycarbonate — the German card body — is analysed on the next slide.", size=9.5, color=C["mute"], align="r")
    chrome(s, "en", 2, 8, TOTAL, "SP2 · pp.20, 23–26")
    notes(s,
        "Card materials evolved from secure paper. From the 1970s plastics took a significant position in secure documents because they are more secure, reliable and durable than paper; accumulated experience put them in the lead for digital cards. The main families in the lecture: PVC — the cheapest card plastic, widely used for telecom and contactless cards, but with lower resistance to heat, loads, bending and UV, which causes premature deterioration through layer separation, partial damage or surface erosion; expected life 3–5 years, shorter than ID cards and licences. Polyester — improved and modified (PETG, PETF) to reduce weaknesses, improve the physical durability of the card body and its resistance to bending and warping; they withstand high temperatures and have excellent solvent resistance. Composite materials — more than one material in one configuration, achieving properties no single material can, with competitive quality and affordability.",
        "تطورت خامات البطاقات بدءًا من الورق المؤمَّن، ومنذ السبعينيات احتلت المواد البلاستيكية مكانة كبيرة لأنها أكثر أمانًا وموثوقية ومتانة من الورق. أهم العائلات في المحاضرة: PVC — الأرخص، ويُستخدم في بطاقات الاتصالات والبطاقات اللاتلامسية، لكنه أقل مقاومة للحرارة والأحمال والثني والأشعة فوق البنفسجية، فيتلف مبكرًا بانفصال الطبقات أو التلف الجزئي أو تآكل السطح، وعمره المتوقع 3–5 سنوات. البوليستر — طُوِّر وعُدِّل (PETG وPETF) لتقليل نقاط الضعف وتحسين المتانة ومقاومة الثني والالتواء، ويتحمل الحرارة العالية ومقاومته للمذيبات ممتازة. المواد المركبة — أكثر من خامة في تكوين واحد لتحقيق خصائص لا تحققها خامة منفردة، بجودة وتكلفة تنافسية.",
        "SP2 p.20 (materials history), p.23 (main materials), p.24 (PVC), p.25 (polyester PETG/PETF), p.26 (composites).")
    return s

# ------------------------------------------------------------------ 09 AR polycarbonate
def s09(D):
    s = D.new(); bg(s, "bg_glow_bl.jpg")
    # macro composition (left)
    frame_pic(s, "de_m_laser_text.png", MX, 1.0, 4.3, 2.15, r=0.12)
    frame_pic(s, "de_m_tactile_2034.png", MX, 3.3, 2.08, 1.08, r=0.1)
    frame_pic(s, "de_m_identigram_d.png", MX + 2.22, 3.3, 2.08, 1.08, fy=0.3, r=0.1)
    text(s, MX, 4.45, 4.3, 0.5, "تفاصيل مكبّرة من البطاقة الألمانية (BMI): حفر ليزري داخل الخامة، كتابة بارزة، عنصر هولوجرافي.",
         size=9.5, color=C["mute"], font=F["ar"], align="l", ls=1.1)
    # verdict chips
    rect(s, MX, 5.05, 4.3, 0.85, fill=C["s1"], line=C["txt"], lw=0.75, r=0.08)
    text(s, MX + 0.15, 5.05, 4.0, 0.85, [[("ألمانيا  ", {"font": F["ar_sb"], "color": C["txt"]}), ("بولي كربونات (Bundesdruckerei) — طبقات بلاستيكية متعددة وطلاء حماية سطحي (البوابة الرسمية)", {})]],
         size=11, color=C["txt2"], anchor="ctr", ls=1.15)
    rect(s, MX, 6.0, 4.3, 0.85, fill=C["s1"], line=C["org"], lw=0.75, r=0.08)
    text(s, MX + 0.15, 6.0, 4.0, 0.85, [[("مصر  ", {"font": F["ar_sb"], "color": C["org"]}), ("بطاقة بلاستيكية منذ 1995 — نوع البوليمر غير منشور رسميًا ولا تحدده المحاضرة", {})]],
         size=11, color=C["txt2"], anchor="ctr", ls=1.15)
    # right text
    X, W = 5.4, SW - MX - 5.4
    label(s, X, 0.9, W, "خامة جسم البطاقة", align="r")
    title_ar(s, "البولي كربونات Polycarbonate", y=1.2, w=W, size=34)
    text(s, X, 2.05, W, 0.3, "من المحاضرة", size=11, font=F["ar_sb"], color=C["org"])
    bullet_rows(s, X, 2.4, W, [("طباعة متعددة", "يقبل الطباعة بطرق متعددة."),
                               ("رقائق متغيرة بصريًا", "يمكن إضافة الهولوجرام والكينجرام إليه لتأمين البطاقة بشكل شامل."),
                               ("العيب الرئيسي", "يميل إلى الهشاشة مع كثرة الاستخدام، وسطحه عرضة للتشقق مما قد يؤدي إلى كسر جسم البطاقة."),
                               ("ليس وحيدًا", "تُستخدم خامات بلاستيكية أخرى كثيرة لأنواع مختلفة من البطاقات.")], ar=True, row_h=0.56, gap=0.04, size=12.5)
    text(s, X, 5.0, W, 0.3, "من البحث (ممارسة صناعية عامة)", size=11, font=F["ar_sb"], color=C["txt2"])
    text(s, X, 5.35, W, 1.5, "تُدمج رقائق البولي كربونات بالحرارة والضغط دون لاصق فتصبح كتلة واحدة لا يمكن فصل طبقاتها دون تدمير البطاقة، ويُسوِّد شعاع الليزر الخامة من الداخل ليكتب البيانات فيها لا عليها.",
         size=12.5, font=F["ar_lt"], color=C["txt"], ls=1.25)
    chrome(s, "ar", 2, 9, TOTAL, "SP2 · p.21 · BDR · PAP · COV · ENG")
    notes(s,
        "من المحاضرة: البولي كربونات يقبل الطباعة بطرق متعددة، ويمكن إضافة رقائق متغيرة بصريًا كالهولوجرام والكينجرام إليه، مما يساعد على تأمين البطاقات بشكل شامل. من أهم عيوبه ميله للهشاشة مع كثرة الاستخدام، وسطحه عرضة للتشقق والتلف مما قد يؤدي لكسر جسم البطاقة. ولا يعني ذلك أنه الخامة الوحيدة. ملاحظة: الشريحة التي تقدّم البولي كربونات في المحاضرة غير موجودة (تبدأ صفحة 21 بكلمة «أيضًا»). من البحث: تصف Bundesdruckerei بطاقات الهوية الإلكترونية بأنها مصنوعة من البولي كربونات، وتذكر البوابة الرسمية أن البطاقة من عدة طبقات بلاستيكية مع طلاء حماية. وفي الممارسة الصناعية العامة تُدمج رقائق PC بالحرارة والضغط دون لاصق، ويكتب الليزر البيانات داخل الخامة. أما البطاقة المصرية فلم نجد مصدرًا رسميًا يحدد نوع البوليمر.",
        "Lecture: polycarbonate accepts printing in multiple ways and optically variable laminates such as holograms or Kinegrams can be added, securing cards comprehensively. A major drawback is its tendency to become brittle with frequent use; its surface is susceptible to cracking and damage, which can lead to card-body breakage. It is not the only card material. Note: the lecture slide that introduces polycarbonate is missing (p.21 begins 'Polycarbonate also…'). Research: Bundesdruckerei describes eID cards as made of polycarbonate; the official portal says the card consists of several plastic layers with a protective lacquer. General industry practice: PC films are fused under heat and pressure without adhesive into a monolithic body, and lasers blacken the material inside the card. No official source specifies the Egyptian card's polymer.",
        "SP2 p.21; BDR (eID cards made of polycarbonate); PAP (several plastic layers, protective lacquer); COV, ENG (lamination & laser engraving — industry-general); HRW (Egyptian plastic cards 1995). Images: BMI flyer May 2024.")
    return s

# ------------------------------------------------------------------ 10 EN document structure (chapter 03 opener)
def s10(D):
    s = D.new(); bg(s, "bg_opener_r.jpg")
    text(s, SW - 4.95, 0.5, 4.6, 2.95, "03", size=170, font=F["disp_lt"], color=C["txt"], rtl=False, align="r")
    label(s, MX, 0.95, 6, "CHAPTER 03 · LAYERS & CONSTRUCTION")
    title_en(s, [("A SECURE DOCUMENT", False)], y=1.3, w=7.5, size=46)
    title_en(s, [("IS A STACK", True)], y=1.95, w=7.5, size=46)
    sub(s, "Imagine any secured document as layers stacked in the chronological order of its life cycle. The figure gives a simple overview of its composition and production stages.",
        MX, 2.75, 6.2, 1.0, size=13.5)
    bars = [("01", "CARD BODY", "Primary material — paper or polymer — carrying the security made with the substrate."),
            ("02", "PRINT", "Security design printed onto the substrate: backgrounds, fine lines, special inks."),
            ("03", "PERSONALIZE", "Holder data and image added by digital methods."),
            ("04", "FINISHING", "Optional transparent panels or visually variable markings over the data.")]
    for i, (n, nm, d) in enumerate(reversed(bars)):
        idx = 3 - i
        y = 3.95 + i * 0.73; indent = i * 0.32
        w = 7.6 - indent * 0
        rect(s, MX + (3 - idx) * 0.0, y, 0.08, 0.58, fill=C["org"] if idx == 3 else C["org2"] if idx == 2 else C["deep"] if idx == 1 else C["line2"])
        rect(s, MX + 0.14, y, 7.2 - idx * 0.55, 0.58, fill=C["s1"], alpha=0.9, line=C["line"], lw=0.5, r=0.06)
        text(s, MX + 0.3, y, 0.5, 0.58, n, size=14, font=F["disp_md"], color=C["org"], anchor="ctr")
        text(s, MX + 0.85, y, 1.75, 0.58, nm, size=16, font=F["disp"], anchor="ctr", spc=80)
        text(s, MX + 2.65, y, 4.6 - idx * 0.55, 0.58, d, size=11, color=C["txt2"], anchor="ctr", ls=1.05)
    PW = 4.3; PH = PW * 1100 / 1200
    img(s, "pyramid_top.png", 8.55, 2.95, PW, PH)
    text(s, 8.4, 6.75, 4.33, 0.25, "Life-cycle order: card body first, finishing last.", size=9.5, color=C["txt2"], align="r")
    chrome(s, "en", 3, 10, TOTAL, "SP2 · pp.5–8")
    notes(s,
        "The lecture's document structure: if we imagine the structural composition of any secured document as several layers stacked on top of each other according to the chronological order of its life cycle, we get a simple overview of its composition and production stages: (1) card body — the primary material, natural (paper) or synthetic (polymers), containing the essential security elements produced while making the secure paper or polymer; (2) print; (3) personalize; (4) finishing — sometimes unnecessary; transparent panels, or transparent panels with visually variable markings such as transparent holograms.",
        "بنية المستند في المحاضرة: إذا تخيلنا التكوين البنائي لأي مستند مؤمَّن كطبقات متراكبة وفق الترتيب الزمني لدورة حياته، نحصل على صورة مبسطة لتكوينه ومراحل إنتاجه: (1) جسم المستند — الخامة الأساسية طبيعية (ورق) أو صناعية (بوليمرات) وتحمل عناصر التأمين الناتجة عن تصنيع الورق أو البوليمر المؤمَّن؛ (2) الطباعة؛ (3) التشخيص؛ (4) التشطيب — قد لا يكون ضروريًا أحيانًا، ويتكون من ألواح شفافة أو ألواح بعلامات متغيرة بصريًا كالهولوجرام الشفاف.",
        "SP2 p.5 (pyramid: Card Body, Print, Personalize, Finishing), p.6 & p.8 (life-cycle stacking), p.7 (first layer), p.11 (fourth layer).")
    return s

# ------------------------------------------------------------------ 11 AR exploded generic card
def s11(D):
    s = D.new(); bg(s, "bg_glow_bl.jpg")
    IX, IY, IW = 0.35, 0.75, 6.35; IH = IW * 1250 / 1300
    img(s, "exploded.png", IX, IY, IW, IH)
    X, W = 7.55, SW - MX - 7.55
    title_ar(s, "تشريح بطاقة ذكية", y=0.8, w=W + 1.0, size=34)
    sub(s, "مثال عام من المحاضرة لطبقات البطاقة — لا يمثل أيًّا من البطاقتين.", X - 1.0, 1.55, W + 1.0, 0.4, size=13)
    labels = {  # kind -> (title, desc)
        "overlay": ("طبقة الحماية العلوية", "Overlay شفافة أو هولوجرافية"),
        "perso": ("طبقة التشخيص", "بيانات الحامل وصورته · طباعة ملونة 300 DPI"),
        "clear": ("طبقة شفافة", "طبقة PVC شفافة (Clear PVC)"),
        "core": ("القلب المطبوع", "PET بطباعة ليثوغرافية ورقمية وعناصر ضد التزييف"),
        "prelam": ("الطبقة الداخلية Prelam", "هوائي وشريحة لاتلامسية · MIFARE · iCLASS · Prox"),
        "back": ("الوجه الخلفي", "شريط مغناطيسي · باركود · رمز QR"),
    }
    anchors = ANCH["exploded"]
    ys = {}
    for i, a in enumerate(anchors):
        ax, ay = IX + a["right"][0] * IW, IY + a["right"][1] * IH
        ys[a["kind"]] = (ax, ay)
    order = ["overlay", "perso", "clear", "core", "prelam", "back"]
    for j, kind in enumerate(order):
        ax, ay = ys[kind]
        ly = 2.25 + j * 0.76
        line(s, ax + 0.05, ay, X - 0.75, ly + 0.2, C["org"], 0.75, alpha=0.75); dot(s, ax + 0.05, ay, 0.07)
        line(s, X - 0.75, ly + 0.2, X - 0.15, ly + 0.2, C["org"], 0.75, alpha=0.75)
        t, d = labels[kind]
        text(s, X - 0.1, ly - 0.02, W + 0.1, 0.35, t, size=14, font=F["ar_sb"], color=C["txt"], align="l")
        text(s, X - 0.1, ly + 0.3, W + 0.1, 0.35, d, size=11, font=F["ar"], color=C["txt2"], align="l")
    text(s, X - 1.0, 6.8, W + 1.0, 0.25, "رسم توضيحي أصلي مبني على أشكال المحاضرة (SP2 ص 6، 9، 10)", size=9, color=C["mute"], font=F["ar"])
    chrome(s, "ar", 3, 11, TOTAL, "SP2 · pp.6, 9, 10")
    notes(s,
        "تعرض المحاضرة عدة أشكال لتشريح البطاقة: حماية علوية (Overlay) شفافة أو هولوجرافية، وطبقة بيانات الحامل والرسوم المتغيرة المطبوعة بتقنية عالية الدقة (HDP)، وطبقة PVC شفافة، وطبقة PET تحمل طباعة ليثوغرافية ورقمية وعناصر مضادة للتزييف مدمجة، وطبقة داخلية (Prelam) تحتوي التقنية اللاتلامسية (iCLASS وProx وMIFARE وLegic)، إضافة إلى شريحة ذكية، وترميز بيانات، وصور شخصية بالأشعة فوق البنفسجية، وطباعة ملونة بدقة 300 نقطة/بوصة، وشريط مغناطيسي، وباركود ورمز QR، وطباعة أحادية اللون. هذا الرسم مثال عام وليس تمثيلًا لبطاقة مصر أو ألمانيا.",
        "The lecture shows several card anatomies: an overlaminate (clear or holographic); a film carrying cardholder data and variable graphics printed with high-definition printing (HDP); a clear PVC layer; a PET layer with lithographic and digital printing and embedded anti-counterfeiting; a prelam with contactless technology (iCLASS, Prox, MIFARE, Legic). Other labelled elements: smart/IC chip, data encoding, overlay protection, personalised UV images, holographic lamination, vivid 300 dpi colour printing, PVC card, proximity/MIFARE card, magnetic stripe, barcode, QR code and mono-printing. This drawing is a generic example — not the Egyptian or German card.",
        "SP2 p.6 (layer diagram with chip, overlay, UV images, holographic lamination, 300 DPI, PVC, MIFARE, barcode, QR, magnetic stripe, mono-printing), p.9 (Anatomy of a card), p.10 (front/material/chip/material/back). Original illustration.")
    return s

# ------------------------------------------------------------------ 12 EN base layer & fourth layer
def s12(D):
    s = D.new(); bg(s, "bg_quiet.jpg")
    title_en(s, [("SECURITY LIVES ", False), ("IN THE LAYERS", True)], y=0.78, w=11, size=40)
    sub(s, "Layer 1 brings security from the substrate itself; the optional layer 4 adds transparent, optically variable protection on top.", MX, 1.45, 10.5, 0.5, size=13.5)
    # left column: layer 1
    LX, LW = MX, 5.85
    label(s, LX, 2.15, LW, "LAYER 1 · THE SUBSTRATE")
    text(s, LX, 2.45, LW, 0.95, "The primary material — paper or polymer — already contains essential security elements made during its manufacture: watermarks, warranty strips and fluorescent fibres.",
         size=12.5, color=C["txt"], ls=1.15)
    frame_pic(s, "de_m_thread_muster.png", LX, 3.5, 2.85, 1.45, r=0.1)
    frame_pic(s, "de_m_uv_fibres.png", LX + 3.0, 3.5, 2.85, 1.45, fy=0.45, r=0.1)
    text(s, LX, 5.0, 2.85, 0.65, [[("DE  ", {"font": F["disp_md"], "color": C["txt"]}), ("machine-verifiable security thread, personalised with document no. & name", {})]], size=10, color=C["txt2"], ls=1.05)
    text(s, LX + 3.0, 5.0, 2.85, 0.65, [[("DE  ", {"font": F["disp_md"], "color": C["txt"]}), ("transparent security fibres, luminescent under UV", {})]], size=10, color=C["txt2"], ls=1.05)
    rect(s, LX, 5.85, LW, 0.85, fill=C["s1"], line=C["org"], lw=0.75, r=0.08)
    text(s, LX + 0.18, 5.85, LW - 0.36, 0.85, [[("EG  ", {"font": F["disp_md"], "color": C["org"]}), ("Lab-tested marks 'related to the nature of the materials used in printing and manufacturing the card' — no public detail.", {})]],
         size=10.5, color=C["txt2"], anchor="ctr", ls=1.1)
    line(s, SW / 2 + 0.02, 2.2, SW / 2 + 0.02, 6.75, C["line2"], 0.75)
    # right column: layer 4
    RX, RW = SW / 2 + 0.3, SW - MX - SW / 2 - 0.3
    label(s, RX, 2.15, RW, "LAYER 4 · TRANSPARENT PANELS")
    text(s, RX, 2.45, RW, 0.95, "Sometimes unnecessary: clear panels, or panels with visually variable markings such as transparent holograms — local or full-surface — protecting data from tampering, much like lamination.",
         size=12.5, color=C["txt"], ls=1.15)
    frame_pic(s, "eg_m_kinegram.png", RX, 3.5, 1.9, 1.45, fy=0.4, r=0.1)
    frame_pic(s, "de_m_identigram_d.png", RX + 2.03, 3.5, 1.9, 1.45, fy=0.25, r=0.1)
    frame_pic(s, "de_m_identigram_blue.png", RX + 4.06, 3.5, 1.9, 1.45, fy=0.35, r=0.1)
    text(s, RX, 5.0, 1.9, 0.7, [[("EG  ", {"font": F["disp_md"], "color": C["org"]}), ("local Kinegram patch (Tutankhamun)", {})]], size=10, color=C["txt2"], ls=1.05)
    text(s, RX + 2.03, 5.0, 3.93, 0.7, [[("DE  ", {"font": F["disp_md"], "color": C["txt"]}), ("Identigram®: green holographic portrait, red 3D eagle, blue elements at 90°", {})]], size=10, color=C["txt2"], ls=1.05)
    rect(s, RX, 5.85, RW, 0.85, fill=C["s1"], line=C["txt"], lw=0.75, r=0.08)
    text(s, RX + 0.18, 5.85, RW - 0.36, 0.85, [[("FULL SURFACE  ", {"font": F["disp_md"], "color": C["txt"], "spc": 100}), ("German card: protective lacquer over the whole surface prevents damage in normal use (official portal).", {})]],
         size=10.5, color=C["txt2"], anchor="ctr", ls=1.1)
    chrome(s, "en", 3, 12, TOTAL, "SP2 · pp.7, 11 · SP1 · p.16 · BMI 2024 · PAP")
    notes(s,
        "Layer 1: the first layer, the basic foundation of the document, is the primary material — natural (paper) or synthetic (polymers) — and contains the essential security elements produced in manufacturing secured paper or polymers, such as watermarks, warranty strips and fluorescent fibres. Germany: a machine-verifiable security thread personalised with the document number and name, and transparent security fibres luminescent under UV (BMI #10, #11). Egypt: the lecture lists laboratory-tested marks related to the nature of the materials used in printing and manufacturing the card, without public detail. Layer 4: sometimes unnecessary; transparent panels, or panels with visually variable markings such as transparent holograms, either specific in location and dimension or covering the entire surface, used to increase security and protect data from tampering — similar to lamination. Egypt: a local Kinegram patch with Tutankhamun's head on the back. Germany: the Identigram (kinematic structures, green holographic portrait, red 3D eagle, blue elements after a 90° turn) and a protective lacquer on the whole surface.",
        "الطبقة الأولى: هي الأساس، أي الخامة الأولية الطبيعية (الورق) أو الصناعية (البوليمرات)، وتحتوي عناصر التأمين الناتجة عن مراحل تصنيع الورق أو البوليمر المؤمَّن كالعلامات المائية وشرائط الضمان والألياف الفلورية. ألمانيا: خيط أمان قابل للفحص آليًا مُشخَّص برقم الوثيقة والاسم، وألياف أمان شفافة تتألق تحت الأشعة فوق البنفسجية. مصر: تذكر المحاضرة علامات مرتبطة بطبيعة خامات الطباعة والتصنيع تُفحص معمليًا دون تفاصيل منشورة. الطبقة الرابعة: قد تكون غير ضرورية، وهي ألواح شفافة أو بعلامات متغيرة بصريًا كالهولوجرام الشفاف، محددة الموقع والأبعاد أو تغطي السطح كاملًا، لزيادة التأمين وحماية البيانات من العبث — تشبه التغليف. مصر: كينجرام موضعي برأس توت عنخ آمون. ألمانيا: Identigram وطلاء حماية على السطح كله.",
        "SP2 p.7 (first layer), p.11 (fourth layer); SP1 p.16 (lab-tested material marks); BMI flyer May 2024 #3, #10, #11; PAP (protective lacquer). Images: BMI flyer; Wikimedia (Kinegram).")
    return s

# ------------------------------------------------------------------ 13 AR what sits in each layer
def s13(D):
    s = D.new(); bg(s, "bg_center.jpg")
    title_ar(s, "ماذا تحمل كل طبقة؟ مصر مقابل ألمانيا", w=10, size=32)
    sub(s, "توزيع العناصر الموثقة لكل بطاقة على طبقات نموذج المحاضرة الأربع.", SW - MX - 10, 1.5, 10, 0.4, size=13)
    hdr_y = 2.05
    cols = {"layer": (SW - MX - 2.45, 2.45), "eg": (SW - MX - 2.45 - 0.15 - 4.6, 4.6), "de": (MX, 4.95)}
    text(s, cols["eg"][0], hdr_y, cols["eg"][1], 0.3, "مصر", size=13, font=F["ar_sb"], color=C["org"])
    text(s, cols["de"][0], hdr_y, cols["de"][1], 0.3, "ألمانيا", size=13, font=F["ar_sb"], color=C["txt"])
    rows = [
        ("04", "التشطيب", "كينجرام موضعي برأس توت عنخ آمون على ظهر البطاقة.",
         "Identigram® (صورة هولوجرافية ونسر ثلاثي الأبعاد) · طلاء حماية سطحي · بروز سطحي محسوس بالخلف."),
        ("03", "التشخيص", "الصورة والبيانات العربية · الصورة الليزرية المتعددة MLI · رقم المصنع · باركود ثنائي الأبعاد مشفر.",
         "صورة ملونة ورقم الوثيقة بالحبر النفاث داخل الخامة · بيانات بالحفر الليزري · تاريخ الانتهاء وCAN بارزان · صورة ليزر متغيرة · بيانات الشريحة."),
        ("02", "الطباعة", "طباعة تدريجية (Rainbow) · جلوشيات · كتابة ميكرونية ظاهرة وخفية · أحبار UV · طباعة Relief «مصر».",
         "جلوشيات متعددة الألوان · كتابة ميكرونية موجبة وسالبة · طباعة قزحية بأحبار UV · حبر متغير بصريًا OVI."),
        ("01", "جسم البطاقة", "بطاقة بلاستيكية (منذ 1995) — نوع البوليمر غير منشور · علامات خامات تُفحص معمليًا.",
         "بولي كربونات متعدد الطبقات · خيط أمان مُشخَّص · ألياف أمان UV · شريحة وهوائي مدمجان."),
    ]
    y = 2.45; rh = 1.0
    for i, (n, nm, eg, de) in enumerate(rows):
        yy = y + i * (rh + 0.08)
        hot = [C["org"], C["org2"], C["deep"], "4A1A0C"][i]
        lx, lw = cols["layer"]
        rect(s, lx, yy, lw, rh, grad=[(0, hot, 1), (100, C["deep"] if i < 3 else "2A0F07", 1)], angle=0, r=0.08)
        text(s, lx + 0.15, yy, lw - 0.3, rh, [[(n + "  ", {"font": F["disp_md"], "color": C["ink"] if i == 0 else C["txt"], "size": 13}), (nm, {"font": F["ar_sb"], "size": 15})]],
             color=C["ink"] if i == 0 else C["txt"], anchor="ctr", align="r")
        ex, ew = cols["eg"]
        rect(s, ex, yy, ew, rh, fill=C["s1"], alpha=0.9, line=C["org"], lw=0.5, lalpha=0.6, r=0.08)
        text(s, ex + 0.15, yy, ew - 0.3, rh, eg, size=11.5, color=C["txt"], anchor="ctr", ls=1.15)
        dx, dw = cols["de"]
        rect(s, dx, yy, dw, rh, fill=C["s1"], alpha=0.9, line=C["line2"], lw=0.5, r=0.08)
        text(s, dx + 0.15, yy, dw - 0.3, rh, de, size=11.5, color=C["txt"], anchor="ctr", ls=1.15)
    text(s, MX, 6.8, SW - 2 * MX, 0.25, "توزيع العناصر على الطبقات اجتهاد توضيحي وفق نموذج المحاضرة؛ الترتيب الفعلي للطبقات داخل البطاقتين غير منشور.",
         size=9, color=C["mute"], font=F["ar"], align="r")
    chrome(s, "ar", 3, 13, TOTAL, "SP1 · pp.11–19 · SP2 · p.5 · BMI 2024 · PAP · BDR")
    notes(s,
        "نوزع العناصر الموثقة على الطبقات الأربع: جسم البطاقة — مصر: بطاقة بلاستيكية منذ 1995 دون إعلان نوع البوليمر، مع علامات خامات تفحص معمليًا؛ ألمانيا: بولي كربونات متعدد الطبقات، وخيط أمان مُشخَّص، وألياف أمان تتألق تحت UV، وشريحة وهوائي. الطباعة — مصر: الطباعة التدريجية، والجلوشيات، والكتابة الميكرونية الظاهرة والخفية، والأحبار المتألقة، وطباعة Relief بكلمة «مصر»؛ ألمانيا: جلوشيات متعددة الألوان، وكتابة ميكرونية موجبة وسالبة، وطباعة قزحية بأحبار UV، وحبر متغير بصريًا. التشخيص — مصر: الصورة والبيانات، والصورة الليزرية المتعددة، ورقم المصنع، والباركود؛ ألمانيا: صورة ملونة ورقم الوثيقة بالحبر النفاث، وحفر ليزري، وعلامات بارزة، وصورة ليزر متغيرة، وبيانات الشريحة. التشطيب — مصر: كينجرام موضعي؛ ألمانيا: Identigram وطلاء حماية وبروز سطحي. التوزيع اجتهاد توضيحي؛ الترتيب الفعلي غير منشور.",
        "Mapping documented elements onto the four layers. Card body — Egypt: plastic card since 1995, polymer unpublished, lab-tested material marks; Germany: multi-layer polycarbonate, personalised security thread, UV security fibres, embedded chip and antenna. Print — Egypt: rainbow printing, guilloches, visible and invisible microtext, UV inks, relief printing of the word 'Egypt'; Germany: multicolour guilloches, positive/negative microprint, iris (rainbow) UV printing, optically variable ink. Personalize — Egypt: portrait and Arabic data, Multi Laser Image, factory number, encrypted 2D barcode; Germany: inkjet colour photo and document number inside the material, laser-engraved data, tactile expiry/CAN, variable laser image, chip data. Finishing — Egypt: local Kinegram; Germany: Identigram, protective lacquer, tactile surface embossing. The layer assignment is our illustrative mapping; the true internal layer order of both cards is not published.",
        "SP1 pp.11–19 (Egyptian features); SP2 p.5 (structure); BMI flyer May 2024 (#1–#13); PAP (layers, lacquer); BDR (polycarbonate); HRW (1995).")
    return s

SLIDES = [s07, s08, s09, s10, s11, s12, s13]
