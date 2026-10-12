"""Reuse the repository's Office-embedded Barlow fonts in the new presentation.

These fntdata parts came from the prior PowerPoint export, not from renaming raw
TTF files. Retaining them avoids depending on a system Barlow installation.
"""
from copy import deepcopy
from pathlib import Path
from lxml import etree
from pptx.opc.package import Part
from pptx.opc.packuri import PackURI
from pptx.oxml.ns import qn


def embed_fonts(prs):
    root = Path(__file__).resolve().parents[1] / "assets/embedded-fonts"
    font_list = deepcopy(etree.parse(str(root / "embedded-fonts.xml")).getroot())
    for font in font_list:
        for variant in list(font)[1:]:
            filename = variant.get(qn("r:id"))
            part = Part(PackURI("/ppt/fonts/" + filename), "application/x-fontdata",
                        prs.part.package, (root / filename).read_bytes())
            relationship = prs.part.relate_to(part, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font")
            variant.set(qn("r:id"), relationship)
    document = prs.part._element
    document.set("embedTrueTypeFonts", "1")
    document.set("saveSubsetFonts", "1")
    for old in document.findall(qn("p:embeddedFontLst")):
        document.remove(old)
    successor = document.find(qn("p:defaultTextStyle"))
    if successor is not None:
        successor.addprevious(font_list)
    else:
        document.append(font_list)
