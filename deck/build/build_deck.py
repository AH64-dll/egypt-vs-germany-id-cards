"""Build the current English deck; explicit s01..s06 arguments build the legacy deck."""
import sys, importlib, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
if len(sys.argv) == 1:
    import build_english
    raise SystemExit(0)
from lib import Deck, ROOT
mods = sys.argv[1:]
D = Deck()
for m in mods:
    try:
        mod = importlib.import_module(m)
    except ModuleNotFoundError as e:
        print("skip", m, e); continue
    for fn in mod.SLIDES:
        fn(D)
out = ROOT / "output/_draft.pptx"
D.save(out); print("saved", out, D.n, "slides")
