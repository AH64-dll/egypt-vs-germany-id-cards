# QA log — current English presentation

Validated on 12 October 2026. Outputs replace the prior bilingual deck:
`output/Egypt-vs-Germany-ID-Cards.pptx` and `.pdf`, each with 24 slides/pages.
The two contact sheets and `renders/s01.png` through `s24.png` show the new PDF.
Obsolete previews for slides 25–37 have been removed.

| Check | Result |
|---|---|
| Cover | Exact name, code, course, comparison subtitle and supervisor |
| Editable slide text and notes | English throughout |
| Lecture mapping | 57/57 concepts mapped to slides or speaker notes |
| Sources | Per-slide source labels; fuller citations and caveats in notes |
| Native animations | 495 object entrance effects; 24 fade transitions |
| Timing structure | Unique IDs; all shape targets resolve |
| XML conformance | ECMA-376 transitional schema: presentation and 24 slide XML parts pass |
| Fonts | Original Office-exported Barlow, Barlow SemiBold and Barlow Condensed SemiBold embedded |
| Layout | Measured text fits; all shape bounds within slide |
| PDF | 24 pages; normalized text matches corresponding PowerPoint slides |
| Visual review | Complete PDF contact sheets inspected; illustrative crop corrected |
| Content boundaries | Egyptian roadmap distinguished from current lecture features; unknown polymer/print method unspecified |

Commands:
```bash
python deck/build/build_deck.py
python deck/build/qa.py
python deck/build/qa_english.py --schema /workspace/ooxml-schema/pml.xsd
python deck/build/render_preview.py
```

The optional schema files were retrieved from the QtExcel ECMA-376-5th schema
collection into a workspace-only cache; they are not a build dependency.

Verification limit: previews are rendered from the directly generated PDF, not
from a desktop PowerPoint export. Animation timing is present and schema-valid,
but actual desktop PowerPoint playback has not been visually tested in this
Linux environment. Open the PPTX in Slide Show to play the effects; PDF and
image previews are static.
