"""Slides 14–20: chapter 04 — printing technologies (prepress, offset, plates, security backgrounds)."""
from common import *
from pptx.enum.shapes import MSO_SHAPE

def arrow_r(s, x, y, w=0.35, h=0.3, color=None, left=False):
    shp = shape(s, MSO_SHAPE.LEFT_ARROW if left else MSO_SHAPE.RIGHT_ARROW, x, y, w, h, fill=color or C["org"])
    return shp

# ------------------------------------------------------------------ 14 EN printing defined (chapter 04 opener)
def s14(D):
    s = D.new(); bg(s, "bg_opener_r.jpg")
    text(s, SW - 4.95, 0.5, 4.6, 2.95, "04", size=170, font=F["disp_lt"], color=C["txt"], rtl=False, align="r")
    label(s, MX, 0.95, 7, "CHAPTER 04 · PRINTING TECHNOLOGIES")
    title_en(s, [("PRINTING,", False)], y=1.3, w=7, size=46); title_en(s, [("DEFINED", True)], y=1.95, w=7, size=46)
    sub(s, "Creating physical copies of digital or physical content by applying ink, toner or other materials to a surface such as paper, fabric or metal.",
        MX, 2.75, 6.6, 0.8, size=14)
    text(s, MX, 3.6, 7, 0.3, [[("KEY MILESTONE  ", {"font": F["disp_md"], "color": C["org"], "spc": 150, "size": 10}), ("Johannes Gutenberg's printing press", {})]], size=12.5, color=C["txt"])
    x = MX
    for t in ["INKJET", "LASER", "OFFSET", "FLEXOGRAPHY", "3D PRINTING"]:
        w = chip(s, x, 4.0, t, fill=C["s2"] if t != "OFFSET" else C["org"], color=C["txt"] if t != "OFFSET" else C["ink"], size=10)
        x += w + 0.12
    # three-stage flow
    stages = [("01", "PREPRESS", "text, images, design → printing plate"), ("02", "PRINT", "the plate prints the job"), ("03", "POST-PRESS", "finishing → printed product")]
    for i, (n, t, d) in enumerate(stages):
        bx = MX + i * 2.28
        rect(s, bx, 4.7, 2.0, 1.2, fill=C["s1"], alpha=0.92, line=C["org"] if i == 0 else C["line2"], lw=0.75, r=0.08)
        text(s, bx + 0.15, 4.78, 0.6, 0.3, n, size=11, font=F["disp_md"], color=C["org"])
        text(s, bx + 0.15, 5.05, 1.8, 0.4, t, size=17, font=F["disp"], spc=60)
        text(s, bx + 0.15, 5.45, 1.75, 0.45, d, size=9.5, color=C["txt2"], ls=1.0)
        if i < 2: arrow_r(s, bx + 2.03, 5.17, 0.22, 0.24, C["org"])
    text(s, MX, 6.1, 6.9, 0.75, [[("PRINTED PRODUCTS  ", {"font": F["disp_md"], "color": C["txt2"], "spc": 150, "size": 9.5}),
                                  ("books & brochures · newspapers & magazines · leaflets & posters · labels & stickers · ", {}),
                                  ("stamps & securities · credit & check cards", {"color": C["org"]}), (" · folding cartons, blister packs, bags…", {})]],
         size=11, color=C["txt"], ls=1.15)
    # relief principle diagram (right, on ember)
    X0, Y0 = 8.75, 3.55
    rect(s, X0 + 0.2, Y0 + 0.15, 2.4, 0.05, fill=C["txt"])                        # paper
    rect(s, X0 + 0.9, Y0 + 0.62, 1.1, 0.09, fill=C["org"], line=C["peach"], lw=0.5)  # ink
    rect(s, X0 + 0.9, Y0 + 0.71, 1.1, 0.5, fill=C["s3"], line=C["line2"], lw=0.75)  # raised
    rect(s, X0, Y0 + 1.21, 2.9, 0.42, fill=C["s2"], line=C["line2"], lw=0.75)       # lowered
    for t, ty, ly in [("PAPER", Y0 + 0.17, Y0 + 0.05), ("INK", Y0 + 0.66, Y0 + 0.5), ("RAISED SURFACE", Y0 + 0.95, Y0 + 0.85), ("LOWERED SURFACE", Y0 + 1.42, Y0 + 1.32)]:
        line(s, X0 + 2.95 if t != "PAPER" else X0 + 2.65, ty, X0 + 3.25, ty, C["txt2"], 0.6)
        text(s, X0 + 3.3, ly, 1.25, 0.25, t, size=9.5, font=F["disp_md"], color=C["txt"], spc=120)
    text(s, X0, Y0 + 1.8, 4.0, 0.5, "Relief principle shown in the lecture: only the inked, raised surface transfers to the paper.", size=9.5, color=C["txt"], ls=1.05)
    chrome(s, "en", 4, 14, TOTAL, "PP1 · pp.3–6")
    notes(s,
        "Printing is the process of creating physical copies of digital or physical content by applying ink, toner or other materials to a surface such as paper, fabric or metal. Key historical development: Johannes Gutenberg's printing press. Modern printing includes inkjet, laser, offset, flexography and 3D printing, used from personal documents to large-scale commercial production. The process of producing printed products divides into three parts: prepress, print and post-press. Printed products in the widest sense include books and brochures, newspapers and magazines, leaflets and posters, labels and stickers, stamps and securities, credit and check cards, folding cartons, blister packs, bags and paper tissues. The lecture's relief diagram shows paper, ink, raised surface and lowered surface. Course aim (PP1 p.3): digital systems for prepress to produce printing surfaces with lasers, hardware and software, and plate production techniques using computers.",
        "الطباعة هي عملية إنتاج نسخ مادية من محتوى رقمي أو مادي بوضع الحبر أو الحبر الجاف (التونر) أو مواد أخرى على سطح كالورق أو القماش أو المعدن. أهم تطور تاريخي: مطبعة يوهانس جوتنبرج. وتشمل الطباعة الحديثة: النفث الحبري، والليزر، والأوفست، والفلكسوجراف، والطباعة ثلاثية الأبعاد. تنقسم عملية إنتاج المطبوعات إلى ثلاثة أجزاء: ما قبل الطباعة، والطباعة، وما بعد الطباعة. والمطبوعات بأوسع معانيها تشمل الكتب والصحف والملصقات والطوابع والأوراق المالية وبطاقات الائتمان والشيكات والعبوات. ويوضح رسم المحاضرة مبدأ الطباعة البارزة: الورق، الحبر، السطح البارز، السطح المنخفض. هدف المقرر: الأنظمة الرقمية لما قبل الطباعة لإنتاج أسطح الطباعة بالليزر وتقنيات إنتاج الألواح بالحاسب.",
        "PP1 p.3 (course aim), p.4 (printing definition, Gutenberg, techniques), p.5 (prepress/print/post-press; relief diagram), p.6 (printed products).")
    return s

# ------------------------------------------------------------------ 15 AR premedia / prepress chain
def s15(D):
    s = D.new(); bg(s, "bg_glow_tr.jpg")
    title_ar(s, "من الأصل إلى المنتج المطبوع", w=9, size=32)
    sub(s, "ما قبل الطباعة: كل خطوات تجهيز النص والصور والرسوم والتصميم حتى إنتاج «الأصل» الجاهز للطباعة، أي لوح الطباعة. وبمعنى أوسع يُسمّى «ما قبل الوسائط» (Premedia): تجهيز النص والصورة لوسائط النشر المختلفة.",
        MX + 1.2, 1.5, SW - 2 * MX - 1.2, 0.8, size=13.5)
    steps = [("01", "صنع الأصل", "تجهيز النص والصور والتصميم", "الأصل"),
             ("02", "التجهيز (Repro)", "إعداد الأفلام والفصل اللوني", "الفيلم"),
             ("03", "إعداد اللوح", "نقل الصورة إلى سطح الطباعة", "لوح الطباعة"),
             ("04", "الطباعة", "اللوح يطبع العمل", "الفرخ المطبوع"),
             ("05", "التشطيب", "تجهيز المطبوع في صورته النهائية", "المنتج المطبوع")]
    groups = [("ما قبل الوسائط", 0, 0), ("ما قبل الطباعة", 1, 2), ("الطباعة", 3, 3), ("ما بعد الطباعة", 4, 4)]
    cw, gap = 2.22, 0.258; y0 = 2.95
    def colx(i):  # RTL: step 1 on the right
        return SW - MX - (i + 1) * cw - i * gap
    for nm, a, b in groups:
        x1 = colx(b); x2 = colx(a) + cw
        hot = nm == "ما قبل الطباعة"
        rect(s, x1, y0 - 0.5, x2 - x1, 0.32, fill=C["org"] if hot else C["s2"], line=None, r=0.06)
        text(s, x1, y0 - 0.5, x2 - x1, 0.32, nm, size=11, font=F["ar_sb"], color=C["ink"] if hot else C["txt2"], align="c", anchor="ctr")
    for i, (n, t, d, out) in enumerate(steps):
        x = colx(i)
        rect(s, x, y0, cw, 1.75, fill=C["s1"], alpha=0.92, line=C["line"], lw=0.5, r=0.08)
        text(s, x + 0.15, y0 + 0.12, cw - 0.3, 0.3, n, size=13, font=F["disp_md"], color=C["org"], align="r", rtl=False)
        text(s, x + 0.15, y0 + 0.45, cw - 0.3, 0.4, t, size=15, font=F["ar_sb"])
        text(s, x + 0.15, y0 + 0.88, cw - 0.3, 0.6, d, size=11, color=C["txt2"], ls=1.1)
        rect(s, x + 0.15, y0 + 1.95, cw - 0.3, 0.42, fill=None, line=C["org"], lw=0.75, r=0.21)
        text(s, x + 0.15, y0 + 1.95, cw - 0.3, 0.42, out, size=11.5, font=F["ar_md"], color=C["org"], align="c", anchor="ctr")
        if i < 4: arrow_r(s, x - gap + 0.03, y0 + 0.75, gap - 0.06, 0.22, C["line2"], left=True)
    # conventional vs digital
    y1 = 5.6; half = (SW - 2 * MX - 0.2) / 2
    for j, (t, d) in enumerate([("ما قبل الطباعة التقليدية", "أفلام فردية لتجميع الصفحة أو فرخ الطباعة، وتجميع ميكانيكي/يدوي للأفلام، دون أنظمة تعريض رقمي للصفحة كاملة."),
                                ("ما قبل الطباعة الرقمية", "معالجة الصور رقميًا، ومن الحاسب إلى اللوح (CTP)، ومن الحاسب إلى الفيلم (CTF).")]):
        x = SW - MX - (j + 1) * half - j * 0.2
        rect(s, x, y1, half, 1.15, fill=C["s1"], line=C["org"] if j else C["line2"], lw=0.75, r=0.08)
        text(s, x + 0.2, y1 + 0.1, half - 0.4, 0.35, t, size=14, font=F["ar_sb"], color=C["org"] if j else C["txt"])
        text(s, x + 0.2, y1 + 0.47, half - 0.4, 0.65, d, size=11.5, color=C["txt2"], ls=1.15)
    chrome(s, "ar", 4, 15, TOTAL, "PP1 · pp.7–9")
    notes(s,
        "ما قبل الطباعة يشمل كل خطوات المعالجة من تجهيز النص والصور الأصلية والرسوم والتصميم حتى إنتاج الأصل الجاهز للطباعة (لوح الطباعة) الذي يُستخدم في مرحلة الطباعة. وبمعنى أوسع يُسمى «ما قبل الوسائط» أي تجهيز النص والصورة لوسائط النشر المختلفة، وقد تُدمج مرحلة ما قبل الوسائط داخل مرحلة ما قبل الطباعة. السلسلة: صنع الأصل ← الأصل ← تجهيز الاستنساخ ← الفيلم ← إعداد اللوح ← لوح الطباعة ← الطباعة ← الفرخ المطبوع ← التشطيب ← المنتج. الفرق بين التقليدي والرقمي في طريقة استخدام الأفلام: التقليدي يستخدم أفلامًا فردية وتجميعًا ميكانيكيًا أو يدويًا دون أنظمة تعريض رقمي للصفحة كاملة، والرقمي يشمل معالجة الصور رقميًا والطباعة من الحاسب إلى اللوح ومن الحاسب إلى الفيلم.",
        "Prepress includes all processing steps from preparing text, original images, graphics and the design concept up to the ready-for-print master (the printing plate), which is then used to print the job. In a wider sense prepress is called premedia — preparing text and images for several publication media; premedia may already be incorporated in prepress. The chain: making the original → original → repro preparation → film → platemaking → printing plate → printing process → printed sheet → print finishing → printed product (premedia | prepress | press | postpress). The distinction between conventional and digital prepress is how films are used: conventional uses individual films with mechanical/manual assembly and no digital full-page exposure; digital covers digital image processing, computer-to-plate and computer-to-film.",
        "PP1 p.7 (prepress definition), p.8 (premedia; workflow figure), p.9 (conventional vs digital prepress).")
    return s

# ------------------------------------------------------------------ 16 EN offset lithography
def cyl(s, cx, cy, r, fill, line_c, lab=None, grad=None):
    o = oval(s, cx - r, cy - r, 2 * r, 2 * r, fill=fill, line=line_c, lw=1.25, grad=grad, angle=45)
    oval(s, cx - 0.06, cy - 0.06, 0.12, 0.12, fill=C["txt"] if fill != C["txt"] else C["ink"])
    return o

def s16(D):
    s = D.new(); bg(s, "bg_glow_br.jpg")
    title_en(s, [("OFFSET LITHOGRAPHY", False)], y=0.8, w=6.5, size=42)
    text(s, MX, 1.48, 6.3, 0.35, "INDIRECT  ·  OIL AND WATER REPEL", size=13, font=F["disp_md"], color=C["org"], spc=200)
    steps = [("IMAGE PLATE", "A metal plate carries the image."),
             ("INK & WATER", "Water wets the hydrophilic non-image areas; oil-based ink adheres only to the hydrophobic image areas."),
             ("BLANKET TRANSFER", "The inked image passes from the plate to a rubber blanket cylinder."),
             ("PRINTING", "The blanket 'offsets' the image onto paper, board or plastic held by the impression cylinder.")]
    y = 2.05
    for i, (t, d) in enumerate(steps):
        line(s, MX, y, MX + 5.9, y, C["line"], 0.5)
        text(s, MX, y + 0.08, 0.5, 0.3, f"{i+1:02d}", size=13, font=F["disp_md"], color=C["org"])
        text(s, MX + 0.55, y + 0.08, 5.3, 0.3, t, size=14, font=F["disp"], spc=80)
        text(s, MX + 0.55, y + 0.4, 5.3, 0.5, d, size=11.5, color=C["txt2"], ls=1.08)
        y += 0.92
    rect(s, MX, 5.85, 5.9, 0.95, fill=C["s1"], line=C["org"], lw=0.75, r=0.08)
    text(s, MX + 0.2, 5.85, 5.5, 0.95, [[("WHY INDIRECT?  ", {"font": F["disp_md"], "color": C["org"], "spc": 120}),
                                         ("The plate never touches the paper, so it lasts longer; the flexible rubber conforms to rough media (canvas, cloth, wood). Result: high, consistent quality for small to high volumes.", {})]],
         size=11, color=C["txt"], anchor="ctr", ls=1.15)
    # diagram
    cx = 9.55
    P, B, I = (cx, 2.45, 0.78), (cx, 4.03, 0.78), (cx, 5.61, 0.78)
    # water train (left, bone) & ink train (right, orange)
    rect(s, 7.05, 1.55, 1.05, 0.38, fill=C["txt2"], alpha=0.25, line=C["txt2"], lw=0.75, r=0.04)
    cyl(s, 7.9, 1.45, 0.26, C["s2"], C["txt2"]); cyl(s, 8.45, 1.12, 0.2, C["s2"], C["txt2"]); cyl(s, 8.72, 1.62, 0.22, C["s2"], C["txt2"])
    for (x, y, r) in [(10.45, 1.62, 0.22), (10.75, 1.12, 0.2), (11.25, 1.42, 0.3), (11.55, 0.95, 0.18)]:
        cyl(s, x, y, r, C["deep"], C["org"])
    cyl(s, *P, None, C["org"], grad=[(0, C["org"], 1), (100, C["deep"], 1)])
    cyl(s, *B, C["s3"], C["org"])
    cyl(s, *I, C["s2"], C["line2"])
    # substrate path
    yp = 4.03 + 0.78 + 0.005
    line(s, 6.95, yp, 12.65, yp, C["txt"], 1.5, tail="triangle")
    rect(s, 8.25, yp - 0.035, 0.8, 0.07, fill=C["org"])  # printed image on sheet
    labels = [("WATER ROLLERS", 7.05, 0.72, 8.3, 1.0), ("INK ROLLERS", 11.0, 0.55, 11.3, 0.75), ("PLATE CYLINDER", 10.85, 2.35, 10.33, 2.45),
              ("BLANKET (OFFSET) CYLINDER", 10.85, 3.93, 10.33, 4.03), ("IMPRESSION CYLINDER", 10.85, 5.51, 10.33, 5.61),
              ("SUBSTRATE", 11.4, yp - 0.33, None, None), ("WATER", 7.08, 1.95, None, None)]
    for t, lx, ly, ax, ay in labels:
        if ax is not None and t not in ("WATER ROLLERS", "INK ROLLERS"):
            line(s, ax, ay, lx - 0.05, ly + 0.12, C["txt2"], 0.6)
        text(s, lx, ly, min(2.2, SW - MX + 0.45 - lx), 0.26, t, size=9.5, font=F["disp_md"], color=C["txt"], spc=120)
    chrome(s, "en", 4, 16, TOTAL, "PP1 · pp.10–13, 22 · PP2 · pp.3, 11")
    notes(s,
        "Offset printing, also called offset lithography, is a mass-production method in which the image on a metal plate is transferred (offset) to a rubber blanket or roller and then to the print media. The indirect method is based on the principle that water and oil repel each other. How it works: (1) image plate — a metal plate carries the image; (2) ink and water — the plate is first dampened with water, which adheres to hydrophilic areas; then oil-based ink adheres only to the hydrophobic image areas; (3) blanket transfer — the inked image passes to the rubber blanket cylinder; (4) printing — the blanket offsets the image onto the final surface held by the impression cylinder. Because the media never touches the metal plate, plate life is prolonged; the flexible rubber conforms to rough surfaces such as canvas, cloth or wood. The main advantage is high and consistent image quality; it can be used for small, medium or high-volume jobs. The diagram is redrawn from the lecture figures (water rollers, ink rollers, plate, blanket/offset and impression cylinders, paper).",
        "طباعة الأوفست (الليثوغرافيا الأوفست) طريقة إنتاج كمي تُنقل فيها الصورة من لوح معدني إلى بطانية مطاطية ثم إلى وسيط الطباعة، وهي طريقة غير مباشرة قائمة على تنافر الماء والزيت. كيف تعمل: (1) لوح الصورة المعدني؛ (2) الحبر والماء: يُرطَّب اللوح بالماء فيلتصق بالمناطق المحبة للماء، ثم يلتصق الحبر الزيتي بالمناطق الطاردة للماء التي تحمل الصورة؛ (3) النقل إلى أسطوانة البطانية المطاطية؛ (4) الطباعة: البطانية تنقل الصورة إلى السطح النهائي الذي تحمله أسطوانة الضغط. لأن الورق لا يلمس اللوح المعدني يطول عمر اللوح، ولأن المطاط مرن يتكيف مع الأسطح الخشنة كالقماش والخشب. الميزة الرئيسية: جودة صورة عالية وثابتة، وتصلح للكميات الصغيرة والمتوسطة والكبيرة.",
        "PP1 p.10–12 (offset definition, indirect method, plate life, rough media), p.13 (quality, volumes), p.22 (how it works); PP2 p.3, p.11 (cylinder diagrams). Diagram redrawn natively.")
    return s

# ------------------------------------------------------------------ 17 AR sheet-fed vs web
def s17(D):
    s = D.new(); bg(s, "bg_center.jpg")
    title_ar(s, "الأوفست: أفرخ أم بكرات؟", w=8, size=32)
    sub(s, "نوعان من آلات الأوفست شائعا الاستخدام في النشر اليوم.", SW - MX - 8, 1.5, 8, 0.4, size=13)
    half = (SW - 2 * MX - 0.25) / 2
    panels = [("التغذية بالأفرخ", "Sheet-fed", "12,000–24,000", "فرخ في الساعة",
               ["أفرخ ورق منفردة تُغذّى إلى الآلة.", "تُقص مسبقًا بمقاس النشر النهائي أو بعد الطباعة.", "للأعمال الصغيرة والمتوسطة الثابتة، كالكتب محدودة الإصدار.", "تحسنت سرعتها كثيرًا مع التحديث."]),
              ("التغذية بالبكرات", "Web-fed", "≈ 80,000", "فرخ متماثل في الساعة",
               ["آلات أكبر وأسرع تُغذّى ببكرات ورق ضخمة.", "تُفصل الصفحات وتُقص بعد الطباعة.", "أوفر للأعداد الكبيرة متغيرة المحتوى كالصحف والعلب.", "مثالية للكميات الكبيرة والمواعيد الضيقة."])]
    for j, (t, en, num, unit, rows) in enumerate(panels):
        x = SW - MX - (j + 1) * half - j * 0.25
        rect(s, x, 2.05, half, 2.75, fill=C["s1"], alpha=0.9, line=C["org"] if j == 0 else C["line2"], lw=0.75, r=0.1)
        text(s, x + 0.25, 2.18, half - 0.5, 0.4, [[(t, {"font": F["ar_sb"], "size": 17}), ("   " + en, {"font": F["disp_md"], "color": C["txt2"], "size": 12})]])
        text(s, x + 0.25, 2.62, half - 0.5, 0.75, num, size=40, font=F["disp_lt"], color=C["org"], align="r", rtl=False)
        text(s, x + 0.25, 3.32, half - 0.5, 0.3, unit, size=11, color=C["txt2"])
        yy = 3.68
        for r in rows:
            text(s, x + 0.25, yy, half - 0.5, 0.28, "•  " + r, size=11.5, color=C["txt"])
            yy += 0.27
    # advantages / disadvantages
    adv = [("جودة عالية", "دقة ألوان وحدّة ممتازة للصور والنصوص."), ("تعدد الأسطح", "ورق وكرتون وبلاستيك."), ("اقتصادية", "للإنتاج الكبير."), ("ثبات النتائج", "عبر الكميات الكبيرة.")]
    dis = [("تستغرق وقتًا", "خطوات عديدة منها تجهيز الألواح."), ("تخصيص محدود", "الألواح الخاصة تضيف وقتًا وتكلفة."), ("غير مناسبة للكميات الصغيرة", "تكلفة التجهيز مرتفعة نسبيًا."), ("مخاوف بيئية", "الكيماويات تتطلب تخلصًا آمنًا.")]
    for j, (hdr, items, col) in enumerate([("المزايا", adv, C["org"]), ("العيوب", dis, C["txt2"])]):
        x = SW - MX - (j + 1) * half - j * 0.25
        text(s, x, 5.0, half, 0.32, hdr, size=13, font=F["ar_sb"], color=col)
        for k, (a, b) in enumerate(items):
            cx = x + half - (k % 2 + 1) * (half / 2)
            cy = 5.38 + (k // 2) * 0.72
            rect(s, cx + 0.05, cy, half / 2 - 0.1, 0.64, fill=C["s1"], line=C["line"], lw=0.5, r=0.06)
            text(s, cx + 0.15, cy + 0.02, half / 2 - 0.3, 0.6, [[(a + "  ", {"font": F["ar_sb"], "color": C["txt"]}), (b, {})]], size=10.5, color=C["txt2"], anchor="ctr", ls=1.05)
    chrome(s, "ar", 4, 17, TOTAL, "PP1 · pp.15–25")
    notes(s,
        "نوعان من آلات الأوفست شائعا الاستخدام: التغذية بالأفرخ والتغذية بالبكرات (الويب). في الأفرخ تُغذّى أوراق منفردة، وتُقص مسبقًا أو بعد الطباعة، وتنتج كميات أصغر لكنها ما زالت خيارًا سريعًا: من 12,000 إلى 24,000 فرخ في الساعة، وقد تحسنت سرعتها حتى قاربت وظائف آلات الويب. في الويب تُستخدم آلات أكبر وأسرع تُغذّى ببكرات ورق كبيرة وتُفصل الصفحات وتُقص بعد ذلك؛ وهي أوفر للمطبوعات الكبيرة متغيرة المحتوى كالصحف والعلب. تذكر المحاضرة «أكثر من 3,000 في الدقيقة، أي نحو 80,000 فرخ متماثل في الساعة» — والرقمان غير متسقين حسابيًا، فاعتمدنا الرقم الساعي. المزايا: جودة عالية، وتعدد الأسطح بما فيها البلاستيك، واقتصادية للإنتاج الكبير مع تكلفة تجهيز أقل من طرق أخرى، وثبات النتائج. العيوب: تستغرق وقتًا، وتخصيص محدود، وغير اقتصادية للكميات الصغيرة، ومخاوف بيئية من الكيماويات.",
        "Two offset press types are common: sheet-fed and web. Sheet-fed feeds individual sheets, pre-cut or trimmed after printing; it produces smaller quantities but is still quick — 12,000 to 24,000 sheets per hour — and has improved to perform similar functions to web presses; popular for small and medium fixed jobs such as limited-edition books. Web offset uses larger, higher-speed machines fed by large paper rolls; pages are separated and trimmed afterwards; more cost-effective for high-volume publications whose content changes often (newspapers, boxes). The lecture states 'over 3,000 papers per minute, translating to about 80,000 identical sheets per hour' — the two figures are inconsistent; we show the hourly figure. Advantages: high quality, versatility (paper, cardboard, plastic), cost-effective for large runs, consistency. Disadvantages: time-consuming, limited customization, not ideal for small runs, environmental concerns about chemicals.",
        "PP1 p.15 (two press types), pp.16–18 (sheet-fed), pp.19–21 (web), pp.23–25 (advantages/disadvantages).")
    return s

# ------------------------------------------------------------------ 18 EN plates
def plate_diagram(s, x, y, w, kind):
    base_h = 0.32
    if kind == "wet":
        n = 5; seg = w / n
        for i in range(n):
            ink = i % 2 == 1
            rect(s, x + i * seg + 0.02, y + 0.06, seg - 0.04, 0.42, fill=C["org"] if ink else C["txt2"], alpha=1 if ink else 0.35, r=0.2)
        rect(s, x, y + 0.3, w, base_h, fill="5A5A5A", line=C["line2"], lw=0.5)
    else:
        n = 5; seg = w / n
        for i in range(n):
            ink = i % 2 == 1
            if ink:
                rect(s, x + i * seg + 0.02, y + 0.06, seg - 0.04, 0.42, fill=C["org"], r=0.2)
            else:
                rect(s, x + i * seg, y + 0.18, seg, 0.14, fill=C["peach"], alpha=0.85)
        rect(s, x, y + 0.3, w, base_h, fill="5A5A5A", line=C["line2"], lw=0.5)

def s18(D):
    s = D.new(); bg(s, "bg_quiet.jpg")
    title_en(s, [("THE PRINTING ", False), ("PLATE", True)], y=0.8, w=8, size=42)
    sub(s, "File preparation feeds plate preparation — and the plate decides how many impressions, at what quality and cost.", MX, 1.5, 11.5, 0.45, size=13.5)
    # wet vs waterless
    label(s, MX, 2.2, 5.6, "CONVENTIONAL (WET) vs WATERLESS")
    plate_diagram(s, MX, 2.6, 2.6, "wet")
    text(s, MX + 2.8, 2.55, 2.9, 0.85, [[("WET PLATE  ", {"font": F["disp_md"], "color": C["txt"], "spc": 100}), ("uses a dampening (water-softener) solution — water + alcohol film on non-image areas; tainted water leaves the press.", {})]],
         size=10.5, color=C["txt2"], ls=1.08)
    plate_diagram(s, MX, 3.75, 2.6, "dry")
    text(s, MX + 2.8, 3.7, 2.9, 0.85, [[("WATERLESS  ", {"font": F["disp_md"], "color": C["org"], "spc": 100}), ("no dampening solution — a silicone-rubber layer repels ink; ink sits where the silicone is removed.", {})]],
         size=10.5, color=C["txt2"], ls=1.08)
    for t, c, xx in [("INK", C["org"], MX), ("WATER FILM", C["txt2"], MX + 0.75), ("SILICONE", C["peach"], MX + 1.75)]:
        rect(s, xx, 4.62, 0.14, 0.14, fill=c, alpha=0.9); text(s, xx + 0.2, 4.56, 1.0, 0.25, t, size=8.5, font=F["disp_md"], color=C["txt2"], spc=100)
    # CTP build
    label(s, MX, 5.05, 5.6, "CTP PLATE BUILD (DOUBLE-LAYER)")
    layers = [("IR-sensitive layer", C["org"]), ("UV-ink-resistant layer", C["org2"]), ("Hydrophilic layer", C["peach"]), ("Multi-grain layer", "8A8A8A"), ("Aluminium", "5A5A5A")]
    for i, (t, c) in enumerate(layers):
        yy = 5.4 + i * 0.27
        rect(s, MX, yy, 2.6, 0.22, fill=c, alpha=0.95, r=0.02)
        text(s, MX + 2.8, yy - 0.02, 2.9, 0.25, t, size=10.5, color=C["txt"])
    line(s, SW / 2 - 0.25, 2.25, SW / 2 - 0.25, 6.8, C["line2"], 0.75)
    # substrates
    X, W = SW / 2, SW - MX - SW / 2
    label(s, X, 2.2, W, "PLATE SUBSTRATES · RUN LENGTH")
    subs = [("METAL", "Grained aluminium holds a thin wetting film on non-image areas; silver-halide or photopolymer coatings.", "100,000 – 2,000,000+", 1.0),
            ("POLYESTER", "Cheaper than metal; small, colour-coded quality work; red or IR laser; silver-halide + toner coating fused by heat; 0.004–0.012 in.", "≤ 25,000", 0.55),
            ("PAPER", "Cellulose, not grained but chemically treated; toner-based imaging; small runs on small presses; 0.004–0.008 in.", "small runs", 0.22)]
    yy = 2.6
    for nm, d, run, frac in subs:
        text(s, X, yy, 2.0, 0.4, nm, size=20, font=F["disp"])
        text(s, X + W - 2.6, yy + 0.05, 2.6, 0.35, run, size=17, font=F["disp_lt"], color=C["org"], align="r")
        rect(s, X, yy + 0.48, W, 0.08, fill=C["s2"], r=0.04)
        rect(s, X, yy + 0.48, W * frac, 0.08, grad=[(0, C["deep"], 1), (100, C["org"], 1)], angle=0, r=0.04)
        text(s, X, yy + 0.65, W, 0.65, d, size=10.5, color=C["txt2"], ls=1.08)
        yy += 1.42
    text(s, X, 6.78, W, 0.22, "Bar length is indicative (log-like), not to scale.", size=8.5, color=C["mute"])
    chrome(s, "en", 4, 18, TOTAL, "PP2 · pp.6–21, 28")
    notes(s,
        "Lithographic preparation has two parts: file preparation and plate preparation. Conventional printing plates use a water-softener (dampening) solution during printing — a water-and-alcohol film covers non-image areas and ink sits on image areas; this results in tainted water being discharged from the press. Waterless plates do not use a dampening solution: a silicone rubber layer repels ink, and exposure/development removes silicone where ink should sit. Plates are classified by substrate: metal, plastic (polyester) and paper. Metal plates (grained aluminium) retain a thin film of wetting solution in non-printing areas; they are coated with photosensitive coatings including silver halide and photopolymers, and are used for large runs from 100,000 to 2 million or more. Polyester plates are less expensive than metal and a good alternative for 25,000 or fewer; used for small, colour-coded high-quality prints; earlier expansion and registration problems were solved; exposed by red or infrared lasers; coatings are mostly silver halide covered with a toner-based coating fused by heat; thickness 0.004–0.012 in (thicker for longer runs). Paper plates are cellulose, 0.004–0.008 in, not grained but chemically treated, used for small quantities on small presses with toner-based recording. Double-layer CTP plate: IR-sensitive, UV-ink-resistant, hydrophilic, multi-grain and aluminium layers (another figure: over-coat, photosensitive, under-coat, aluminium base).",
        "تنقسم التجهيزات الليثوغرافية إلى تجهيز الملف وتجهيز اللوح. الألواح التقليدية تستخدم محلول ترطيب (ماء وكحول) أثناء الطباعة ويخرج من الآلة ماء ملوث، أما الألواح بدون ماء فلا تستخدم محلول ترطيب وتعتمد على طبقة مطاط السيليكون الطاردة للحبر. تُصنَّف الألواح حسب الخامة: معدنية وبلاستيكية (بوليستر) وورقية. المعدنية من الألومنيوم المحبب تحتفظ بطبقة رقيقة من محلول الترطيب في المناطق غير الطابعة، وتُغطى بطبقات حساسة للضوء (هاليد الفضة أو البوليمرات الضوئية)، وتطبع من 100,000 إلى مليوني نسخة أو أكثر. ألواح البوليستر أرخص وتناسب 25,000 نسخة أو أقل، للمطبوعات الصغيرة الملونة عالية الجودة، وتُعرَّض بليزر أحمر أو تحت أحمر، وسمكها 0.004–0.012 بوصة. الألواح الورقية من السليلوز بسمك 0.004–0.008 بوصة، غير محببة ومعالجة كيميائيًا، للكميات الصغيرة بتقنية التونر. بنية لوح CTP مزدوج الطبقة: طبقة حساسة للأشعة تحت الحمراء، وطبقة مقاومة لأحبار UV، وطبقة محبة للماء، وطبقة متعددة الحبيبات، والألومنيوم.",
        "PP2 p.7 (file vs plate preparation), pp.8–13 (wet vs waterless), p.15 (substrate classes), pp.16–17 (metal), pp.18–19 (CTP structures), p.20 (polyester), p.21 (paper), p.28 (sequence). Diagrams redrawn natively.")
    return s

# ------------------------------------------------------------------ 19 AR plate-making chain
def s19(D):
    s = D.new(); bg(s, "bg_glow_tl.jpg")
    title_ar(s, "صناعة لوح الطباعة خطوة بخطوة", w=9, size=32)
    sub(s, "مراحل التجهيز التقليدي: التعريض الضوئي، المعالجة الكيميائية، التثقيب، ثني الحواف — تسبقها فصل الألوان وتليها خطوط CTP الآلية.", SW - MX - 10.5, 1.5, 10.5, 0.45, size=13)
    cols = [("01", "فصل الألوان", "تجهيز الملف ثم فصل صورة RGB على الحاسب إلى أربعة ألواح: C · M · Y · K."),
            ("02", "التعريض الضوئي", "تلامس كامل بين فيلم المونتاج واللوح في موضعه الصحيح، زجاج نظيف بلا غبار أو بصمات، شفط جيد، ضوء قوي، وزمن تعريض مناسب؛ تغييره يغيّر حجم النقطة."),
            ("03", "المعالجة الكيميائية", "يدوية أو آلية: إظهار ← غسيل مائي ← تصميغ ← تجفيف، مع ضبط الحرارة ونِسب المحلول والماء ولزوجة الصمغ."),
            ("04", "خط CTP الآلي", "محمِّل آلي ← جهاز التعريض ← المُعالِج ← المُكدِّس. وحدات المعالج: تغذية، معالجة، غسيل، تصميغ، تجفيف، تسليم."),
            ("05", "تثقيب اللوح", "ثقوب خاصة لتثبيت الفيلم دون حركة، وتوحيد تطابق الألوان، وضبط موضع اللوح على أسطوانته."),
            ("06", "ثني الحواف والتركيب", "ثني حافتي اللوح ليُركّب على الأسطوانة؛ يثبت عبر الثقوب على مسامير الآلة، ورافعتان تمسكان الحافتين وتثنيانهما.")]
    n = len(cols); gap = 0.12; cw = (SW - 2 * MX - gap * (n - 1)) / n
    y0 = 2.25
    for i, (num, t, d) in enumerate(cols):
        x = SW - MX - (i + 1) * cw - i * gap
        rect(s, x, y0, cw, 3.65, fill=C["s1"], alpha=0.92, line=C["org"] if i in (1, 2) else C["line"], lw=0.6, r=0.08)
        rect(s, x, y0, cw, 0.06, fill=C["org"] if i in (1, 2) else C["line2"])
        text(s, x + 0.15, y0 + 0.2, cw - 0.3, 0.5, num, size=26, font=F["disp_lt"], color=C["org"], align="r", rtl=False)
        text(s, x + 0.12, y0 + 0.78, cw - 0.24, 0.4, t, size=13.5, font=F["ar_sb"])
        text(s, x + 0.12, y0 + 1.22, cw - 0.24, 2.4, d, size=10.5, color=C["txt2"], ls=1.18)
        if i == 0:
            for k, ch in enumerate("CMYK"):
                bx = x + cw - 0.27 - k * 0.38
                rect(s, bx - 0.05, y0 + 3.05, 0.32, 0.32, fill=[C["txt"], C["txt2"], C["mute"], C["ink"]][k], line=C["line2"], lw=0.5, r=0.04)
                text(s, bx - 0.05, y0 + 3.05, 0.32, 0.32, ch, size=10, font=F["disp_md"], color=C["ink"] if k < 3 else C["txt"], align="c", anchor="ctr", rtl=False)
        if i == 4:
            # registration-hole layout redrawn from PP2 p.32 (mm)
            px0, pw, yy = x + 0.16, cw - 0.32, y0 + 2.45
            line(s, px0, yy, px0 + pw, yy, C["txt2"], 1)
            for fx, kind in [(0.03, 2), (0.12, 1), (0.5, 1), (0.88, 1), (0.97, 2)]:
                hx = px0 + fx * pw
                if kind == 1: rect(s, hx - 0.05, yy - 0.03, 0.1, 0.07, line=C["org"], lw=0.9, r=0.02)
                else: rect(s, hx - 0.03, yy - 0.1, 0.06, 0.1, line=C["txt2"], lw=0.9, r=0.03)
            for a, b, yv, t in [(0.12, 0.5, 0.26, "196.5"), (0.5, 0.88, 0.26, "196.5"), (0.03, 0.97, 0.62, "425")]:
                line(s, px0 + a * pw, yy + yv, px0 + b * pw, yy + yv, C["org"] if t != "425" else C["txt2"], 0.75, head="triangle", tail="triangle")
                text(s, px0 + a * pw, yy + yv + 0.02, (b - a) * pw, 0.25, t, size=10, font=F["disp_md"],
                     color=C["org"] if t != "425" else C["txt2"], align="c", rtl=False)
            text(s, px0, yy + 0.88, pw, 0.25, "مم · عن رسم المحاضرة", size=9, font=F["ar"], color=C["mute"], align="c")
    rect(s, MX, 6.1, SW - 2 * MX, 0.72, fill=C["deep"], alpha=0.35, line=C["org"], lw=0.6, r=0.08)
    text(s, MX + 0.25, 6.1, SW - 2 * MX - 0.5, 0.72, [[("السلامة في أقسام تجهيز الألواح:  ", {"font": F["ar_sb"], "color": C["org"]}),
                                                         ("تهوية جيدة · قفازات لمنع ملامسة الكيماويات · حماية العين · حرارة بين 18 و22 °م · خزانة إسعافات أولية", {})]],
         size=12, color=C["txt"], anchor="ctr")
    chrome(s, "ar", 4, 19, TOTAL, "PP2 · pp.6–7, 22–34")
    notes(s,
        "يتكون تحضير الطباعة الليثوغرافية من جزأين: تجهيز الملف (File preparation) وتجهيز اللوح (Plate preparation). مراحل التجهيز التقليدي للألواح: التعريض الضوئي (فوتوليثوغرافيا)، والمعالجة الكيميائية، وتثقيب اللوح، وثني الحواف. في التعريض يوضع فيلم المونتاج في تلامس كامل مع اللوح في الموضع الصحيح مع مراعاة مقاس الدبوس، والتأكد من نظافة الزجاج من الغبار والبصمات، وقوة الشفط، وقوة مصدر الضوء، وتحديد زمن التعريض المناسب؛ وزيادة أو تقليل زمن التعريض للمادة سالبة الأداء يغيّر حجم النقطة. المعالجة الكيميائية يدوية أو آلية، والأجهزة الآلية مصممة للسرعة مع معايرة كل المراحل: التحكم في حرارة وحدات الإظهار، ونسب محلول الإظهار وماء الغسيل، ونسبة الصمغ ولزوجته؛ والمراحل: إظهار، غسيل مائي، تصميغ، تجفيف، عبر وحدات: تغذية، معالجة كيميائية، غسيل، تصميغ، تجفيف، تسليم. خط CTP: محمّل آلي، جهاز التعريض، المعالج، المكدّس. فصل الألوان: صورة RGB على الحاسب تُفصل إلى سماوي وأرجواني وأصفر وأسود. التثقيب: ثقوب خاصة لتثبيت الفيلم دون حركة، وتوحيد تطابق الألوان، وضمان وضع اللوح صحيحًا على الأسطوانة. ثني الحواف: لتركيب اللوح على الأسطوانة، وتثبيته عبر الثقوب على مسامير الآلة، ورافعتان تثنيان الحافتين. السلامة: تهوية القسم، وقفازات، وحماية العين من الكيماويات، وحرارة 18–22 °م، وخزانة إسعافات أولية.",
        "Lithographic printing preparation has two parts: file preparation and plate preparation. Traditional plate preparation: photolithography, chemical treatment, plate piercing and edge bending. Exposure: the montage film in full contact with the plate at the correct position (allowing for the pin size), clean glass with no dust or fingerprints, adequate suction, a strong light source and the right exposure time; increasing or reducing exposure for negative-working material changes the dot size. Chemical processing is manual or automated; automated developers are built for speed with calibration of every stage — control of developer temperature, developer and wash-water supply ratios, and gum supply ratio and viscosity; stages: development, water washing, gumming, drying; processor units: feeding, chemical treatment, water washing, gumming, drying, delivery. A CTP line: autoloader, platesetter (e.g. UV-800FA), processor, stacker. Colour separation: an RGB image is separated into cyan, magenta, yellow and black. Perforation: special holes for secure film placement, standardized colour matching and correct positioning on the plate cylinder (diagram: holes 196.5 mm apart, 425 mm between outer slots). Edge bending: edges are bent for mounting; the plate is fixed through its holes onto the machine pins and two levers grip and bend the edges. Safety: ventilation, gloves, keep chemicals from eyes, 18–22 °C, first-aid cabinet.",
        "PP2 pp.6–7 (file vs plate preparation), p.22 (stages), pp.23–24 (photolithography, dot size), pp.25–27 (chemical processing), p.29 (CTP line), p.30 (CMYK), p.32 (perforation), p.33 (edge bending), p.34 (safety). CMYK tiles shown in neutral tones to respect the deck palette.")
    return s

# ------------------------------------------------------------------ 20 EN from press to card
def s20(D):
    s = D.new(); bg(s, "bg_glow_br.jpg")
    title_en(s, [("FROM PRESS ", False), ("TO CARD", True)], y=0.8, w=8, size=42)
    sub(s, "Security backgrounds are where prepress and offset meet the identity card.", MX, 1.5, 8, 0.4, size=13.5)
    cols = [("GUILLOCHE", ["eg_m_guilloche_band.png", "de_m_guilloche1.png"],
             "Precise designs from special software sold only to governments. Under a magnifier the lines are continuous — other printing shows adjacent dots.",
             "EG  guilloche security printing (SP1)", "DE  multicolour guilloches, anti-copy structures (BMI #6)"),
            ("RAINBOW · IRIS", ["eg_m_rainbow_bg.png", "de_m_uv_eagle.png"],
             "A continuous colour gradient across the design — 'one of the most sophisticated printing techniques'.",
             "EG  back design in rainbow printing (SP1)", "DE  UV eagle & lettering in rainbow printing (BMI #4)"),
            ("MICROTEXT · SPECIAL INKS", ["eg_m_title.png", "de_m_microprint.png"],
             "Lettering legible only with a loupe; inks invisible in daylight but visible under UV, or visible and glowing under UV.",
             "EG  visible & invisible microtext, UV eagle (SP1)", "DE  ± microprint, multicolour UV, OVI ink (BMI #4,5,7)")]
    cw, gap = 3.95, 0.14
    for i, (t, imgs, d, eg, de) in enumerate(cols):
        x = MX + i * (cw + gap)
        frame_pic(s, imgs[0], x, 2.1, cw / 2 - 0.05, 1.25, r=0.08)
        frame_pic(s, imgs[1], x + cw / 2 + 0.05, 2.1, cw / 2 - 0.05, 1.25, r=0.08)
        text(s, x, 3.5, cw, 0.35, t, size=17, font=F["disp"], spc=80)
        text(s, x, 3.88, cw, 0.85, d, size=11, color=C["txt2"], ls=1.1)
        text(s, x, 4.72, cw, 0.28, [[(eg[:2], {"font": F["disp_md"], "color": C["org"]}), (eg[2:], {})]], size=10, color=C["txt"])
        text(s, x, 4.98, cw, 0.28, [[(de[:2], {"font": F["disp_md"], "color": C["txt"]}), (de[2:], {})]], size=10, color=C["txt"])
    # documented vs general practice
    rect(s, MX, 5.45, 4.1, 1.35, fill=C["s1"], line=C["line2"], lw=0.6, r=0.08)
    text(s, MX + 0.2, 5.52, 3.8, 0.3, "DOCUMENTED", size=10.5, font=F["disp_md"], color=C["txt"], spc=180)
    text(s, MX + 0.2, 5.82, 3.8, 0.95, "Which security printing appears on each card — from the lecture (Egypt) and the BMI flyer (Germany).", size=10.5, color=C["txt2"], ls=1.1)
    rect(s, MX + 4.25, 5.45, SW - 2 * MX - 4.25, 1.35, fill=C["deep"], alpha=0.25, line=C["org"], lw=0.6, r=0.08)
    text(s, MX + 4.45, 5.52, 7.5, 0.3, "GENERAL INDUSTRY PRACTICE — NOT COUNTRY-SPECIFIC", size=10.5, font=F["disp_md"], color=C["org"], spc=180)
    text(s, MX + 4.45, 5.82, 7.6, 0.95, "Card security backgrounds are typically offset-printed on large sheets of card material — often waterless or UV-curing offset on non-absorbent plastics — with special spot inks rather than CMYK, before personalization. Neither the lectures nor official sources name the presses used for these two cards.",
         size=10.5, color=C["txt"], ls=1.1)
    chrome(s, "en", 4, 20, TOTAL, "SP1 · pp.13, 18 · BMI 2024 · general practice")
    notes(s,
        "Security backgrounds connect the printing chapter with the cards. Guilloche security printing: precise designs prepared with special software sold only to governments; the lines appear connected, unlike other printing methods which appear as adjacent dots, and are examined with a magnifying glass (SP1 p.18). Rainbow printing: one of the most sophisticated printing techniques (SP1 p.13); BMI describes rainbow (iris) printing as a continuous colour gradient. Microtext and special inks: visible microprint readable with a 5× magnifier; invisible microtext under UV; UV-glowing inks visible to the naked eye (SP1 pp.15, 18). Germany: multicolour guilloches, complex patterns and anti-copy structures; positive and negative microprint; UV eagle and multicolour lettering in rainbow printing; optically variable ink (BMI #4–#7). General practice (not documented for either card): card backgrounds are typically offset-printed on sheets of card material, often waterless or UV-curing on plastics, with special spot inks, before personalization.",
        "الخلفيات الأمنية هي نقطة التقاء الطباعة بالبطاقات. الجلوشيات: تصميمات دقيقة ببرامج خاصة لا تُباع إلا للحكومات، خطوطها متصلة على عكس الطباعة العادية التي تظهر نقاطًا متجاورة، وتُفحص بالعدسة. الطباعة التدريجية (قوس قزح): من أعقد التقنيات الطباعية، وهي تدرج لوني متصل. الكتابة الميكرونية والأحبار الخاصة: كتابة ظاهرة تُقرأ بعدسة 5×، وكتابة خفية تحت الأشعة فوق البنفسجية، وأحبار ظاهرة تتألق تحت هذه الأشعة. ألمانيا: جلوشيات متعددة الألوان وهياكل ضد النسخ، وكتابة ميكرونية موجبة وسالبة، ونسر وكتابة متألقة بالطباعة القزحية، وحبر متغير بصريًا. ممارسة صناعية عامة (غير موثقة للبطاقتين): تُطبع الخلفيات الأمنية عادةً بالأوفست على أفرخ كبيرة من خامة البطاقة، وغالبًا بالأوفست بدون ماء أو بالأحبار المجففة بالأشعة فوق البنفسجية على البلاستيك، بأحبار خاصة لا بألوان CMYK، قبل التشخيص.",
        "SP1 p.13 (rainbow), p.15 (visible microprint), p.18 (guilloche, invisible microtext, UV ink); BMI flyer #4–#7; general industry practice (labelled, not country-specific). Images: Wikimedia (EG), BMI flyer (DE).")
    return s

SLIDES = [s14, s15, s16, s17, s18, s19, s20]
