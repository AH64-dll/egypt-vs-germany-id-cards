"""Check the final English deck, its timings, fonts, PDF and lecture mapping.

Optional ECMA-376 XSD validation: --schema /absolute/path/to/pml.xsd
"""
import argparse
import csv
import re
from pathlib import Path
from zipfile import ZipFile

import fitz
from lxml import etree
from pptx import Presentation
from pptx.oxml.ns import qn

parser = argparse.ArgumentParser()
parser.add_argument("pptx", nargs="?", default=str(Path(__file__).resolve().parents[1] / "output/Egypt-vs-Germany-ID-Cards.pptx"))
parser.add_argument("--schema")
args = parser.parse_args()
path = Path(args.pptx)
root = Path(__file__).resolve().parents[1]
prs = Presentation(path)
arabic = re.compile(r"[\u0600-\u06ff\u0750-\u077f\ufb50-\ufdff\ufe70-\ufeff]")
errors = []
slide_text = {}
effects = 0
if len(prs.slides) != 24:
    errors.append(f"Expected 24 slides, got {len(prs.slides)}")

for number, slide in enumerate(prs.slides, 1):
    texts = [sh.text for sh in slide.shapes if sh.has_text_frame and sh.text.strip()]
    notes = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""
    visible = " ".join(texts)
    slide_text[number] = visible + " " + notes
    if arabic.search(slide_text[number]):
        errors.append(f"Slide {number}: Arabic text in editable content or speaker notes")
    if not notes or "Sources:" not in notes:
        errors.append(f"Slide {number}: missing notes/source attribution")
    if f"{number:02d} / 24" not in visible:
        errors.append(f"Slide {number}: incorrect slide counter")
    if len(visible.split()) > 200:
        errors.append(f"Slide {number}: over 200 visible words")
    identifiers = {str(sh.shape_id) for sh in slide.shapes}
    timing = slide._element.find(qn("p:timing"))
    transition = slide._element.find(qn("p:transition"))
    if timing is None or transition is None:
        errors.append(f"Slide {number}: missing native animation or transition")
    else:
        effect_list = timing.findall('.//' + qn('p:animEffect'))
        effects += len(effect_list)
        if len(effect_list) < 3:
            errors.append(f"Slide {number}: too few animated targets")
        time_ids = [node.get("id") for node in timing.iter(qn("p:cTn"))]
        if len(set(time_ids)) != len(time_ids):
            errors.append(f"Slide {number}: duplicate timing node IDs")
        for target in timing.iter(qn("p:spTgt")):
            if target.get("spid") not in identifiers:
                errors.append(f"Slide {number}: animation targets a missing shape")
    for shape in slide.shapes:
        if min(shape.left, shape.top) < 0 or shape.left + shape.width > prs.slide_width + 1000 or shape.top + shape.height > prs.slide_height + 1000:
            errors.append(f"Slide {number}: off-slide shape {shape.name}")

cover = slide_text[1]
for required in ["SECURITY", "PRINTING", "Kareem Waleed Wagdy", "792400615", "Rania Mohamed", "Egypt and Germany"]:
    if required not in cover:
        errors.append(f"Cover missing {required}")

matched, total = 0, 0
with (root / "research/coverage-matrix.csv").open(encoding="utf-8") as source:
    for row in csv.DictReader(source):
        total += 1
        mapped = [int(n) for n in re.findall(r"\d+", row["slides"])]
        haystack = " ".join(slide_text.get(n, "") for n in mapped).lower()
        if any(word.strip().lower() in haystack for word in row["keywords"].split("|")):
            matched += 1
        else:
            errors.append(f"Coverage #{row['id']}: {row['concept']} not found on {mapped}")

with ZipFile(path) as package:
    if package.testzip() is not None:
        errors.append("Corrupt ZIP member")
    pres = etree.fromstring(package.read("ppt/presentation.xml"))
    fonts = pres.find(qn("p:embeddedFontLst"))
    if fonts is None or len(fonts) != 3:
        errors.append("Missing original Office-embedded font faces")
    if args.schema:
        schema = etree.XMLSchema(etree.parse(args.schema))
        for filename in package.namelist():
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", filename) or filename == "ppt/presentation.xml":
                if not schema.validate(etree.fromstring(package.read(filename))):
                    errors.append(f"{filename}: {schema.error_log}")

with fitz.open(path.with_suffix(".pdf")) as document:
    if len(document) != 24:
        errors.append("PDF page count differs from PowerPoint")
    for number, page in enumerate(document, 1):
        ppt_text = " ".join(sh.text for sh in prs.slides[number - 1].shapes if sh.has_text_frame)
        normalize = lambda value: re.sub(r"\s+", "", value)
        if normalize(ppt_text) != normalize(page.get_text()):
            errors.append(f"Slide {number}: PDF text differs from PowerPoint")

print(f"English QA: {len(prs.slides)} slides; {effects} entrance effects; 24 fade transitions")
print(f"Lecture coverage: {matched}/{total} concepts mapped to slides or speaker notes")
print("English-only editable text and notes; exact student details; embedded fonts; geometry; PDF parity")
if args.schema:
    print("ECMA-376 schema validation enabled for presentation and all slide XML")
print(f"Errors: {len(errors)}")
for error in errors:
    print("ERROR:", error)
raise SystemExit(bool(errors))
