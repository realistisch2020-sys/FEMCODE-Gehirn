// Funnel-Übersicht als Bild. NODE_PATH=$(npm root -g) node funnel-grafik.js <ziel.png>
const {chromium}=require('playwright');
const steps=[
['01','Reel','„9 Sätze“ auf Instagram + Facebook','Reichweite',100],
['02','Kommentar „LISTE“','Automatische Antwort + DM (ManyChat)','Interesse',84],
['03','Gratis-PDF','Download über Tentary, E-Mail wird gesammelt','Kontakt',68],
['04','DM nach 23 h','Sanfter Hinweis auf das Buch','Vertrauen',52],
['05','Buch auf Amazon','„Ich stand nie auf meiner eigenen Liste“','Kauf',36],
];
const html=`<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;1,9..144,400&family=DM+Sans:wght@400;700&display=swap" rel="stylesheet"><style>
body{margin:0}.w{width:1080px;height:1350px;box-sizing:border-box;padding:80px 70px;background:#FFF9F6;font-family:'DM Sans',sans-serif;color:#2A1420}
.e{font-size:22px;letter-spacing:5px;text-transform:uppercase;color:#B8326A;font-weight:700}
h1{font-family:'Fraunces';font-weight:400;font-size:64px;color:#6B1D46;margin:14px 0 50px;line-height:1.05}h1 i{color:#B8326A}
.r{display:flex;align-items:center;margin-bottom:22px}
.bar{height:170px;border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 34px;box-sizing:border-box;color:#fff;margin:0 auto}
.n{font-family:'Fraunces';font-size:54px;opacity:.75}
.t{font-size:32px;font-weight:700}.s{font-size:21px;opacity:.88;margin-top:6px}
.k{font-size:16px;letter-spacing:3px;text-transform:uppercase;font-weight:700;opacity:.8;margin-bottom:6px}
.f{margin-top:36px;text-align:center;font-size:22px;color:#7A5A68}
</style></head><body><div class="w"><div class="e">Funnel · Petra Tanner</div><h1>Vom Reel <i>zum Buch.</i></h1>
${steps.map((s,i)=>{const c=['#B8326A','#A02B5F','#8B2655','#76204B','#5E1A3F'][i];return `<div class="r"><div class="bar" style="width:${[940,830,720,620,560][i]}px;background:${c}"><div class="n">${s[0]}</div><div><div class="k">${s[3]}</div><div class="t">${s[1]}</div><div class="s">${s[2]}</div></div></div></div>`}).join('')}
<div class="f">Messen nach 7 Tagen: Aufrufe · Kommentare · DMs · Downloads · Buchverkäufe</div></div></body></html>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});await p.setContent(html,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:process.argv[2]});await b.close()})();
