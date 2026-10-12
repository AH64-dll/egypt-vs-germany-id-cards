import asyncio, re
from playwright.async_api import async_playwright
START = ["https://www.personalausweisportal.de/Webs/PA/DE/buergerinnen-und-buerger/der-personalausweis/der-personalausweis-node.html",
         "https://www.personalausweisportal.de/Webs/PA/EN/citizens/german-id-card/german-id-card-node.html"]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="msedge", headless=True); pg = await b.new_page()
        seen=set(); links=set()
        for u in START:
            await pg.goto(u, wait_until="domcontentloaded")
            hrefs = await pg.eval_on_selector_all("a", "els=>els.map(e=>e.href)")
            for h in hrefs:
                if re.search(r'(Bilderstrecke|bildergalerie|sicherheit|security|Sicherheitsmerkmal|aussehen|design)', h, re.I): links.add(h.split('#')[0])
        print("links:", *sorted(links), sep="\n  ")
        for u in sorted(links)[:12]:
            try:
                await pg.goto(u, wait_until="domcontentloaded", timeout=30000)
                imgs = await pg.eval_on_selector_all("img", "els=>els.map(e=>e.src+' | '+(e.alt||'').slice(0,100))")
                print("==", u)
                for s in imgs:
                    if s not in seen and re.search(r'(jpg|png)', s, re.I): seen.add(s); print("   ", s)
            except Exception as e: print("ERR", u, e)
        await b.close()
asyncio.run(main())
