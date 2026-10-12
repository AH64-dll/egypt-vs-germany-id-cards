import asyncio, sys, re
from playwright.async_api import async_playwright
URLS = sys.argv[1:]
KEYS = r'(Polycarbonat|polycarbonate|Gültig|valid|Jahre|years|Bundesdruckerei|Chip|Fingerabdr|fingerprint|PIN|CAN|2010|2021|2024|Lasergrav|laser|Scheckkarte|ID-1|Format|kontaktlos|contactless)'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="msedge", headless=True); pg = await b.new_page()
        for u in URLS:
            try:
                await pg.goto(u, wait_until="domcontentloaded", timeout=45000)
                t = await pg.inner_text("main") if await pg.query_selector("main") else await pg.inner_text("body")
                print("=====", u)
                for line in t.split("\n"):
                    line=line.strip()
                    if len(line)>25 and re.search(KEYS, line, re.I): print(" *", line[:400])
            except Exception as e: print("ERR", u, e)
        await b.close()
asyncio.run(main())
