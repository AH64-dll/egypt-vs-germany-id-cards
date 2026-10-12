import sys, pathlib, pymupdf
src, outdir, prefix = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
outdir.mkdir(parents=True, exist_ok=True)
doc = pymupdf.open(src)
for pno in range(len(doc)):
    page = doc[pno]
    for i, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        try:
            pix = pymupdf.Pixmap(doc, xref)
            if pix.n - pix.alpha >= 4:
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
            if pix.width < 120 or pix.height < 60:
                continue
            fn = outdir / f"{prefix}_p{pno+1:02d}_{i}_{pix.width}x{pix.height}.png"
            pix.save(fn)
        except Exception as e:
            print("skip", pno+1, i, e)
print("done", src)
