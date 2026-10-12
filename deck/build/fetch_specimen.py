import asyncio, pathlib
from playwright.async_api import async_playwright
out = pathlib.Path("assets/raw/bmi"); out.mkdir(parents=True, exist_ok=True)
P="https://www.personalausweisportal.de/SharedDocs/"
B="https://www.bmi.bund.de/SharedDocs/bilder/DE/schmuckbilder/moderne-verwaltung/paesse-ausweise/personalausweis.jpg"
items = []
for v in ["poster","normal","panorama","original","standard"]:
    items += [(f"pap_de_front_{v}.jpg", P+f"bilder/Webs/PA/DE/Kopfbilder/bub_der_personalausweis.jpg?__blob={v}"),
              (f"pap_details_de_{v}.jpg", P+f"bildergalerien/Webs/PA/DE/Bilderstrecke_BuB_Personalausweis/Infobroschuere_Details.jpg?__blob={v}"),
              (f"pap_details_en_{v}.jpg", P+f"bildergalerien/Webs/PA/EN/Bilderstrecke_neuer_Personalausweis/Infobroschuere_Details.jpg?__blob={v}"),
              (f"bmi_frontback_{v}.jpg", B+f"?__blob={v}")]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="msedge", headless=True)
        ctx = await b.new_context(); pg = await ctx.new_page()
        await pg.goto("https://www.personalausweisportal.de/Webs/PA/DE/buergerinnen-und-buerger/der-personalausweis/der-personalausweis-node.html")
        await pg.goto("https://www.bmi.bund.de/SharedDocs/bilder/DE/schmuckbilder/moderne-verwaltung/paesse-ausweise/personalausweis.html")
        for name, url in items:
            r = await ctx.request.get(url)
            ct = r.headers.get("content-type","")
            if r.ok and "image" in ct:
                body = await r.body(); (out/name).write_bytes(body); print("ok", name, len(body))
            else:
                print("--", name, r.status, ct)
        await b.close()
asyncio.run(main())
