// Gratis-PDF „9 Sätze für dich“ – Design: modern, Beerentöne
// Neu erzeugen: NODE_PATH=$(npm root -g) node pdf-generator.js <ziel.pdf>
const {chromium}=require('playwright');
// ===== HIER EINTRAGEN =====
const NAME='Petra Tanner';
const AUTORLINK='https://www.amazon.de/s?k=Petra+Tanner&i=stripbooks';
const EMAIL='info.safetothrive@gmail.com';
const INSTA='@petratanner.autorin';
const TB='https://www.amazon.de/gp/aws/cart/add.html?ASIN.1=B0HGT4PX8H&Quantity.1=1', KINDLE='https://www.amazon.de/dp/B0HGSBZS18';
// ==========================
const S=[
['Ich muss mir Ruhe nicht erst verdienen.','Ich darf sie mir einfach nehmen.','Wann hast du dir zuletzt Ruhe erlaubt, ohne sie vorher „abzuarbeiten“?'],
['Ein Nein zu anderen','ist manchmal ein Ja zu mir.','Zu welcher Bitte möchtest du diese Woche Nein sagen?'],
['Ich bin nicht verantwortlich für die Gefühle aller anderen.','Ich bin verantwortlich für meine.','Wessen Enttäuschung versuchst du gerade zu verhindern – und was kostet dich das?'],
['Bevor ich frage „Was brauchen die anderen?“,','frage ich zuerst: „Was brauche ich?“','Was brauchst du heute? Ein Satz reicht.'],
['Mein schlechtes Gewissen ist kein Beweis, dass ich etwas falsch mache.','Es zeigt nur, dass ich etwas Neues lerne.','Wann hattest du zuletzt ein schlechtes Gewissen, obwohl du nichts Falsches getan hast?'],
['Ich höre auf, mich klein zu machen,','nur damit es für alle anderen bequem bleibt.','Wo machst du dich klein, damit es für andere leichter ist?'],
['Ich bin nicht nur so viel wert, wie ich leiste.','Ich bin wertvoll, einfach so.','Was magst du an dir, das nichts mit Leistung zu tun hat?'],
['Müde sein ist keine Schwäche.','Es ist mein Körper, der sagt: Jetzt bin ich dran.','Was will dir deine Müdigkeit gerade sagen?'],
['Ab heute stehe ich auch auf meiner eigenen Liste.','Nicht ganz unten. Ganz oben.','Was kommt diese Woche ganz oben auf deine Liste?'],
];
const H=[
['Kollegin','„Kannst du das noch schnell übernehmen?“','„Heute schaffe ich das nicht. Morgen ab 10 Uhr schaue ich es mir gern an.“'],
['Familie','„Du kommst doch am Sonntag?“','„Dieses Wochenende bleibe ich zu Hause. Ich brauche Ruhe.“'],
['Freundin','„Hilfst du mir beim Umzug?“','„Diesmal nicht. Ich drücke dir die Daumen, dass alles gut klappt.“'],
['Partner','„Machst du das eben?“','„Ich mache heute schon das Abendessen. Übernimmst du das?“'],
['Kinder','„Mama, kannst du mal …?“','„Ich trinke gerade meinen Kaffee. In zehn Minuten bin ich für dich da.“'],
['Schule / Verein','„Wir suchen noch jemanden für …“','„Danke, dass ihr an mich denkt. Dieses Mal sage ich ab.“'],
];
const foot=n=>`<div class="foot"><span>9 Sätze für dich</span><span>${NAME} · ${INSTA}</span><span>${String(n).padStart(2,'0')}</span></div>`;
const card=(s,i)=>`<div class="card"><div class="num">${String(i+1).padStart(2,'0')}</div><div class="cb"><p class="q">${s[0]} <b>${s[1]}</b></p><p class="ask"><span class="tag">Frag dich</span>${s[2]}</p><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>`;
const html=`<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet"><style>
:root{--berry:#6B1D46;--rasp:#B8326A;--blush:#F6E3EB;--cream:#FFF9F6;--ink:#2A1420;--muted:#7A5A68}
@page{size:A4;margin:0}
body{margin:0;font-family:'DM Sans',sans-serif;color:var(--ink)}
.p{width:210mm;height:297mm;box-sizing:border-box;padding:20mm 20mm 24mm;page-break-after:always;position:relative;background:var(--cream);overflow:hidden}
.p:last-child{page-break-after:auto}
h1,h2,.q,.serif{font-family:'Fraunces',serif}
.eyebrow{font-size:9.5pt;letter-spacing:3px;text-transform:uppercase;color:var(--rasp);font-weight:700;margin-bottom:4mm}
h2{font-size:30pt;font-weight:400;line-height:1.08;margin:0 0 7mm;color:var(--berry)}
h2 i{color:var(--rasp)}
p,li{font-size:11.5pt;line-height:1.6}
.cover{background:var(--berry);color:#fff;padding:0}
.cover .blob{position:absolute;border-radius:50%}
.cover .b1{width:150mm;height:150mm;right:-45mm;top:-40mm;background:var(--rasp);opacity:.9}
.cover .b2{width:90mm;height:90mm;left:-30mm;bottom:30mm;background:#8E2A5C}
.cover .in{position:absolute;left:20mm;right:20mm;bottom:38mm}
.cover h1{font-size:76pt;font-weight:400;line-height:.95;margin:0}
.cover h1 i{color:var(--blush)}
.cover .sub{font-size:15pt;margin-top:8mm;line-height:1.45;max-width:130mm;opacity:.95}
.cover .pill{display:inline-block;border:1.5px solid rgba(255,255,255,.7);border-radius:30px;padding:2mm 6mm;font-size:9.5pt;letter-spacing:2.5px;text-transform:uppercase;margin-bottom:10mm}
.cover .by{position:absolute;left:20mm;bottom:16mm;font-size:10pt;letter-spacing:3px;text-transform:uppercase;opacity:.85}
.panel{background:var(--blush);border-radius:6mm;padding:7mm 8mm;margin-top:7mm}
.panel ol{margin:2mm 0 0;padding-left:6mm}.panel li{margin-bottom:2mm}
.card{display:flex;gap:6mm;padding:9mm 0;border-top:1.5px solid var(--blush)}
.card:first-of-type{border-top:none}
.num{font-family:'Fraunces';font-size:34pt;color:var(--rasp);line-height:.9;width:18mm;flex:none}
.q{font-size:20pt;line-height:1.3;margin:0 0 4mm;font-weight:400}
.q b{font-weight:600;color:var(--berry);font-style:italic}
.ask{font-size:11.5pt;margin:0;color:var(--muted)}
.tag{display:inline-block;background:var(--berry);color:#fff;border-radius:20px;padding:.5mm 3mm;font-size:8pt;letter-spacing:1.5px;text-transform:uppercase;margin-right:2.5mm;font-weight:700;vertical-align:1px}
.ln{border-bottom:1.5px dashed #E2B9CA;height:10mm}
.ln2{border-bottom:1.5px dashed #E2B9CA;height:11mm}
.key{background:var(--berry);color:#fff;border-radius:6mm;padding:7mm 8mm;margin:2mm 0 6mm}
.key .serif{font-size:18pt;line-height:1.3;margin:2mm 0}
.key small{opacity:.8;font-size:9.5pt}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.h{background:#fff;border:1.5px solid var(--blush);border-radius:4mm;padding:4mm 5mm}
.h .who{font-size:8pt;letter-spacing:2px;text-transform:uppercase;color:var(--rasp);font-weight:700}
.h .ask2{font-size:10pt;color:var(--muted);margin:1.5mm 0}
.h .ans{font-family:'Fraunces';font-size:12.5pt;line-height:1.35;color:var(--berry)}
ul.x{list-style:none;padding:0}ul.x li{padding-left:7mm;position:relative;margin-bottom:2mm}ul.x li:before{content:"×";position:absolute;left:0;color:var(--rasp);font-weight:700}
ul.c{list-style:none;padding:0}ul.c li{padding-left:7mm;position:relative;margin-bottom:2mm}ul.c li:before{content:"✓";position:absolute;left:0;color:var(--rasp);font-weight:700}
.book{background:var(--berry);color:#fff}
.book h2{color:#fff}.book h2 i{color:#F2B8CF}
.btn{display:block;text-align:center;background:var(--rasp);color:#fff;text-decoration:none;border-radius:30px;padding:4mm;font-weight:700;font-size:12pt;margin-top:3mm}
.btn.o{background:transparent;border:1.5px solid #fff}
.bookcard{background:rgba(255,255,255,.08);border-radius:6mm;padding:7mm 8mm;margin:6mm 0}
.contact{position:absolute;left:20mm;right:20mm;bottom:22mm;border-top:1px solid rgba(255,255,255,.3);padding-top:5mm;font-size:10pt;display:flex;justify-content:space-between}
.contact a{color:#fff}
.foot{position:absolute;left:20mm;right:20mm;bottom:10mm;display:flex;justify-content:space-between;font-size:8pt;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted)}
.book .foot{color:rgba(255,255,255,.6)}
</style></head><body>

<div class="p cover"><div class="blob b1"></div><div class="blob b2"></div>
<div class="in"><div class="pill">Gratis-Workbook</div><h1>9 Sätze<br><i>für dich.</i></h1>
<div class="sub">Für Frauen, die immer an alle denken. Nur nicht an sich. Mit Fragen, Satzhilfen zum Neinsagen und einer Übung für diese Woche.</div></div>
<div class="by">${NAME}</div></div>

<div class="p"><div class="eyebrow">Bevor du anfängst</div><h2>Du zählst <i>auch.</i></h2>
<p>Du bist es gewohnt, für andere da zu sein. Du merkst, was andere brauchen, bevor sie es aussprechen. Und irgendwo ganz unten auf der Liste stehst du.</p>
<p>Diese 9 Sätze sind keine Zauberformeln. Sie sind kleine Erinnerungen daran, dass du auch zählst. Dazu bekommst du Satzhilfen, mit denen du Nein sagen kannst, ohne dich zu rechtfertigen.</p>
<div class="panel"><b>So nutzt du das Workbook</b><ol>
<li><b>Ein Satz pro Tag.</b> Lies ihn morgens laut.</li>
<li><b>Beantworte die Frage</b> darunter mit nur einem Satz. Ehrlich, nicht schön.</li>
<li><b>Mach den Satz, der dich am meisten trifft,</b> zu deinem Handy-Hintergrund.</li>
<li><b>Wenn sich dein schlechtes Gewissen meldet:</b> normal. Mach trotzdem weiter.</li></ol></div>
<div class="panel" style="background:#fff;border:1.5px solid var(--blush)"><b>Was dich erwartet</b>
<ul class="c" style="margin:2mm 0 0"><li>9 Sätze mit je einer Frage</li><li>Satzhilfen: Nein sagen in 6 Alltagssituationen</li><li>Was tun, wenn jemand nachhakt</li><li>Übung „Meine eigene Liste“</li></ul></div>
${foot(2)}</div>

<div class="p"><div class="eyebrow">Satz 1 – 3</div>${S.slice(0,3).map((s,i)=>card(s,i)).join('')}${foot(3)}</div>
<div class="p"><div class="eyebrow">Satz 4 – 6</div>${S.slice(3,6).map((s,i)=>card(s,i+3)).join('')}${foot(4)}</div>
<div class="p"><div class="eyebrow">Satz 7 – 9</div>${S.slice(6,9).map((s,i)=>card(s,i+6)).join('')}${foot(5)}</div>

<div class="p"><div class="eyebrow">Satzhilfen</div><h2>Nein sagen <i>ohne Rechtfertigung.</i></h2>
<p style="margin-top:-2mm">Je mehr du dich rechtfertigst, desto mehr lädst du zum Verhandeln ein. Kurz, freundlich, klar reicht.</p>
<div class="key"><small>DER WICHTIGSTE SATZ – ER STOPPT DAS AUTOMATISCHE JA</small><div class="serif">„Ich schaue in meinen Kalender und sage dir morgen Bescheid.“</div><small>So hast du Zeit zu spüren, ob du wirklich willst.</small></div>
<div class="grid">${H.map(h=>`<div class="h"><div class="who">${h[0]}</div><div class="ask2">${h[1]}</div><div class="ans">${h[2]}</div></div>`).join('')}</div>
${foot(6)}</div>

<div class="p"><div class="eyebrow">Satzhilfen</div><h2>Wenn jemand <i>nachhakt.</i></h2>
<p>Manche Menschen sind es gewohnt, dass du nachgibst. Bleib freundlich bei deiner Antwort:</p>
<div class="key"><div class="serif">„Ich verstehe, dass das blöd für dich ist. Meine Antwort bleibt trotzdem Nein.“</div></div>
<div class="key" style="background:var(--rasp)"><div class="serif">„Das passt für mich gerade nicht.“</div><small>Und dann nichts mehr hinzufügen.</small></div>
<h2 style="font-size:20pt;margin-top:8mm">Was du <i>weglassen</i> darfst</h2>
<ul class="x"><li>Lange Entschuldigungen („Es tut mir so leid, aber …“)</li><li>Ausreden, die du dir erst ausdenken musst</li><li>Versprechen fürs nächste Mal, die du gar nicht willst</li><li>Das schlechte Gewissen danach. Es darf da sein, aber es muss nicht entscheiden.</li></ul>
<div class="panel"><b>Mein Nein-Satz für diese Woche</b><div class="ln2"></div></div>
${foot(7)}</div>

<div class="p"><div class="eyebrow">Übung</div><h2>Meine eigene Liste <i>diese Woche.</i></h2>
<p>Drei Dinge, die ich diese Woche <b>nur für mich</b> tue. Nicht für die Familie, nicht für die Arbeit. Für mich.</p>
${[1,2,3].map(n=>`<div class="card" style="border-top:1.5px solid var(--blush)"><div class="num">${n}</div><div class="cb" style="flex:1"><div class="ln2"></div></div></div>`).join('')}
<div class="panel" style="margin-top:8mm"><b>Und eine Sache, zu der ich diese Woche Nein sage:</b><div class="ln2"></div></div>
<div class="panel" style="background:#fff;border:1.5px solid var(--blush)"><b>Am Ende der Woche:</b> Wie hat es sich angefühlt, auf deiner eigenen Liste zu stehen?<div class="ln2"></div></div>
${foot(8)}</div>

<div class="p book"><div class="eyebrow" style="color:#F2B8CF">Wenn dich diese Sätze berührt haben</div>
<h2>Dann bist du vielleicht schon <i>sehr lange</i> für alle da.</h2>
<p>Genau dafür habe ich mein Buch geschrieben.</p>
<div class="bookcard"><div class="serif" style="font-size:24pt;line-height:1.15">„Ich stand nie auf meiner eigenen Liste“</div>
<p style="opacity:.85;margin:2mm 0 4mm">Du hast an alle gedacht. Nur nicht an dich.</p>
<ul class="c" style="margin:0"><li>30+ kurze Kapitel, die du auch an vollen Tagen schaffst</li><li>Übungen und ein Schritt pro Woche</li><li>Satzhilfen für Momente, in denen du sonst automatisch Ja sagst</li></ul></div>
<a class="btn" href="${TB}">Taschenbuch jetzt bestellen · 12,99 € →</a>
<a class="btn o" href="${KINDLE}">Kindle sofort lesen · 7,99 € →</a>
<p style="font-size:9pt;opacity:.75;text-align:center;margin-top:3mm">Taschenbuch: Klick legt das Buch direkt in deinen Amazon-Warenkorb.<br>Ohne Klick: amazon.de/dp/B0HGT4PX8H (Taschenbuch) · amazon.de/dp/B0HGSBZS18 (Kindle)</p>
<div class="contact"><span><a href="${AUTORLINK}">Alle meine Bücher</a></span><span><a href="mailto:${EMAIL}">${EMAIL}</a></span><span>${INSTA}</span></div>
${foot(9)}</div>
<div class="p"><div class="eyebrow">Alle meine Bücher</div><h2>Für jedes Muster <i>das passende Buch.</i></h2>
<p>Alle Bücher findest du auf Amazon. Ein Klick auf den Titel öffnet das Buch.</p>
${[
['Ich stand nie auf meiner eigenen Liste','Du hast an alle gedacht. Nur nicht an dich.','https://www.amazon.de/dp/B0HGT4PX8H'],
['Deine Reaktion gehört dir. Nicht mir.','Warum du aufhören darfst, für die Gefühle anderer verantwortlich zu sein','https://www.amazon.de/dp/B0HHBDG1Y7'],
['Wenn Beziehungen erschöpfen','','https://www.amazon.de/dp/B0H9J886MQ'],
['Das schlechte Gewissen','','https://www.amazon.de/s?k=Petra+Tanner+Das+schlechte+Gewissen&i=stripbooks'],
['Ich bin so müde und niemand fragt mich warum','','https://www.amazon.de/dp/B0HBQ26552'],
['Du brauchst kein letztes Gespräch','Wie du innerlich frei wirst, auch wenn die Entschuldigung nie kommt','https://www.amazon.de/dp/B0HK86W8T4'],
].map((b,n)=>`<a href="${b[2]}" style="text-decoration:none;color:inherit"><div class="card" style="border-top:1.5px solid var(--blush);padding:6mm 0"><div class="num" style="font-size:26pt">${String(n+1).padStart(2,'0')}</div><div class="cb"><p class="q" style="font-size:17pt;margin:0">${b[0]} <span style="color:var(--rasp)">→</span></p>${b[1]?`<p class="ask" style="margin-top:1mm">${b[1]}</p>`:''}</div></div></a>`).join('')}
<p style="margin-top:6mm;color:var(--muted);font-size:10.5pt">${NAME} · Safe to Thrive</p>
${foot(10)}</div>
</body></html>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.setContent(html,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:process.argv[2],format:'A4',printBackground:true});await b.close()})();
