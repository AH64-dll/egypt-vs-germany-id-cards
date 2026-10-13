"""Build the concise English deck and matching static PDF on Linux or Windows.

The same measured layout produces editable PowerPoint text and vector PDF text.
Run: python deck/build/build_english.py
"""
from pathlib import Path
import csv
import json
import re

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

from animations import add_animations
from embed_fonts import embed_fonts

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
ASSETS = ROOT / "assets"
OUT.mkdir(exist_ok=True)
W, H = 13.333, 7.5
INK, PANEL, LINE = "0A0A0A", "171717", "343434"
WHITE, MUTED, ORANGE = "F5F3F0", "BDB9B5", "FF5A1F"
FONT_FILES = {"body": "Barlow-Regular.ttf", "bold": "Barlow-SemiBold.ttf", "title": "BarlowCondensed-SemiBold.ttf"}
FONT_NAMES = {"body": "Barlow", "bold": "Barlow SemiBold", "title": "Barlow Condensed SemiBold"}
for key, filename in FONT_FILES.items():
    pdfmetrics.registerFont(TTFont(key, str(ASSETS / "raw/fonts" / filename)))

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(W), Inches(H)
prs.core_properties.title = "Security Printing — National ID Card Comparison: Egypt and Germany"
prs.core_properties.author = "Kareem Waleed Wagdy"
prs.core_properties.subject = "Student code: 792400615; supervised by Rania Mohamed"
prs.core_properties.keywords = "Security Printing, Egypt, Germany, lecture summary, animated"
pdf = canvas.Canvas(str(OUT / "Egypt-vs-Germany-ID-Cards.pdf"), pagesize=(W * 72, H * 72))
pdf.setTitle(prs.core_properties.title)
pdf.setAuthor(prs.core_properties.author)
manifest = []
layout_errors = []


def rgb(value):
    return RGBColor.from_string(value)


def pdf_color(value):
    return tuple(int(value[i:i + 2], 16) / 255 for i in (0, 2, 4))


def wrap(text, width, size, font):
    result = []
    for paragraph in text.split("\n"):
        words, line = paragraph.split(), ""
        if not words:
            result.append("")
        for word in words:
            proposal = (line + " " + word).strip()
            if line and pdfmetrics.stringWidth(proposal, font, size) > width * 72 - 3:
                result.append(line)
                line = word
            else:
                line = proposal
        if line:
            result.append(line)
    return result


class Slide:
    def __init__(self, title, section, refs, notes, takeaway=None):
        self.slide = prs.slides.add_slide(prs.slide_layouts[6])
        self.n = len(prs.slides)
        self.phases = {}
        self.refs = refs
        self.title = title
        self.notes = notes
        self.takeaway = takeaway
        self.slide.background.fill.solid()
        self.slide.background.fill.fore_color.rgb = rgb(INK)
        pdf.setFillColorRGB(*pdf_color(INK))
        pdf.rect(0, 0, W * 72, H * 72, fill=1, stroke=0)
        self.box(.55, .37, .18, .045, ORANGE)
        self.tx(section.upper(), .85, .27, 10.9, .35, 11, "bold", MUTED, phase=0)
        self.tx(title, .58, .88, 12.12, 1.04, 37, "title", phase=0)
        if takeaway:
            self.box(.58, 6.37, 12.17, .43, PANEL)
            self.tx(takeaway, .77, 6.46, 11.75, .25, 12.5, "bold", ORANGE)
        self.tx("SECURITY PRINTING  /  GDM5313", .58, 7.08, 3.4, .24, 9, "bold", MUTED)
        self.tx(refs, 3.85, 7.08, 7.7, .25, 9, color=MUTED)
        self.tx(f"{self.n:02d} / 24", 11.86, 7.06, .88, .25, 10, "bold", MUTED, align="right")

    def track(self, shape, phase):
        if phase is not None:
            self.phases.setdefault(phase, []).append(shape.shape_id)
        return shape

    def box(self, x, y, w, h, fill=PANEL, phase=None, border=False):
        sh = self.slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        sh.fill.solid()
        sh.fill.fore_color.rgb = rgb(fill)
        sh.line.fill.background()
        if border:
            sh.line.color.rgb = rgb(LINE)
            sh.line.width = Pt(.7)
        pdf.setFillColorRGB(*pdf_color(fill))
        pdf.rect(x * 72, (H - y - h) * 72, w * 72, h * 72, fill=1, stroke=0)
        return self.track(sh, phase)

    def tx(self, content, x, y, w, h, size=18, font="body", color=WHITE, phase=None, align="left", url=None):
        # Barlow has no arrow glyphs; use readable words in both Office and PDF.
        content = content.replace(" → ", " to ").replace("→", "to").replace("↔", " / ")
        lines = wrap(content, w, size, font)
        line_height = size * 1.15
        if len(lines) * line_height > h * 72 + 2:
            layout_errors.append(f"s{self.n:02d}: text overflows {h:.2f}in: {content[:90]!r} ({len(lines)} lines at {size}pt)")
        shape = self.slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        frame = shape.text_frame
        frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
        frame.vertical_anchor = MSO_ANCHOR.TOP
        frame.word_wrap = True
        frame.text = "\n".join(lines)
        for p in frame.paragraphs:
            p.alignment = {"left": PP_ALIGN.LEFT, "right": PP_ALIGN.RIGHT, "center": PP_ALIGN.CENTER}[align]
            p.line_spacing = Pt(line_height)
            p.space_before = p.space_after = Pt(0)
            for run in p.runs:
                run.font.name = FONT_NAMES[font]
                run.font.size = Pt(size)
                run.font.color.rgb = rgb(color)
                if url:
                    run.hyperlink.address = url
        pdf.setFont(font, size)
        pdf.setFillColorRGB(*pdf_color(color))
        for i, line in enumerate(lines):
            px = x * 72
            width = pdfmetrics.stringWidth(line, font, size)
            if align == "right":
                px += w * 72 - width
            elif align == "center":
                px += (w * 72 - width) / 2
            pdf.drawString(px, (H - y) * 72 - size * .88 - i * line_height, line)
        if url:
            pdf.linkURL(url, (x * 72, (H - y - h) * 72, (x + w) * 72, (H - y) * 72), relative=0)
        return self.track(shape, phase)

    def pic(self, filename, x, y, w, h, phase=None):
        path = Path(filename)
        if not path.is_absolute():
            path = ASSETS / filename
        iw, ih = Image.open(path).size
        ratio = min(w / iw, h / ih)
        rw, rh = iw * ratio, ih * ratio
        xx, yy = x + (w - rw) / 2, y + (h - rh) / 2
        shape = self.slide.shapes.add_picture(str(path), Inches(xx), Inches(yy), Inches(rw), Inches(rh))
        pdf.drawImage(ImageReader(str(path)), xx * 72, (H - yy - rh) * 72, rw * 72, rh * 72, mask="auto")
        return self.track(shape, phase)

    def panel(self, x, y, w, h, title, body, phase=1, size=18, image=None):
        self.box(x, y, w, h, phase=phase)
        self.box(x, y, .045, h, ORANGE, phase=phase)
        self.tx(title, x + .22, y + .18, w - .44, .76, 22, "title", ORANGE, phase)
        top = y + (.8 if h < 2.1 else 1.03)
        if image:
            self.pic(image, x + .22, y + .9, w - .44, 1.25, phase)
            top = y + 2.33
        self.tx(body, x + .22, top, w - .44, h - (top - y) - .2, size, phase=phase)

    def rows(self, headers, rows, widths, y=2.02, row_h=.57, size=16):
        x = .58
        for header, width in zip(headers, widths):
            self.box(x, y, width, .5, "282828", phase=1)
            self.tx(header, x + .13, y + .12, width - .26, .3, 14, "bold", ORANGE, phase=1)
            x += width
        yy = y + .5
        for index, row in enumerate(rows):
            x = .58
            phase = 1 + index // max(1, (len(rows) + 2) // 3)
            for col, (value, width) in enumerate(zip(row, widths)):
                self.box(x, yy, width - .025, row_h - .03, PANEL if index % 2 == 0 else "111111", phase=phase)
                self.tx(value, x + .13, yy + .1, width - .26, row_h - .17, size,
                        "bold" if col == 0 else "body", MUTED if col == 0 else WHITE, phase)
                x += width
            yy += row_h

    def finish(self):
        add_animations(self.slide, self.phases)
        self.slide.notes_slide.notes_text_frame.text = self.notes.strip() + "\n\nSources: " + self.refs
        manifest.append({"slide": self.n, "title": self.title, "refs": self.refs,
                         "effects": sum(len(v) for v in self.phases.values()), "notes": self.notes})
        pdf.showPage()


def three(title, section, refs, notes, panels, takeaway):
    slide = Slide(title, section, refs, notes, takeaway)
    for i, (heading, body, image) in enumerate(panels):
        slide.panel(.58 + i * 4.13, 2.1, 3.9, 3.98, heading, body, i + 1, image=image,
                    size=17 if image else 18)
    slide.finish()


# 01 — The requested cover hierarchy and exact student details.
s = Slide("", "Course presentation  /  Egypt and Germany", "SP1 · SP2 · PP1 · PP2", "Prepared by Kareem Waleed Wagdy, student code 792400615, for Security Printing, under the supervision of Rania Mohamed. This English-only lecture summary compares the Egyptian card described in Security Printing Lecture 1 with the German 2024 design documented by BMI. The photographs are specimens. The 3D cover artwork is an illustration, not a manufactured or authenticated document.")
s.tx("SECURITY\nPRINTING", .58, 1.0, 6.8, 2.0, 62, "title", phase=0)
s.tx("National ID Card Comparison:\nEgypt and Germany", .63, 3.16, 6.25, 1.0, 28, "title", ORANGE, phase=1)
s.tx("Kareem Waleed Wagdy", .63, 4.53, 6.3, .45, 23, "bold", phase=2)
s.tx("Student code: 792400615\nUnder the supervision of: Rania Mohamed", .63, 5.15, 6.55, .95, 18, color=MUTED, phase=2)
s.pic("art/cover_cards.png", 7.1, 1.35, 5.8, 4.9, phase=3)
s.finish()

# 02 — Foundational ideas; avoid treating the lecture's discussion questions as definitions.
three("Easy to verify. Difficult to reproduce.", "01  /  Security printing fundamentals", "SP1 pp.3–8 · SP2 p.4", "The distinction between valuable and secure documents is a classroom discussion in SP1. Our working explanation is that value comes from money, access, legal status or rights, whereas security comes from measures that deter forgery, alteration and substitution. A document may have both. Examples in SP1 include paper and polymer banknotes; driving and weapon licences; birth, leadership, military and death certificates; identity and membership cards; transport and paid tickets; bank checks and credit cards; stamps; prepaid phone cards and entry/exit cards. Identification evolved from handwriting to analog copying to digital methods. The earlier use of glued photographs or metal pins made portrait substitution easier. Course aims include secure materials, security technologies, banknotes, cards, stamps, certificates and government papers; prepress covers digital systems, lasers, hardware and plate production.", [
    ("WHAT IS BEING PROTECTED?", "Identity, legal rights, money and access.\n\nExamples: ID cards, passports, banknotes, certificates, stamps and tickets.", None),
    ("WHAT SECURITY ADDS", "Features that resist copying, portrait substitution and data alteration.\n\nChecks must be clear enough for the intended verifier.", None),
    ("WHY DIGITAL PERSONALIZATION?", "Handwriting → analog → digital.\n\nIntegrating the photo and data into the card makes simple replacement harder.", None)], "Security works when the document and the holder can both be checked.")

# 03 — Preserve both sides of each specimen without adding fake card data.
s = Slide("Two countries. Four card faces.", "02  /  Card overview", "SP1 pp.12–19 · BMI 2024 · PAP · WM-EG", "Egyptian front/back specimen images have personal fields replaced by field labels by the Wikimedia uploader (Heshamdiab16, CC BY-SA 3.0). German specimens depict fictional holder Erika Mustermann, supplied by BMI/Personalausweisportal. Egyptian front: portrait, Arabic fields, pyramids/Sphinx, MLI and factory-number region. Egyptian back: Tutankhamun Kinegram, pharaonic scene, UV-responsive eagle, data and 2D barcode. German front: integrated colour photo, engraved data, CAN, Identigram and optically variable chip logo. Back: variable laser image, security thread, embossed map, eID logo, address and machine-readable zone. Images show card appearance; ordinary-light pictures cannot demonstrate UV fluorescence or angle-dependent behaviour.", "Read the layout first; authenticate with several independent features.")
for col, (country, front, back) in enumerate([("EGYPT", "eg_front.png", "eg_back.png"), ("GERMANY", "de_front.png", "de_back.png")]):
    x = .7 + col * 6.24
    s.tx(country, x, 1.91, 5.55, .43, 25, "title", ORANGE, phase=col + 1)
    for row, filename in enumerate([front, back]):
        s.pic("processed/" + filename, x, 2.5 + row * 1.7, 3.0, 1.65, phase=col + 1)
        description = ("Front: portrait, data and security background" if row == 0 else "Back: security elements and machine-readable data")
        s.tx(description, x + 3.22, 2.7 + row * 1.7, 2.26, 1.3, 18, phase=col + 1)
s.finish()

# 04 — General card anatomy is explicitly separated from country-specific claims.
s = Slide("A secure document is built in four stages", "03  /  Document structure", "SP2 pp.5–11", "Lecture life-cycle model: card body → print → personalize → finishing. The card body can be paper or polymer; substrate security may include watermarks, security strips and fluorescent fibres, depending on document type. General lecture diagrams show overlays, holographic laminates, colour images (300 dpi), UV images, monochrome printing, barcode/QR, magnetic stripes, contact chips, proximity/MIFARE, PET print layers and prelaminated antennas. These are options across card systems, not claims that all are present in either national card. A clear or holographic overlaminate may be local or full-surface; finishing is sometimes unnecessary. HDP/retransfer film, clear PVC, lithographic/digital PET and antenna prelaminate are examples from the general diagrams. The 3D layer rendering is conceptual: neither card's exact internal stack is established by this illustration.", "Security belongs in the substrate, printed design, personal data and protective finish.")
s.pic("art/exploded.png", .65, 2.0, 5.2, 4.15, phase=1)
for i, (heading, body) in enumerate([
    ("01  CARD BODY", "Paper or polymer; security built into the substrate."),
    ("02  PRINT", "Fixed backgrounds, fine lines, microtext and special inks."),
    ("03  PERSONALIZE", "Holder-specific portrait, data and machine-readable information."),
    ("04  FINISHING", "Optional clear or holographic protection against wear and tampering.")]):
    y = 2.13 + i * .99
    s.tx(heading, 6.1, y, 6.3, .34, 20, "title", ORANGE, phase=2 if i < 2 else 3)
    s.tx(body, 6.1, y + .4, 6.1, .55, 18, phase=2 if i < 2 else 3)
s.finish()

# 05 — Four selection criteria, with cost contextualised instead of ranked by invented scores.
s = Slide("Choose personalization for the document's lifetime", "04  /  Selection criteria", "SP2 pp.13–17", "SP2 names four criteria: security capacity, durability, quality and cost. Personalization must add protection instead of weakening an otherwise secure blank. Data and portraits must stay legible throughout the card's service life, with all elements remaining equally durable. Image/text quality should remove ambiguity during verification because secure documents convey civil or financial rights. Cost matters more for short-life tickets; for IDs, passports and financially important cards it is secondary to security, durability and quality. No country-specific cost, throughput or quality score is publicly established here.", "A cheap print method is unsuitable if its data wears out before the card expires.")
for i, (heading, body) in enumerate([
    ("SECURITY CAPACITY", "Does the method make copying or altering the holder's data harder?"),
    ("DURABILITY", "Will portrait, text and security elements survive the full service life?"),
    ("QUALITY", "Can a verifier read the data and recognize the holder without ambiguity?"),
    ("COST", "Balance production cost against the legal, financial and national-security value.")]):
    s.panel(.58 + (i % 2) * 6.2, 2.02 + (i // 2) * 2.03, 5.97, 1.87, heading, body,
            phase=1 + i // 2, size=18)
s.finish()

# 06 — Card substrates and standards; do not assert an Egyptian polymer.
s = Slide("Materials determine durability and security", "05  /  Card materials", "SP2 pp.18–26 · ISO/IEC 7810 · BDR", "SP2 describes the move from secure paper toward plastic materials beginning in the 1970s. PVC is the least expensive card plastic in the lecture and is common in telecom/contactless cards; lower resistance to heat, load, bending and UV can produce delamination, erosion or partial damage, with a generic 3–5-year expected lifespan. Modified polyester materials are labelled PETG and PETF in the lecture; preserve this terminology as lecture wording rather than equating all polyester grades. Composite structures combine different materials to balance durability, security and affordability. Polycarbonate supports several print methods and optically variable elements, but the lecture warns of brittleness, cracking and surface damage. Fused polycarbonate layers and internal laser marking are industry explanations, not a disclosed Egyptian recipe. Germany's polycarbonate is documented by Bundesdruckerei; the exact Egyptian polymer is not established in the supplied lecture. ISO/IEC 7810 nominal sizes: ID-000 25×15 mm, ID-1 85.60×53.98 mm, ID-2 105×74 mm, ID-3 125×88 mm. The lecture labels the smallest format ID-0 and has an inconsistent ID-2 height range; use standard nominal values. Typical ID-1 thickness is 0.76 mm; this is a format specification, not a measured Egyptian thickness.", "German polycarbonate is documented; the Egyptian card's precise polymer is not specified.")
s.rows(["MATERIAL", "LECTURE SUMMARY", "KEY TRADE-OFF"], [
    ("PVC", "Low cost; telecom/contactless cards", "Lower heat, bending and UV resistance"),
    ("Polyester", "Modified PETG / PETF (lecture terms)", "Improved bend, heat and solvent resistance"),
    ("Composite", "Two or more materials in one structure", "Balance properties and affordability"),
    ("Polycarbonate", "Multiple print methods; accepts OVDs", "Durable design, but cracking can occur")], [2.13, 4.99, 5.05], row_h=.72, size=17)
s.tx("ID-1 standard: 85.60 × 53.98 mm; nominal thickness 0.76 mm", .78, 5.65, 11.6, .4, 19, "bold", ORANGE, phase=3)
s.finish()

# 07 — Prepress essentials.
three("Prepress turns a design into a printable master", "06  /  Prepress technologies", "PP1 pp.3–9 · PP2 pp.6–7, 30", "Printing transfers ink, toner or other material to a substrate to produce physical content. Gutenberg is the historical milestone highlighted in PP1; modern methods include inkjet, laser, offset, flexography and 3D printing. The full workflow is originals → reproduction preparation → film or digital imaging → platemaking → press → finishing. Premedia prepares text/images for multiple publication media; prepress ends at the ready-for-print master. Conventional prepress assembles individual films mechanically; digital prepress processes pages electronically and uses computer-to-film (CTF) or computer-to-plate (CTP) output. CMYK separations shown in PP2 convert an RGB source to cyan, magenta, yellow and black print channels. Additional colour management, effective image resolution, fine-line integrity and registration checks are general production practice. No exact Egyptian or German production press is established by these teaching diagrams.", [
    ("PREPRESS / PREMEDIA", "Prepare text, images and graphics.\n\nCheck resolution, colour separation and registration before producing the master.", None),
    ("CONVENTIONAL vs DIGITAL", "Conventional: assemble film manually.\n\nDigital: electronic page preparation → CTF or CTP plate imaging.", None),
    ("PRESS → POST-PRESS", "Print the fixed design, then finish the product.\n\nCard application: accurate fine lines and layers support later personalization.", None)], "A security design only works if prepress preserves its fine detail.")

# 08 — Mechanism and production trade-offs.
s = Slide("Offset lithography: plate → blanket → substrate", "07  /  Printing technology", "PP1 pp.10–25 · PP2 p.11", "Conventional offset is indirect lithography: water wets hydrophilic non-image regions while oil-based ink adheres to image regions. The plate transfers ink to a rubber blanket; the blanket prints onto a substrate supported by the impression cylinder. The plate does not touch the final stock, reducing plate wear; rubber conforms to surface irregularities. Sheet-fed handles individual sheets; web-fed uses continuous rolls subsequently cut and finished, generally suited to high-volume production. PP1 gives illustrative sheet-fed speeds of 12,000–24,000 sheets/hour; these are teaching examples and machine-dependent. Web-speed figures in PP1 mix incompatible units, so they are omitted instead of treated as precise specifications. Advantages: consistent sharp images, colour accuracy, substrate versatility and economical large runs. Limits: plate setup time/cost, less economical small runs, inefficient per-holder changes, and chemical/environmental handling needs. Security-card backgrounds can use offset in general industry practice, often waterless/UV-curing on plastics; the specific production route of these two national cards is not established here.", "Use fixed-design printing for repeatable backgrounds; add variable holder data separately.")
for i, (heading, body) in enumerate([
    ("1  IMAGE PLATE", "Image areas accept ink; wet non-image areas repel it."),
    ("2  RUBBER BLANKET", "Receives the image from the plate; makes the transfer indirect."),
    ("3  SUBSTRATE", "Prints against an impression cylinder; the plate never touches the stock.")]):
    s.panel(.58 + i * 4.13, 2.02, 3.9, 1.92, heading, body, i + 1, size=17)
s.tx("SHEET-FED", .78, 4.22, 3.7, .4, 23, "title", ORANGE, phase=2)
s.tx("Individual sheets; flexible jobs and moderate quantities.", .78, 4.73, 3.7, 1.0, 18, phase=2)
s.tx("WEB-FED", 4.91, 4.22, 3.7, .4, 23, "title", ORANGE, phase=2)
s.tx("Continuous rolls; efficient for high-volume publications.", 4.91, 4.73, 3.7, 1.0, 18, phase=2)
s.tx("THE TRADE-OFF", 9.04, 4.22, 3.5, .4, 23, "title", ORANGE, phase=3)
s.tx("Consistent quality at scale; setup cost and limited customization.", 9.04, 4.73, 3.5, 1.0, 18, phase=3)
s.finish()

# 09 — Distinguish printing plate substrates from card-body materials.
s = Slide("Printing plates: wet or waterless?", "08  /  Lithographic plates", "PP2 pp.8–21, 28", "These are printing-plate materials, not the finished card-body polymers. Conventional plates use a dampening/fountain solution to keep non-image areas ink-free. Waterless plates use ink-repelling silicone and do not use a dampening solution. Grained aluminium provides long run durability; SP2's lecture examples indicate 100,000–2,000,000+ impressions, depending on plate and operating conditions. Coatings may be silver-halide or photopolymer. Polyester plates are cheaper, generally for 25,000 or fewer impressions; red/IR laser imaging, toner/heat or photosensitive technologies depend on plate type. Lecture thickness: polyester 0.004–0.012 inches; cellulose paper plates 0.004–0.008 inches. Paper plates are chemically treated, not grained, and used for small presses/runs with toner-based recording. The CTP diagram shows an infrared-sensitive layer, UV-ink-resistant layer, hydrophilic layer, multi-grain layer and aluminium support; another plate illustration shows protective/photosensitive layers over aluminium. These are examples, not universal plate recipes.", "Choose the plate for run length, registration, coating and imaging compatibility.")
s.panel(.58, 2.0, 5.97, 1.58, "CONVENTIONAL / WET", "Dampening solution keeps the non-image areas free of ink.", 1, size=18)
s.panel(6.78, 2.0, 5.97, 1.58, "WATERLESS", "An ink-repelling silicone layer replaces the dampening solution.", 2, size=18)
s.rows(["PLATE SUBSTRATE", "RUN LENGTH (LECTURE)", "MAIN USE / PROPERTY"], [
    ("Metal / aluminium", "100,000–2,000,000+ impressions", "Long life; grained, photosensitive surface"),
    ("Polyester", "Typically 25,000 or fewer", "Lower cost; compatible laser imaging"),
    ("Paper / cellulose", "Small runs", "Chemically treated; toner recording")], [2.5, 4.1, 5.57], y=3.89, row_h=.62, size=16)
s.finish()

# 10 — All plate preparation stages, calibration and safety summarized on one slide.
three("Plate preparation: control every stage", "09  /  Preparation and safety", "PP2 pp.22–34", "Traditional plate preparation comprises photolithography, chemical treatment, perforating/punching and edge bending. Exposure: film must contact the plate in the correct position; clean exposure glass, maintain vacuum/suction and light intensity, and calibrate exposure time because it affects point/dot size. Manual or automated development is possible. Control developer temperature and replenishment, wash water and gum supply/viscosity. Chemical steps: develop → wash → gum → dry (the lecture's English 'gluing' is conventionally called gumming). Punching enables stable film placement, colour registration and proper cylinder alignment; edge bending lets clamps/pins secure the plate on press. Automated CTP diagrams show autoloader, imaging, processor and stacker; automation still needs calibration. Plate-room safety in the lecture: ventilation, gloves, protect eyes, maintain 18–22°C and provide first aid. CMYK separation and registration preserve fine security lines. The exact production settings of either national ID are not disclosed.", [
    ("EXPOSE & DEVELOP", "Clean glass; correct film contact and vacuum.\n\nCalibrate light and exposure time.\n\nDevelop → wash → gum → dry.", None),
    ("REGISTER & MOUNT", "Control temperature and chemical replenishment.\n\nPunch for alignment.\n\nBend edges for secure cylinder mounting.", None),
    ("SAFE WORKING CONDITIONS", "Ventilation, gloves and eye protection.\n\nLecture room range: 18–22°C.\n\nFirst-aid supplies must be available.", None)], "Poor exposure or registration can destroy the detail that makes a design verifiable.")

# 11 — Shared security-printing concepts, illustrated with existing macros.
three("Security backgrounds carry more than decoration", "10  /  Printed security features", "SP1 pp.13, 18 · BMI 2024 #4, #6, #7", "Guilloche consists of intricate fine-line patterns. SP1 describes precise designs prepared in specialist software and tells verifiers to distinguish continuous fine lines from a crude dot-based reproduction under magnification. Its 'sold only to governments' phrasing is the lecture's statement, not a claim that every guilloche tool is legally restricted. Rainbow/iris printing gives a continuous colour gradient; Germany's official flyer explicitly describes rainbow UV eagle/lettering. Positive microtext uses small printed characters; negative microtext uses characters reversed out of ink. A magnifier helps assess legibility and line quality. Egyptian 'Relief' refers to the lecture's security design printing the word 'Egypt' across the back; this is not proof of intaglio, physical embossing or a particular relief-printing press. The macros here are illustrative specimen crops and do not show every feature under its actual inspection condition.", [
    ("GUILLOCHE", "Complex fine lines resist simple copying.\n\nLook for line continuity and clean intersections.", "processed/de_m_guilloche1.png"),
    ("RAINBOW / IRIS", "A continuous colour gradient makes crude colour reproduction easier to spot.", "processed/eg_m_rainbow_bg.png"),
    ("MICROTEXT", "Tiny, readable lettering; Germany also uses positive and negative microprint.", "processed/de_m_microprint.png")], "A feature should be checked in the right lighting and at the right magnification.")

# 12 — Egyptian public-level checks.
three("Egypt: visible and angle-dependent security", "11  /  Egyptian card — public checks", "SP1 pp.11–13 · WM-EG", "SP1 divides the card's features into four examination levels: public external features; specialist external features; hidden features examined by specialists using simple tools; laboratory checks at the card production centre. At public level, the Multi Laser Image below the portrait can be felt and changes the visibility of date of birth and national emblem with viewing angle. The Tutankhamun Kinegram on the reverse changes appearance in horizontal/vertical viewing directions. The lecture spells this 'Kingram'; use Kinegram as the product spelling. Rainbow printing and the repeated 'Egypt' relief design are also discussed. The MLI crop is from a lecture image with holder data masked; the other images are specimen details. Static crops show location and artwork; the presentation's entrance animation is not a simulation or proof of the optical feature itself.", [
    ("MULTI LASER IMAGE", "Below the portrait.\n\nTilt: birth date / emblem.\nTouch: felt by fingers.", "processed/eg_m_mli_lecture.png"),
    ("TUTANKHAMUN KINEGRAM", "Reverse-side optical element.\n\nChange the viewing direction to see a different appearance.", "processed/eg_m_kinegram.png"),
    ("PRINTED DESIGN", "Rainbow background and repeated “Egypt” relief design.\n\nInspect the detail, not just the motif.", "processed/eg_m_back_texture.png")], "The lecture describes four levels of verification; everyday checks are only the first.")

# 13 — Remaining Egyptian security levels.
three("Egypt: specialist, hidden and laboratory features", "12  /  Egyptian card — deeper checks", "SP1 pp.14–18", "Specialist external features in SP1: factory number derived from a secret equation, unique to the card and recorded against the holder in the national ID database; visible microprint in the lower front reads 'Ministry of Interior – Civil Status Sector'; and the encrypted 2D barcode on the reverse. Microprint can be read using a simple magnifier (the illustrated list states 5×). Hidden/tool-based features include invisible UV microtext with the same ministry wording, guilloche line quality under magnification, and visible ink that fluoresces under UV, such as the eagle on the back. Laboratory categories are material-related marks, intentional printing errors in confidential design areas and filter-only writing. Their confidential details are not given; listing these categories does not enable an actual laboratory authentication. Database and barcode checks require the appropriate authorized systems. Neither a visually plausible number nor a successful generic scan proves authenticity.", [
    ("02  SPECIALISTS", "Factory number: database-linked.\n\nVisible microprint: magnifier.\n\n2D barcode: compare decoded and printed data.", None),
    ("03  SPECIALISTS + TOOLS", "Invisible microtext under UV.\n\nUV-glowing eagle.\n\nGuilloche line quality under magnification.", None),
    ("04  LABORATORY", "Material-related marks.\n\nConfidential intentional print errors.\n\nText visible through specific filters.", None)], "A specimen photograph cannot establish UV response, database validity or laboratory authenticity.")

# 14 — Egyptian personalization and what is not known.
s = Slide("Egypt: link the printed card to one holder", "13  /  Egyptian personalization", "SP1 pp.13–15 · WIKI-EG (secondary)", "The lecture documents the portrait, holder data, MLI, unique factory number and encrypted reverse-side 2D barcode. The factory number is associated with the holder in the national ID database and checked there; barcode data can be decoded for comparison with visible data and electronic transfer to beneficiary systems. The 14-digit national number and PDF417 barcode format come from secondary background research, not a newly verified official manufacturing specification. We omit the digit-generation algorithm because it is unnecessary for this summary. The exact photo/text personalization process and precise card polymer are not stated by the supplied lectures; no laser, thermal or inkjet method is asserted for the Egyptian card. Chip technology, agency applications and biometrics appear in the future vision section of SP1 and must not be presented as deployed features.", "A machine-readable code supports consistency checks; it does not authenticate a card by itself.")
s.pic("processed/eg_front.png", .7, 2.17, 5.14, 3.17, phase=1)
s.tx("Portrait + holder data + national number", .85, 5.56, 4.9, .65, 20, "title", ORANGE, phase=1)
s.panel(6.15, 2.05, 6.6, 1.91, "FACTORY NUMBER", "Unique card identifier linked to the holder in the national ID database.", 2, size=19)
s.panel(6.15, 4.16, 6.6, 1.91, "ENCRYPTED 2D BARCODE", "Compare encoded data with readable fields. Exact print process is not specified in the lecture.", 3, size=19)
s.finish()

# 15 — Additional official German facts.
three("Germany: secure body and integrated personalization", "14  /  German card — manufacture", "BMI 2024 #1, #2 · PAP · BDR", "The comparison refers to the German ID card design documented in the May 2024 BMI flyer, introduced on 2 May 2024; the doctoral-degree field moved to the reverse. The chip-card system began in November 2010. Bundesdruckerei documents polycarbonate for German eID cards. The official portal describes several plastic layers and protective lacquer. In general polycarbonate manufacture, fused layers and internal marking help reveal attempts to separate or replace data, but exact layer recipes are not disclosed here. BMI #1: colour photograph and document number are securely integrated with inkjet technology; all other personal data are high-contrast laser engraving on front/back. BMI #2: the expiry date and six-digit card access number (CAN) are engraved so they can be felt. CAN is a card-access number, not the holder's secret eID PIN. The face is also represented in a holographic portrait and the variable laser image. Source-specific facts are kept separate from industry explanations.", [
    ("POLYCARBONATE BODY", "Multi-layer polymer structure with a protective surface finish.\n\nMaterial choice supports durable embedded data.", None),
    ("INKJET + LASER", "Colour photo and document number: integrated inkjet.\n\nOther personal data: high-contrast laser engraving.", "processed/de_m_photo.png"),
    ("TACTILE DATA", "Laser-engraved expiry date and six-digit CAN can be felt.\n\nCAN is different from the eID PIN.", "processed/de_m_tactile_can.png")], "The German print methods are documented; the Egyptian methods remain unspecified.")

# 16 — Optical effects.
three("Germany: optical and tactile features", "15  /  German card — public checks", "BMI 2024 #3, #5, #8, #9", "Identigram: the holder's holographic image appears green, the three-dimensional federal eagle red, with kinematic structures; additional design elements appear blue after a 90° card rotation. Optically variable ink in the ICAO 'chip inside' logo changes green/blue depending on viewing and illumination angle. The variable laser image shows either expiry date or portrait when tilted. Surface embossing on the reverse includes microprinting and a map of Germany; expiry/CAN are separate tactile engraved data. These are distinct technologies: colour-shifting ink, holographic/diffractive structure, angle-selective laser image and physical surface texture should not be conflated. The static macro pictures locate features; real optical verification needs an actual card.", [
    ("IDENTIGRAM", "Tilt: green portrait and red 3D eagle.\n\nRotate 90°: additional blue elements.", "processed/de_m_identigram_d.png"),
    ("COLOUR-SHIFTING INK", "Tilt the chip logo: green ↔ blue.\n\nCheck the change, not just the printed colour.", "processed/de_m_ovi_logo.png"),
    ("LASER IMAGE + EMBOSSING", "Tilt: portrait / expiry date.\n\nTouch: embossed map and microprint on the reverse.", "processed/de_m_cli_portrait.png")], "Combine tilt and touch checks; one visible logo cannot establish authenticity.")

# 17 — Additional German hidden and electronic features.
three("Germany: UV, embedded features and electronic ID", "16  /  German card — tools and chip", "BMI 2024 #4, #10–13 · PAP", "BMI #4: UV reveals the federal eagle and multi-coloured luminescent lettering, both made using rainbow/iris printing. BMI #10: transparent fibres in the reverse luminesce under UV. #11: machine-verifiable embedded thread personalized with document number and name/given names. #12: address changes can be shown on a label, possibly protected by transparent foil; some labels use a 2D barcode checked by smartphone app instead of a stamp. #13: the eID logo indicates supported electronic-ID functionality. The contactless chip stores a facial image and two fingerprints, accessed by authorized officials; an eID workflow uses the holder's PIN for online identification with government or business. The public portal dates mandatory fingerprint enrolment to 2 August 2021, with applicable statutory exceptions. Iris biometrics are not described in these sources. The printed MRZ is a machine-readable representation, not the chip. Barcode, MRZ and authenticated chip reading are different kinds of checks. The flyer lists visual, magnifier, touch, tilt, overhead light, oblique light, UV and app verification methods.", [
    ("UV PRINT + FIBRES", "Rainbow UV eagle and lettering.\n\nTransparent security fibres fluoresce on the reverse.", "processed/de_m_uv_eagle.png"),
    ("SECURITY THREAD", "Embedded and machine-verifiable.\n\nPersonalized with name and document number.", "processed/de_m_thread.png"),
    ("CONTACTLESS CHIP / eID", "Facial image + two fingerprints for authorized checks.\n\nOnline identification uses an eID PIN.", "processed/de_m_eid_logo.png")], "Printed security and authenticated electronic checks protect different parts of identity.")

# 18 — Operational comparison, condensed without downgrading lab/database requirements.
s = Slide("Verification: use the right check for each feature", "17  /  Verification comparison", "SP1 pp.11–18 · BMI 2024 · PAP", "This comparison uses SP1's verification logic and the German flyer, not a numerical country ranking. Public: visual inspection, tilt and touch. Specialist: detailed design/microtext examination. Tools: magnifier, UV lamp, barcode reader and electronic systems, depending on the feature. Laboratory: confidential material/design checks. Some lecture categories overlap because a specialist-visible feature may still require a reader or a database. Germany's guide additionally specifies light from above, oblique light and app verification, particularly for address-label codes. Database access for the Egyptian factory number and authorized chip verification are not replaced by visual checks. A mismatch or missing feature requires a proper examination rather than an instant authenticity judgment from a photo.", "Cross-check appearance, holder data and machine-readable information; no single feature is decisive.")
s.rows(["CHECK", "EGYPT (LECTURE)", "GERMANY (BMI GUIDE)"], [
    ("Tilt", "MLI; Tutankhamun Kinegram", "Identigram; OVI logo; variable laser image"),
    ("Touch", "Multi Laser Image", "Expiry / CAN; surface embossing"),
    ("Magnify", "Microprint; guilloche line quality", "Positive / negative microprint; guilloches"),
    ("UV light", "Invisible microtext; UV-glowing eagle", "Rainbow UV print; luminescent fibres"),
    ("Reader / system", "2D barcode; factory-number database", "MRZ; authorized chip / eID checks"),
    ("Laboratory", "Material marks; errors; filter-only text", "Confidential checks not detailed in flyer")], [2.01, 4.96, 5.2], row_h=.61, size=16)
s.finish()

# 19 — Required characteristics and design comparison.
s = Slide("Comparison table: characteristics and design", "18  /  Lecture assignment", "SP1 · SP2 · BMI 2024 · PAP · BDR · PAuswG §6 · WIKI-EG", "SP2's assignment explicitly asks for a table comparing security features, characteristics and design. Egyptian issuer: Ministry of Interior, Civil Status Sector. German card is issued through competent identity-card authorities and produced by Bundesdruckerei; BMI supplies the national framework/design information. Germany: ID-1, multi-layer polycarbonate with protective lacquer, ten-year validity or six years if issued before age 24 under PAuswG §6. The Egyptian seven-year validity is secondary background from WIKI-EG; the lecture does not publish the precise polymer or dimensions. Both specimens have credit-card-like proportions; do not turn this observation into an official Egyptian standard declaration. Egyptian visible specimen motifs include pyramids/Sphinx, a pharaonic relief, Tutankhamun and an eagle. German motifs include federal eagle, Brandenburg Gate, EU flag/DE and embossed country map. Labels are Arabic on the Egyptian specimen and German/English/French on the German card. German three portrait representations are the inkjet image, holographic portrait and variable laser image; Egypt's MLI displays birth date/emblem, not a second portrait.", "Design communicates national identity while supporting data organization and verification.")
s.rows(["CHARACTERISTIC", "EGYPT", "GERMANY"], [
    ("Body / format", "Plastic; exact polymer not stated", "Polycarbonate; ID-1 card format"),
    ("Validity", "7 years (secondary source)", "10 years; 6 if issued before age 24"),
    ("Field labels", "Arabic", "German, English and French"),
    ("National motifs", "Pyramids, Sphinx, Tutankhamun, eagle", "Federal eagle, Brandenburg Gate, EU flag"),
    ("Portraits", "Main photo; MLI shows date / emblem", "Photo, holographic portrait, laser image"),
    ("Machine-readable", "Encrypted 2D barcode", "MRZ and contactless chip")], [2.36, 4.77, 5.04], row_h=.61, size=16)
s.finish()

# 20 — Security comparison in a readable dedicated table.
s = Slide("Comparison table: security and personalization", "19  /  Lecture assignment", "SP1 pp.12–18 · BMI 2024 · PAP", "Both cards combine fine security printing with optical effects and machine-readable data, but the documented scope is different. The Egyptian lecture documents MLI, Kinegram, guilloche, rainbow printing, repeated 'Egypt' relief, visible/invisible microtext, UV eagle, unique factory number, encrypted barcode and laboratory categories. The German flyer documents multicolour guilloches/anti-copy patterns, positive/negative microtext, Identigram, OVI logo, variable laser image, tactile engraved data, surface embossing, rainbow UV features, fibres, personalized thread and a contactless eID chip. German inkjet and laser processes are explicitly documented, whereas Egypt's personalization technology and polymer are not established here. Biometrics and chip applications appear only as future proposals in the Egyptian lecture. This is a comparison of the supplied evidence, not proof that every unlisted feature is absent from an actual card.", "Use “not specified” when the source does not establish a manufacturing or security claim.")
s.rows(["FEATURE", "EGYPT", "GERMANY"], [
    ("Security print", "Guilloche; rainbow; “Egypt” relief", "Guilloche; anti-copy; ± microprint"),
    ("Optical effects", "Kinegram; Multi Laser Image", "Identigram; OVI; variable laser image"),
    ("UV", "Invisible microtext; glowing eagle", "Rainbow eagle / text; security fibres"),
    ("Personalization", "Exact method not specified", "Integrated inkjet + laser engraving"),
    ("Embedded data", "Barcode + database-linked factory no.", "Personalized thread + contactless chip"),
    ("Biometrics / eID", "Future vision in the lecture", "Face + fingerprints; PIN-based eID")], [2.36, 4.77, 5.04], row_h=.61, size=16)
s.finish()

# 21 — Every future-vision item, with comparisons rather than implied implementation.
s = Slide("Egypt's future vision vs Germany's documented features", "20  /  Development roadmap", "SP1 pp.20–21 · BMI 2024 · PAP", "Every item below is a future proposal in SP1, not evidence that it is already deployed on the Egyptian card. Proposed fluorescent UV rainbow effect has a documented counterpart in Germany's rainbow UV eagle and lettering. Embedded transparent hologram/Kinegram has a comparable purpose to the German Identigram, but is not the same construction. Tactile cold-laser factory number has a comparable tactile-data objective to Germany's engraved expiry/CAN, not an identical method or field. IR-reactive ink is not described by the public German flyer; no claim of absence is made. Contactless smart-card technology corresponds to Germany's contactless chip. Integrating health, social security and social-insurance services is a proposed multi-agency application scope; German eID supports digital services, but that is not proof the same health/social data is stored on the card. Proposed biometrics include fingerprints, iris and facial recognition; Germany's flyer documents facial image and two fingerprints, not iris. The comparison describes functional parallels and evidence limitations.", "A lecture roadmap is a proposal; similar goals do not mean identical technology.")
s.rows(["EGYPT: PROPOSED IN SP1", "GERMANY: PUBLICLY DOCUMENTED"], [
    ("UV rainbow effect", "Rainbow UV eagle and multicolour lettering"),
    ("Embedded transparent hologram / Kinegram", "Comparable purpose: Identigram optical security"),
    ("Tactile cold-laser factory number", "Comparable purpose: tactile expiry date and CAN"),
    ("IR-reactive ink", "Not specified in the public BMI guide"),
    ("Contactless smart-card technology", "Contactless chip and online eID"),
    ("Health / social-service applications", "Digital-service identification; different application scope"),
    ("Fingerprints, iris and face", "Facial image + two fingerprints; iris not listed")], [6.0, 6.17], row_h=.52, size=15.5)
s.finish()

# 22 — Finishing and durability in context.
three("Finishing must protect data without hiding the checks", "21  /  Protection and durability", "SP2 pp.11, 15, 21, 24–26 · PAP · BMI 2024 #12", "SP2 states that transparent panels may be optional and may be local or full-surface, clear or optically variable. Their purpose is to protect holder data against damage/tampering, similar to lamination. Card-body, print, personalized image/data and finish should all endure for the intended service life. PVC delamination and PC brittleness/cracking illustrate why substrate selection and mechanical durability matter; these are lecture-level material trade-offs, not measurements of either national card. Germany's portal documents protective lacquer, and the BMI flyer describes optional transparent protection on address-change labels. Specific abrasion, heat, bending and solvent tests are general engineering evaluation examples; no private acceptance criteria are inferred. Do not cover security elements with a finish that makes legitimate public/tool verification impractical.", [
    ("PROTECT", "Local or full-surface clear / optical protection can deter data tampering and reduce wear.", None),
    ("PRESERVE VERIFIABILITY", "Keep portraits and text legible.\n\nOptical, tactile and UV checks must still work after finishing.", None),
    ("MATCH THE SERVICE LIFE", "Inspect for cracking, surface wear, bending damage and layer separation.\n\nEvery layer must remain usable.", None)], "Durability is part of security because damaged data becomes difficult to verify.")

# 23 — Answer the assignment without a fabricated winner or feature-count ranking.
three("Three conclusions from the lecture comparison", "22  /  Key findings", "SP1 · SP2 · PP1 · PP2 · BMI 2024 · PAP", "The comparison is grounded in all four supplied lectures and strengthened by official German evidence. First, security is layered: substrate, printed design, personalization and finishing work together. Second, a feature is only useful when a verifier can test it, so public, specialist, tool-assisted and laboratory checks need different information and access. Third, the German sources establish polycarbonate, integrated inkjet, laser engraving and a contactless biometric/eID chip; the Egyptian lecture establishes optical/printed features, barcode and a database-linked factory number, while chip applications and biometrics appear as future proposals. These differences in published evidence do not justify unsupported cost/performance scores or a simplistic winner. The SP1 assignment asks for a 3D sample based on field/survey study; the cover/layer art supports illustration, but is not a completed physical sample or a field study. The SP2 comparison-table requirement is answered on slides 19–20.", [
    ("1  SECURITY IS LAYERED", "Body + print + personalized data + finish.\n\nPrepress accuracy supports the final security design.", None),
    ("2  VERIFY THE FEATURE", "Use tilt, touch, magnification, UV and authorized systems.\n\nCheck several independent features together.", None),
    ("3  RESPECT THE EVIDENCE", "Germany's chip and print methods are documented.\n\nEgypt's future proposals must stay separate from lecture-described features.", None)], "Easy to verify. Difficult to reproduce. Durable for the document's lifetime.")

# 24 — Readable references with real hyperlinks and full URLs in the notes.
s = Slide("Sources and image credits", "23  /  References", "Full claim register and lecture map: deck/research/", "Primary academic sources: SP1 Security Printing Lecture 1 (23 pages); SP2 Security Printing Lecture 2 (27 pages); PP1 Prepress Technologies Lecture 1 (27 pages); PP2 Prepress Technologies Lecture 2 (35 pages), all by Rania Mohamed, 2026/27. Official German flyer (May 2024): https://bern.diplo.de/blob/2668104/e18dadad82d6bc712f8bc35fbd9dcc02/flyer-personalausweis-data.pdf . German portal: https://www.personalausweisportal.de/Webs/PA/EN/citizens/german-id-card/german-id-card-node.html . Manufacturer: https://www.bundesdruckerei.de/en/german-id-card-with-online-id-functionality . Validity law: https://www.gesetze-im-internet.de/pauswg/__6.html . Standard: ISO/IEC 7810:2019. Secondary Egyptian background: https://en.wikipedia.org/wiki/Egyptian_National_Identity_Card . Egyptian specimen: https://commons.wikimedia.org/wiki/File:Egyptian_ID_Card.jpg , Heshamdiab16, CC BY-SA 3.0, fields already replaced with labels by uploader; adapted crops retain this attribution. Licence: https://creativecommons.org/licenses/by-sa/3.0/ . German specimens/macros: BMI/Personalausweisportal, image credit BKA and Bundesdruckerei. Masked MLI crop: SP1. Other 3D artwork and diagrams: original assets retained from the repository. Official German flyer is included in the repository. Additional facts are attributed on slides and in notes. PDF is a static reading copy; animation runs in the PPTX slideshow.", "Kareem Waleed Wagdy  ·  792400615  ·  Under the supervision of Rania Mohamed")
s.panel(.58, 2.02, 5.97, 3.98, "PRIMARY COURSE MATERIAL", "SP1  Security Printing — Lecture 1\nSP2  Security Printing — Lecture 2\nPP1  Prepress Technologies — Lecture 1\nPP2  Prepress Technologies — Lecture 2\n\nAll four lectures: Rania Mohamed.\n112 pages condensed into 24 slides.", 1, size=17)
s.box(6.78, 2.02, 5.97, 3.98, phase=2)
s.tx("ADDITIONAL SOURCES & IMAGES", 7.0, 2.22, 5.5, .55, 22, "title", ORANGE, phase=2)
links = [
    ("BMI: German ID security features, May 2024", "https://bern.diplo.de/blob/2668104/e18dadad82d6bc712f8bc35fbd9dcc02/flyer-personalausweis-data.pdf"),
    ("Personalausweisportal; Bundesdruckerei", "https://www.personalausweisportal.de/Webs/PA/EN/citizens/german-id-card/german-id-card-node.html"),
    ("PAuswG §6; ISO/IEC 7810 card format", "https://www.gesetze-im-internet.de/pauswg/__6.html"),
    ("Egyptian validity: Wikipedia (secondary)", "https://en.wikipedia.org/wiki/Egyptian_National_Identity_Card"),
    ("Egyptian specimen: Heshamdiab16, CC BY-SA 3.0", "https://commons.wikimedia.org/wiki/File:Egyptian_ID_Card.jpg")]
for i, (label, url) in enumerate(links):
    s.tx(label, 7.0, 3.05 + i * .43, 5.5, .4, 15.5, phase=2, url=url)
s.tx("German images: © BKA / Bundesdruckerei.\nLecture crop: masked. 3D art: repository originals.", 7.0, 5.4, 5.5, .5, 12, color=MUTED, phase=3)
s.finish()

assert len(prs.slides) == 24
# Secondary examples from lecture diagrams belong in the notes, not crowded slides.
for number, extra in {
    3: "Card anatomy overview based on the SP1 p.19 labelled feature map.",
    7: "Printed products include books, packaging, labels, stamps, securities and credit/check cards. The relief principle diagram illustrates transfer from raised inked image areas, unlike planographic offset.",
    9: "File preparation precedes plate preparation; imaging and registration must match the intended output.",
    15: "SP1 p.22 includes a Veridos video: the Giesecke+Devrient / Bundesdruckerei joint venture is an additional industry example, not evidence of the Egyptian card's supplier.",
}.items():
    manifest[number - 1]["notes"] += " " + extra
    prs.slides[number - 1].notes_slide.notes_text_frame.text = manifest[number - 1]["notes"] + "\n\nSources: " + manifest[number - 1]["refs"]
embed_fonts(prs)
prs.save(OUT / "Egypt-vs-Germany-ID-Cards.pptx")
pdf.save()
(ROOT / "research/english-deck-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Built {len(prs.slides)} English slides, {sum(s['effects'] for s in manifest)} native entrance effects, matching static PDF.")
if layout_errors:
    raise SystemExit("\n".join(layout_errors))
