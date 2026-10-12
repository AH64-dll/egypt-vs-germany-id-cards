"""Original artwork rendered in headless Edge (Playwright) -> transparent PNGs in assets/art.

Scenes: guilloche rosette + wave band, floating card mockups (CSS 3D), isometric layer stacks (SVG)
with anchor coordinates exported to assets/art/anchors.json for native PPTX labels/leader lines.
"""
import asyncio, json, math, pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
ART = ROOT / "assets/art"; PROC = ROOT / "assets/processed"; ART.mkdir(exist_ok=True)
ANCH = {}
OR, OR2, DEEP, BONE = "#FF5A1F", "#D63A0B", "#8F270D", "#F5F3F0"

import base64
def uri(p):
    return "data:image/png;base64," + base64.b64encode((PROC / p).read_bytes()).decode()

# ---------------------------------------------------------------- guilloche (canvas)
GUILLOCHE_JS = r"""
function rosette(ctx, cx, cy, R, rings, stroke, alpha, lw){
  ctx.globalCompositeOperation='lighter';
  for (let k=0;k<rings.length;k++){
    const [Rr, r, d, n, ph] = rings[k];
    for (let j=0;j<n;j++){
      ctx.beginPath();
      const phase = ph + j*2*Math.PI/n;
      const N = 1400*r/gcd(Rr,r);
      for (let i=0;i<=N;i++){
        const t = i/N*2*Math.PI*r/gcd(Rr,r);
        const x = (Rr-r)*Math.cos(t) + d*Math.cos((Rr-r)/r*t + phase);
        const y = (Rr-r)*Math.sin(t) - d*Math.sin((Rr-r)/r*t + phase);
        const X = cx + x*R/(Rr), Y = cy + y*R/(Rr);
        if(i==0) ctx.moveTo(X,Y); else ctx.lineTo(X,Y);
      }
      ctx.strokeStyle = stroke(k,j); ctx.globalAlpha = alpha; ctx.lineWidth = lw; ctx.stroke();
    }
  }
}
function gcd(a,b){ return b? gcd(b, a%b) : a; }
"""

def html_rosette(size, variant):
    return f"""<html><body style='margin:0;background:transparent'>
<canvas id=c width={size} height={size}></canvas><script>{GUILLOCHE_JS}
const c=document.getElementById('c'), ctx=c.getContext('2d'); const S={size};
const cols=['#FF5A1F','#D63A0B','#FF8A4C','#8F270D','#FFB08A'];
const stroke=(k,j)=>cols[(k+j)%cols.length];
const v={variant};
if(v==0){{
  rosette(ctx,S/2,S/2,S*0.46,[[96,27,40,6,0],[96,27,40,6,0.26]],stroke,0.22,1.1);
  rosette(ctx,S/2,S/2,S*0.33,[[80,23,30,5,0.1],[80,23,30,5,0.45]],stroke,0.20,1.0);
  rosette(ctx,S/2,S/2,S*0.20,[[60,17,22,4,0.3]],stroke,0.22,0.9);
}} else {{
  rosette(ctx,S/2,S/2,S*0.47,[[120,41,52,3,0]],stroke,0.30,0.9);
  rosette(ctx,S/2,S/2,S*0.30,[[70,19,28,2,0.2]],stroke,0.28,0.8);
}}
</script></body></html>"""

def html_waves(w, h):
    return f"""<html><body style='margin:0;background:transparent'><canvas id=c width={w} height={h}></canvas><script>
const c=document.getElementById('c'),ctx=c.getContext('2d');ctx.globalCompositeOperation='lighter';
const W={w},H={h};
for(let j=0;j<46;j++){{
  ctx.beginPath();
  for(let x=0;x<=W;x+=3){{
    const t=x/W*Math.PI*2;
    const y=H/2+Math.sin(t*3+j*0.14)*H*0.22+Math.sin(t*7-j*0.09)*H*0.08+(j-23)*H*0.012;
    if(x==0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
  }}
  const g=ctx.createLinearGradient(0,0,W,0);g.addColorStop(0,'rgba(255,90,31,0)');g.addColorStop(0.3,'rgba(255,90,31,0.9)');
  g.addColorStop(0.7,'rgba(214,58,11,0.9)');g.addColorStop(1,'rgba(143,39,13,0)');
  ctx.strokeStyle=g;ctx.globalAlpha=0.35;ctx.lineWidth=1.4;ctx.stroke();
}}</script></body></html>"""

# ---------------------------------------------------------------- floating cards (CSS 3D)
CARD_CSS = """
body{margin:0;background:transparent;width:%dpx;height:%dpx;overflow:hidden;font-family:sans-serif}
.stage{position:absolute;inset:0;perspective:2600px}
.card{position:absolute;border-radius:3.6%%/5.7%%;transform-style:preserve-3d}
.card img{position:relative;z-index:1;width:100%%;height:100%%;border-radius:inherit;display:block}
.card::after{content:'';position:absolute;inset:0;border-radius:inherit;
  z-index:2;background:linear-gradient(115deg,rgba(255,255,255,0.0) 32%%,rgba(255,255,255,0.16) 46%%,rgba(255,255,255,0.0) 58%%);mix-blend-mode:screen}
.edge{position:absolute;z-index:0;inset:0;border-radius:inherit;transform:translate(5px,7px);background:#3a302a}
"""

def html_cards(w, h, cards):
    parts = []
    for c in cards:
        shadow = f"filter: drop-shadow(0 {c.get('sy',60)}px {c.get('sb',70)}px rgba(0,0,0,.75)) drop-shadow(0 0 {c.get('glow',40)}px rgba(255,90,31,{c.get('ga',.35)}));"
        parts.append(f"""<div class=card style="left:{c['x']}px;top:{c['y']}px;width:{c['w']}px;height:{c['w']/c.get('ratio',1.586):.1f}px;
          transform:{c['t']};{shadow}"><div class=edge></div><img src="{uri(c['img'])}"></div>""")
    return f"<html><head><style>{CARD_CSS % (w, h)}</style></head><body><div class=stage>{''.join(parts)}</div></body></html>"

# ---------------------------------------------------------------- isometric stacks (SVG)
def iso(u, v, z, ox, oy, s):
    """card plane (u along width, v along depth) -> screen; z lifts layer up."""
    X = ox + (u * 0.866 - v * 0.866) * s
    Y = oy + (u * 0.5 + v * 0.5) * s - z * s
    return X, Y

def slab_path(w, d, z, ox, oy, s, r=0.0):
    pts = [iso(0, 0, z, ox, oy, s), iso(w, 0, z, ox, oy, s), iso(w, d, z, ox, oy, s), iso(0, d, z, ox, oy, s)]
    return pts

def poly(pts):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)

def svg_pyramid(W, H, levels, name):
    """Stacked slabs (largest at bottom), exploded with gaps; returns svg + anchors (right/left label points)."""
    s = 1.0; ox, oy = W * 0.5, H * 0.20
    out = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}'>",
           "<defs>",
           f"<linearGradient id='top' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#FF8A4C'/><stop offset='.45' stop-color='{OR}'/><stop offset='1' stop-color='{OR2}'/></linearGradient>",
           f"<linearGradient id='topd' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#3a3a3a'/><stop offset='1' stop-color='#1b1b1b'/></linearGradient>",
           f"<linearGradient id='sideL' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='{OR2}'/><stop offset='1' stop-color='{DEEP}'/></linearGradient>",
           f"<linearGradient id='sideR' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='{DEEP}'/><stop offset='1' stop-color='#3d1206'/></linearGradient>",
           "<linearGradient id='sideLd' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#2b2b2b'/><stop offset='1' stop-color='#121212'/></linearGradient>",
           "<linearGradient id='sideRd' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#1d1d1d'/><stop offset='1' stop-color='#0c0c0c'/></linearGradient>",
           "<filter id='blur'><feGaussianBlur stdDeviation='28'/></filter>",
           "</defs>"]
    anchors = []
    n = len(levels)
    base_w, base_d = W * 0.46, W * 0.46 * 0.63
    thick = H * 0.045; gap = H * 0.115
    # floor glow
    gx, gy = iso(base_w / 2, base_d / 2, 0, ox, oy + H * 0.42, s)
    out.append(f"<ellipse cx='{gx:.0f}' cy='{gy:.0f}' rx='{W*0.36:.0f}' ry='{H*0.09:.0f}' fill='{OR}' opacity='.28' filter='url(#blur)'/>")
    for i, lv in enumerate(levels):           # i=0 bottom
        f = 1 - i * 0.16
        w, d = base_w * f, base_d * f
        cx0 = (base_w - w) / 2; cy0 = (base_d - d) / 2
        z0 = -(H * 0.42) + i * (thick + gap)   # screen offset upward handled via z (in px)
        lift = (H * 0.40) - i * (thick + gap)
        def P(u, v, zz):
            return iso(cx0 + u, cy0 + v, 0, ox, oy + lift - zz, s)
        hot = lv.get("hot", False)
        top = [P(0, 0, thick), P(w, 0, thick), P(w, d, thick), P(0, d, thick)]
        left = [P(0, d, thick), P(w, d, thick), P(w, d, 0), P(0, d, 0)]
        right = [P(w, 0, thick), P(w, d, thick), P(w, d, 0), P(w, 0, 0)]
        out.append(f"<polygon points='{poly(left)}' fill='url(#{'sideL' if hot else 'sideLd'})'/>")
        out.append(f"<polygon points='{poly(right)}' fill='url(#{'sideR' if hot else 'sideRd'})'/>")
        out.append(f"<polygon points='{poly(top)}' fill='url(#{'top' if hot else 'topd'})' stroke='{'#FFB08A' if hot else '#4a4a4a'}' stroke-width='1.5' stroke-opacity='.6'/>")
        # anchor: right-most corner (w,0) mid-thickness and left-most corner (0,d)
        rx, ry = P(w, 0, thick / 2); lx, ly = P(0, d, thick / 2)
        anchors.append({"right": [rx / W, ry / H], "left": [lx / W, ly / H], "label": lv["label"]})
    out.append("</svg>")
    ANCH[name] = anchors
    return "\n".join(out)

def svg_exploded(W, H, name):
    """Exploded generic card (6 layers) in isometric view; anchors at right-front corner of each layer."""
    s = 1.0; cw = W * 0.40; cd = cw / 1.586
    ox, oy = W * 0.50, H * 0.06
    gap = H * 0.125
    defs = f"""<defs>
<linearGradient id='holo' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#FFD2B8' stop-opacity='.55'/><stop offset='.35' stop-color='{OR}' stop-opacity='.25'/><stop offset='.6' stop-color='#FFF4EC' stop-opacity='.45'/><stop offset='1' stop-color='{OR2}' stop-opacity='.25'/></linearGradient>
<linearGradient id='glass' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#ffffff' stop-opacity='.16'/><stop offset='1' stop-color='#ffffff' stop-opacity='.05'/></linearGradient>
<linearGradient id='core' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#2a1a12'/><stop offset='1' stop-color='#141010'/></linearGradient>
<linearGradient id='print' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#efe6de'/><stop offset='1' stop-color='#d9cfc6'/></linearGradient>
<linearGradient id='back' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#2c2c2c'/><stop offset='1' stop-color='#161616'/></linearGradient>
<filter id='blur'><feGaussianBlur stdDeviation='26'/></filter>
<filter id='soft'><feGaussianBlur stdDeviation='2'/></filter>
</defs>"""
    out = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}'>", defs]
    anchors = []
    # matrix mapping card-local (u,v) to iso plane for layer at screen lift L
    def M(L):
        a, b = 0.866 * s, 0.5 * s; c, d = -0.866 * s, 0.5 * s
        return f"matrix({a} {b} {c} {d} {ox:.1f} {oy + L:.1f})"
    layers = ["back", "prelam", "core", "clear", "perso", "overlay"]  # bottom -> top
    gx, gy = ox + (cw * 0.866 - cd * 0.866) / 2, oy + (cw * 0.5 + cd * 0.5) / 2 + gap * 5.4
    out.append(f"<ellipse cx='{gx:.0f}' cy='{gy:.0f}' rx='{W*0.33:.0f}' ry='{H*0.06:.0f}' fill='{OR}' opacity='.30' filter='url(#blur)'/>")
    R = cw * 0.045
    for i, kind in enumerate(layers):
        L = gap * (5 - i) + H * 0.02
        g = [f"<g transform='{M(L)}'>"]
        rect = f"<rect x='0' y='0' width='{cw:.1f}' height='{cd:.1f}' rx='{R:.1f}'"
        if kind == "back":
            g.append(rect + " fill='url(#back)' stroke='#555' stroke-width='1.2'/>")
            g.append(f"<rect x='0' y='{cd*0.12:.1f}' width='{cw:.1f}' height='{cd*0.16:.1f}' fill='#050505'/>")   # magnetic stripe
            for k in range(26):  # barcode
                wbar = 2 + (k * 7 % 5)
                g.append(f"<rect x='{cw*0.08 + k*9:.1f}' y='{cd*0.62:.1f}' width='{wbar}' height='{cd*0.22:.1f}' fill='#cfc7c0' opacity='.85'/>")
            for qx in range(7):
                for qy in range(7):
                    if (qx * 3 + qy * 5) % 3:
                        g.append(f"<rect x='{cw*0.78 + qx*7:.1f}' y='{cd*0.58 + qy*7:.1f}' width='6' height='6' fill='#cfc7c0' opacity='.85'/>")
        elif kind == "prelam":
            g.append(rect + " fill='#f3eee9' fill-opacity='.10' stroke='#bbb' stroke-opacity='.5' stroke-width='1.2'/>")
            for k in range(4):  # antenna coil
                m = 14 + k * 9
                g.append(f"<rect x='{m}' y='{m}' width='{cw-2*m:.1f}' height='{cd-2*m:.1f}' rx='{R*0.8:.1f}' fill='none' stroke='{OR}' stroke-width='3' stroke-opacity='.95'/>")
            g.append(f"<rect x='{cw*0.12:.1f}' y='{cd*0.36:.1f}' width='{cw*0.11:.1f}' height='{cd*0.24:.1f}' rx='6' fill='#E8A23A' stroke='#FFD39A' stroke-width='2'/>")
        elif kind == "core":
            g.append(rect + " fill='url(#core)' stroke='#7a3a20' stroke-width='1.4'/>")
            for k in range(30):  # guilloche-like waves on core (litho + digital print)
                pts = []
                for t in range(0, 101):
                    x = cw * t / 100
                    y = cd * 0.5 + math.sin(t / 100 * 6.28 * 3 + k * 0.21) * cd * 0.22 + (k - 15) * cd * 0.012
                    pts.append(f"{x:.1f},{y:.1f}")
                g.append(f"<polyline points='{' '.join(pts)}' fill='none' stroke='{OR}' stroke-opacity='.45' stroke-width='1.3'/>")
        elif kind == "clear":
            g.append(rect + " fill='url(#glass)' stroke='#ffffff' stroke-opacity='.55' stroke-width='1.4'/>")
        elif kind == "perso":
            g.append(rect + " fill='url(#print)' stroke='#fff' stroke-width='1.2'/>")
            g.append(f"<rect x='{cw*0.06:.1f}' y='{cd*0.18:.1f}' width='{cw*0.26:.1f}' height='{cd*0.66:.1f}' rx='6' fill='#8c8077'/>")
            g.append(f"<circle cx='{cw*0.19:.1f}' cy='{cd*0.40:.1f}' r='{cd*0.12:.1f}' fill='#b3a79d'/>")
            for k, ww in enumerate([0.42, 0.30, 0.36, 0.22, 0.30]):
                g.append(f"<rect x='{cw*0.38:.1f}' y='{cd*(0.22 + k*0.12):.1f}' width='{cw*ww:.1f}' height='{cd*0.05:.1f}' rx='3' fill='#5b5049'/>")
            g.append(f"<rect x='{cw*0.38:.1f}' y='{cd*0.06:.1f}' width='{cw*0.5:.1f}' height='{cd*0.07:.1f}' rx='3' fill='{OR}'/>")
        elif kind == "overlay":
            g.append(rect + " fill='url(#holo)' stroke='#FFD2B8' stroke-opacity='.8' stroke-width='1.6'/>")
            g.append(f"<circle cx='{cw*0.80:.1f}' cy='{cd*0.70:.1f}' r='{cd*0.15:.1f}' fill='{OR}' fill-opacity='.35' stroke='#FFE0CC' stroke-width='2'/>")
        g.append("</g>")
        out.extend(g)
        # anchors: right corner (u=cw, v=0) and left corner (u=0, v=cd)
        rx, ry = ox + cw * 0.866, oy + L + cw * 0.5
        lx, ly = ox - cd * 0.866, oy + L + cd * 0.5
        anchors.append({"kind": kind, "right": [rx / W, ry / H], "left": [lx / W, ly / H]})
    out.append("</svg>")
    ANCH[name] = anchors
    return "\n".join(out)

# ---------------------------------------------------------------- render
async def shoot(page, html, w, h, out, scale=2):
    tmp = ART / "_tmp"; tmp.mkdir(exist_ok=True)
    f = tmp / (out + ".html"); f.write_text(html, encoding="utf-8")
    await page.set_viewport_size({"width": w, "height": h})
    await page.goto(f.resolve().as_uri(), wait_until="load")
    await page.wait_for_timeout(500)
    await page.screenshot(path=str(ART / out), omit_background=True, full_page=False)
    print("rendered", out)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="msedge", headless=True, args=["--allow-file-access-from-files"])
        ctx = await b.new_context(device_scale_factor=2); page = await ctx.new_page()
        page.on("console", lambda m: print("  console:", m.type, m.text))
        page.on("pageerror", lambda e: print("  PAGEERROR:", e))
        await shoot(page, html_rosette(1400, 0), 1400, 1400, "guilloche_rosette.png", 1)
        await shoot(page, html_rosette(1400, 1), 1400, 1400, "guilloche_rosette2.png", 1)
        await shoot(page, html_waves(1920, 420), 1920, 420, "guilloche_waves.png")
        # cover: EG front forward-left, DE front behind-right
        await shoot(page, html_cards(1500, 1000, [
            dict(img="de_front.png", x=560, y=170, w=760, t="rotateX(16deg) rotateY(-24deg) rotateZ(8deg)", glow=50, ga=.30),
            dict(img="eg_front.png", ratio=1.629, x=150, y=380, w=780, t="rotateX(14deg) rotateY(22deg) rotateZ(-7deg)", glow=60, ga=.42),
        ]), 1500, 1000, "cover_cards.png")
        await shoot(page, html_cards(1500, 1000, [
            dict(img="de_back.png", x=560, y=170, w=760, t="rotateX(16deg) rotateY(-24deg) rotateZ(8deg)", glow=50, ga=.30),
            dict(img="eg_back.png", ratio=1.633, x=150, y=380, w=780, t="rotateX(14deg) rotateY(22deg) rotateZ(-7deg)", glow=60, ga=.42),
        ]), 1500, 1000, "closing_cards.png")
        for nm, img, ratio, t in [("float_eg_front.png", "eg_front.png", 1.629, "rotateX(10deg) rotateY(16deg) rotateZ(-5deg)"),
                                  ("float_de_front.png", "de_front.png", 1.587, "rotateX(10deg) rotateY(-16deg) rotateZ(5deg)"),
                                  ("float_eg_back.png", "eg_back.png", 1.633, "rotateX(10deg) rotateY(16deg) rotateZ(-5deg)"),
                                  ("float_de_back.png", "de_back.png", 1.583, "rotateX(10deg) rotateY(-16deg) rotateZ(5deg)")]:
            await shoot(page, html_cards(1200, 860, [dict(img=img, ratio=ratio, x=170, y=170, w=860, t=t, glow=50, ga=.38)]), 1200, 860, nm)
        # stacks
        await shoot(page, f"<html><body style='margin:0;background:transparent'>{svg_pyramid(1200, 1100, [dict(label='CARD BODY', hot=False), dict(label='PRINT', hot=False), dict(label='PERSONALIZE', hot=False), dict(label='FINISHING', hot=True)], 'pyramid_top')}</body></html>", 1200, 1100, "pyramid_top.png")
        await shoot(page, f"<html><body style='margin:0;background:transparent'>{svg_pyramid(1200, 1100, [dict(label='CARD BODY', hot=True), dict(label='PRINT', hot=True), dict(label='PERSONALIZE', hot=True), dict(label='FINISHING', hot=True)], 'pyramid_all')}</body></html>", 1200, 1100, "pyramid_all.png")
        await shoot(page, f"<html><body style='margin:0;background:transparent'>{svg_exploded(1300, 1250, 'exploded')}</body></html>", 1300, 1250, "exploded.png")
        await b.close()
    (ART / "anchors.json").write_text(json.dumps(ANCH, indent=1))

asyncio.run(main())
