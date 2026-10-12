# Egypt vs Germany — National ID Cards (Security Printing)

Bilingual (Arabic / English) 37-slide presentation comparing the Egyptian Identity Verification Card and the German Personalausweis — materials, printing technologies, personalization, security features and design.
Course: GDM5313 Security Printing / GDM5310 Pre-Press Technologies, Dr. Rania Mohamed, ECU 2026/27.

- **Final deck:** `deck/output/Egypt-vs-Germany-ID-Cards.pptx` and `.pdf`
- **Research:** `deck/research/` — sources, claims register, lecture coverage matrix, QA log
- **Build:** `deck/build/` — python-pptx slide modules (`s01.py`–`s06.py`), `build_deck.py`, `finalize.ps1` (PowerPoint COM export), `qa.py`
- **Assets:** `deck/assets/` — raw extracts, processed crops, original art
- **Lectures:** the four course PDFs at the repository root

Rebuild:
```
python -P deck/build/build_deck.py s01 s02 s03 s04 s05 s06
powershell -File deck/build/finalize.ps1 -In deck/output/_draft.pptx -Out deck/output/Egypt-vs-Germany-ID-Cards.pptx -Pdf deck/output/Egypt-vs-Germany-ID-Cards.pdf -PngDir deck/output/renders
python -P deck/build/qa.py deck/output/Egypt-vs-Germany-ID-Cards.pptx
```
Requires the fonts Barlow, Barlow Condensed and IBM Plex Sans Arabic installed.
