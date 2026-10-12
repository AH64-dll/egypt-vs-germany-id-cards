# QA log — Egypt vs Germany ID cards deck

Final files: `output/Egypt-vs-Germany-ID-Cards.pptx` (37 slides, 16:9, fonts embedded, ~29 MB) and `output/Egypt-vs-Germany-ID-Cards.pdf` (~8.7 MB). Renders: `output/renders/s01–s37.png` (1920 px). Contact sheets: `output/contact_sheet_1.jpg`, `output/contact_sheet_2.jpg`.

## Automated checks (`build/qa.py`, output in `_qa_output.txt`)
| Check | Result |
|---|---|
| Slide count | 37 |
| Language alternation (odd = Arabic, even = English); no Arabic on English slides; Arabic slides ≥ 60 % Arabic script | pass |
| `rtl="1"` on every Arabic paragraph (text boxes and table cells) | pass |
| Arabic complex-script font on every Arabic run; only Barlow / Barlow Condensed / IBM Plex Sans Arabic used | pass |
| Speaker notes: own language first, full other language, "Sources / المصادر" line | pass (37/37) |
| Source tag in footer (all slides except cover and closing) | pass |
| Text overflow (PowerPoint COM BoundHeight vs frame) | NO_OVERFLOW |
| Off-slide / zero-size shapes | none (intentional bleed images excluded) |
| Coverage matrix: keywords of each of the 57 lecture concepts found on the mapped slides (text + notes) | 57/57 |
| Effective image resolution ≥ 150 ppi | 14 warnings, accepted — see below |

**Resolution warnings:** all 14 are BMI macro photographs (native ~375 px wide in the official flyer) or zoomed crops of the Wikimedia specimen, shown at 87–145 ppi. They were not upscaled with generative tools, to keep the images authentic. They read cleanly at projection size (checked in the 1920 px renders).

## Visual review (every slide rendered and inspected; fixed and re-rendered where noted)
- s01–s13: reviewed in earlier passes (cover cards, roadmap pyramid, ISO table, exploded card). The chapter-numeral boxes were enlarged to clear the COM overflow flags.
- s14–s20 (printing):
  - s18: subtitle widened to one line.
  - s19: perforation values redrawn as a native diagram from PP2 p.32 (196.5 / 196.5 / 425 mm).
  - s14 and s16: label boxes trimmed so they stay inside the slide.
- s21: the cost column was rebuilt so the "tickets" text no longer collides with the solid block.
- s22:
  - A negative-width text box made PowerPoint refuse the file; the national-number strip was rebuilt.
  - Badges moved off the field labels; legend spacing tightened.
- s23: badges moved off the personal data; card size and grid reduced to fit; privacy box clear of the list.
- s24: chips now wrap to two lines instead of being cut off.
- s25:
  - Crossing leader lines replaced by numbered badges.
  - The relief loupe is a clearly labelled illustration ("رسم توضيحي"), because the effect is not visible in any available image.
- s27:
  - The verification matrix reproduces the official BMI icon matrix, read from the flyer page 2 icons.
  - Arabic row labels right-aligned.
- s28:
  - Captions moved clear of the footer.
  - The 66 ppi Identigram crop was replaced with the OVI logo macro.
- s31: Arabic source label given RTL and an Arabic font.
- s32: subtitle shortened so it no longer overlaps the column headers.
- s35: cards re-centred.
- s36: two-line references now get extra spacing.
- Bidi spot checks: "8.6 × 5.4 سم", "ID-1", "GDM5313" and the parentheses all display correctly in RTL text.

## Accuracy
- Every on-slide claim maps to `claims-register.md`. New entries are D28–D30, E14 and E15.
- Unverified E13 (Morpho/Safran) is mentioned only in the slide 36 notes, as "not used".
- Secondary sources are labelled on the slides: Wikipedia (7-year validity, number structure, PDF417), HRW (1995) and Annahar (no redesign as of May 2026).
- Gaps are stated, not filled: the Egyptian substrate and personalization method are unpublished, and German laboratory-level features are unpublished.
- Lecture anomalies are footnoted:
  - ID-2 height typo;
  - "Kingram" spelling;
  - missing polycarbonate intro slide;
  - inconsistent web-offset speed.

## Privacy
- Egyptian card images: the Wikimedia specimen carries field labels only.
- The lecture photo is used only as small crops, with the face blurred and the name, address, numbers and DOB pixelated.
- The national-number structure uses placeholder letters.
- German images are the official MUSTER specimens (fictional holder).

## Asset optimisation
Hi-res originals are kept in `assets/art/_hires/` and `assets/processed/_hires/`. The deck uses these downscaled copies:
- backgrounds at 2560 px;
- guilloche art palettised;
- card images at 1800–2100 px.

This took the PPTX from 62 MB to 29 MB with no visible change at 1920 px.

## Font verification (late catch)
The PDF font audit showed PowerPoint had silently substituted Calibri for IBM Plex Sans Arabic. The per-user font files were registered but had not been loaded into the Windows session.
- Fix: the fonts were loaded with `AddFontResourceW` plus a `WM_FONTCHANGE` broadcast, then the deck was re-exported.
- Check: the PDF now embeds IBMPlexSansArabic Regular, Light, Medium, SemiBold and Bold, and the PPTX embeds all 10 deck font faces.
- Re-review: every Arabic slide was re-reviewed with the real font, because Plex is wider than Calibri:
  - s01 and s37: the course credit is now split onto two lines;
  - s29: step-box text set to 9.5 pt;
  - s25: relief illustration text reduced.
- Result: COM overflow check is NO_OVERFLOW and qa.py reports 0 errors.
