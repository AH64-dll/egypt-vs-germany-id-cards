# Security Printing — National ID Card Comparison: Egypt and Germany

**24 English slides**, condensed from all four supplied lectures (112 pages),
with additional sourced German ID-card information. The original 37-slide
bilingual deck has been replaced at the existing output paths.

**Kareem Waleed Wagdy** · **Student code: 792400615**

**Security Printing** · **Under the supervision of Rania Mohamed**

- [Animated PowerPoint](deck/output/Egypt-vs-Germany-ID-Cards.pptx)
- [Static reading PDF](deck/output/Egypt-vs-Germany-ID-Cards.pdf)
- [Preview: slides 1–12](deck/output/contact_sheet_1.jpg)
- [Preview: slides 13–24](deck/output/contact_sheet_2.jpg)

Open the **PPTX in PowerPoint and start Slide Show** (F5, or Shift+F5 from the
current slide). Each slide automatically reveals its title and content in short
staggered fades. Click or use the arrow keys to advance at your own pace. The
deck contains 495 native object entrance effects and 24 slide fade transitions;
the original Barlow font faces are embedded. A PDF and the preview images are
static copies and do not play these effects.

The lecture essentials are on the slides; speaker notes carry the fuller
explanations, terminology corrections and source boundaries. The deck covers
security principles, document layers, personalization criteria, materials,
prepress/offset, plates and preparation, Egyptian verification levels, German
optical/UV/electronic features, comparison tables and Egypt's lecture roadmap.
Future proposals are labelled as proposals. The precise Egyptian polymer and
personalization method are left unspecified because the lectures do not establish
them. The German comparison refers to the design documented by BMI in May 2024.

## Rebuild

```bash
python -m pip install -r deck/build/requirements.txt
python deck/build/build_deck.py
python deck/build/qa.py
python deck/build/render_preview.py
```

`build_english.py` produces the editable animated PPTX and matching vector-text
PDF from one measured layout. `animations.py` adds native DrawingML timing;
`embed_fonts.py` preserves the original Office-exported embedded fonts.
`qa_english.py` checks English text/notes, exact cover details, shape bounds,
animation references, font embedding, PDF text parity and the 57-concept lecture
coverage map. Optional XML schema validation:

```bash
python deck/build/qa_english.py --schema /absolute/path/to/pml.xsd
```

The PDF is generated directly from the same layout, not by PowerPoint. Static
previews are rendered from that PDF. Native animation playback has not been
visually tested in a desktop PowerPoint session in this Linux environment.

The legacy `s01.py`–`s06.py` modules and Windows `finalize.ps1` remain available
for historical rebuilding; the default build and QA target the current English
deck. Older versions are available through Git history.

## Sources and assets

See [sources](deck/research/sources.md), [claims](deck/research/claims-register.md),
[lecture coverage](deck/research/coverage-matrix.csv) and
[validation record](deck/research/qa-log.md). The four lecture PDFs remain at
the repository root. German specimen images/macros: BMI/Personalausweisportal,
© BKA / Bundesdruckerei. Egyptian specimen: Heshamdiab16, Wikimedia Commons,
CC BY-SA 3.0; fields were replaced with labels by the uploader. Lecture crop:
holder data masked. Original diagrams and 3D artwork are retained from the repo.
