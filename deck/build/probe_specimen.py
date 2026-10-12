import asyncio, sys, re
from playwright.async_api import async_playwright
URLS = [
 "https://www.personalausweisportal.de/Webs/PA/DE/buergerinnen-und-buerger/der-personalausweis/der-personalausweis-node.html",
 "https://www.personalausweisportal.de/Webs/PA/EN/citizens/german-id-card/german-id-card-node.html",
 "https://www.bmi.bund.de/SharedDocs/bilder/DE/schmuckbilder/moderne-verwaltung/paesse-ausweise/personalausweis.html",
]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="msedge", headless=True)
        pg = await b.new_page()
        for u in URLS:
            try:
                r = await pg.goto(u, timeout=45000, wait_until="domcontentloaded")
                print("==", u, r.status if r else None, await pg.title())
                imgs = await pg.eval_on_selector_all("img, a", "els => els.map(e => (e.src||e.href||'') + ' | ' + (e.alt||e.title||e.innerText||'').slice(0,90))")
                for s in imgs:
                    if re.search(r'(jpg|jpeg|png|__blob=image)', s, re.I): print("  ", s)
            except Exception as e:
                print("ERR", u, e)
        await b.close()
asyncio.run(main())
