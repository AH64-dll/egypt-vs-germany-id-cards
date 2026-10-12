"""Native DrawingML entrance animations; no raster/video animation substitute.

Effects start automatically when a slide opens. Slides advance on click, so the
presenter controls reading time. Keep this timing XML when exporting in Office.
"""
from lxml import etree
from pptx.oxml.ns import qn


def add_animations(slide, phases):
    root = slide._element
    for tag in ("p:transition", "p:timing"):
        for old in root.findall(qn(tag)):
            root.remove(old)
    transition = etree.Element(qn("p:transition"), spd="med", advClick="1")
    etree.SubElement(transition, qn("p:fade"))
    timing = etree.Element(qn("p:timing"))
    tn_list = etree.SubElement(timing, qn("p:tnLst"))
    par = etree.SubElement(tn_list, qn("p:par"))
    main = etree.SubElement(par, qn("p:cTn"), id="1", dur="indefinite", restart="never", nodeType="tmRoot")
    children = etree.SubElement(main, qn("p:childTnLst"))
    seq = etree.SubElement(children, qn("p:seq"), concurrent="1", nextAc="seek")
    sequence = etree.SubElement(seq, qn("p:cTn"), id="2", dur="indefinite", nodeType="mainSeq")
    effects = etree.SubElement(sequence, qn("p:childTnLst"))
    ident = 3
    for phase, shape_ids in sorted(phases.items()):
        block = etree.SubElement(effects, qn("p:par"))
        clock = etree.SubElement(block, qn("p:cTn"), id=str(ident), fill="hold")
        ident += 1
        starts = etree.SubElement(clock, qn("p:stCondLst"))
        etree.SubElement(starts, qn("p:cond"), delay=str(phase * 260))
        group = etree.SubElement(clock, qn("p:childTnLst"))
        for shape_id in shape_ids:
            entrance = etree.SubElement(group, qn("p:par"))
            effect = etree.SubElement(entrance, qn("p:cTn"), id=str(ident), dur="550", fill="hold",
                                      presetID="10", presetClass="entr", presetSubtype="0", grpId="0", nodeType="withEffect")
            ident += 1
            start = etree.SubElement(effect, qn("p:stCondLst"))
            etree.SubElement(start, qn("p:cond"), delay="0")
            behavior_list = etree.SubElement(effect, qn("p:childTnLst"))
            # Visibility set and opacity effect are both required by Office.
            visible = etree.SubElement(behavior_list, qn("p:set"))
            behavior = etree.SubElement(visible, qn("p:cBhvr"))
            tick = etree.SubElement(behavior, qn("p:cTn"), id=str(ident), dur="1", fill="hold")
            ident += 1
            starts = etree.SubElement(tick, qn("p:stCondLst"))
            etree.SubElement(starts, qn("p:cond"), delay="0")
            target = etree.SubElement(behavior, qn("p:tgtEl"))
            etree.SubElement(target, qn("p:spTgt"), spid=str(shape_id))
            attrs = etree.SubElement(behavior, qn("p:attrNameLst"))
            etree.SubElement(attrs, qn("p:attrName")).text = "style.visibility"
            to = etree.SubElement(visible, qn("p:to"))
            etree.SubElement(to, qn("p:strVal"), val="visible")
            fade = etree.SubElement(behavior_list, qn("p:animEffect"), transition="in", filter="fade")
            behavior = etree.SubElement(fade, qn("p:cBhvr"))
            etree.SubElement(behavior, qn("p:cTn"), id=str(ident), dur="550", fill="hold")
            ident += 1
            target = etree.SubElement(behavior, qn("p:tgtEl"))
            etree.SubElement(target, qn("p:spTgt"), spid=str(shape_id))
    for tag, event in (("p:prevCondLst", "onPrev"), ("p:nextCondLst", "onNext")):
        conditions = etree.SubElement(seq, qn(tag))
        condition = etree.SubElement(conditions, qn("p:cond"), evt=event, delay="0")
        target = etree.SubElement(condition, qn("p:tgtEl"))
        etree.SubElement(target, qn("p:sldTgt"))
    # ECMA-376 order: cSld, clrMapOvr, transition, timing, extLst.
    extension = root.find(qn("p:extLst"))
    if extension is not None:
        extension.addprevious(transition)
        extension.addprevious(timing)
    else:
        root.append(transition)
        root.append(timing)
