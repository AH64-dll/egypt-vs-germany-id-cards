"""Build the deck: python build/build_deck.py [module ...]  -> output/_draft.pptx"""
import sys, importlib, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import Deck, ROOT
mods = sys.argv[1:] or ["s01", "s02", "s03", "s04", "s05", "s06", "s07"]
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
