const {chromium}=require('playwright');
// ===== HIER EINTRAGEN =====
const NAME='Petra Tanner';
const AUTORLINK='https://www.amazon.de/s?k=Petra+Tanner&i=stripbooks';
const EMAIL='info.safetothrive@gmail.com';
const INSTA='@petratanner.autorin';
// ==========================
const H=[
['Kollegin: „Kannst du das noch schnell übernehmen?“','„Heute schaffe ich das nicht. Morgen ab 10 Uhr schaue ich es mir gern an.“'],
['Familie: „Du kommst doch am Sonntag?“','„Dieses Wochenende bleibe ich zu Hause. Ich brauche Ruhe.“'],
['Freundin: „Hilfst du mir beim Umzug?“','„Diesmal nicht. Ich drücke dir die Daumen, dass alles gut klappt.“'],
['Partner: „Machst du das eben?“','„Ich mache heute schon das Abendessen. Übernimmst du das?“'],
['Kinder: „Mama, kannst du mal …?“','„Ich trinke gerade meinen Kaffee. In zehn Minuten bin ich für dich da.“'],
['Schule / Verein: „Wir suchen noch jemanden für …“','„Danke, dass ihr an mich denkt. Dieses Mal sage ich ab.“'],
];
const S=[
['Ich muss mir Ruhe nicht erst <em>verdienen.</em> Ich darf sie mir einfach nehmen.','Wann hast du dir zuletzt Ruhe erlaubt, ohne sie vorher „abzuarbeiten“?'],
['Ein <em>Nein</em> zu anderen ist manchmal ein Ja zu mir.','Zu welcher Bitte möchtest du diese Woche Nein sagen?'],
['Ich bin nicht verantwortlich für die Gefühle aller anderen. Ich bin verantwortlich für <em>meine.</em>','Wessen Enttäuschung versuchst du gerade zu verhindern – und was kostet dich das?'],
['Bevor ich frage „Was brauchen die anderen?“, frage ich zuerst: „Was brauche <em>ich?</em>“','Was brauchst du heute? Ein Satz reicht.'],
['Mein schlechtes Gewissen ist kein Beweis, dass ich etwas falsch mache. Es zeigt nur, dass ich etwas <em>Neues lerne.</em>','Wann hattest du zuletzt ein schlechtes Gewissen, obwohl du nichts Falsches getan hast?'],
['Ich höre auf, mich <em>klein</em> zu machen, nur damit es für alle anderen bequem bleibt.','Wo machst du dich klein, damit es für andere leichter ist?'],
['Ich bin nicht nur so viel wert, wie ich leiste. Ich bin <em>wertvoll, einfach so.</em>','Was magst du an dir, das nichts mit Leistung zu tun hat?'],
['Müde sein ist keine Schwäche. Es ist mein Körper, der sagt: <em>Jetzt bin ich dran.</em>','Was will dir deine Müdigkeit gerade sagen?'],
['Ab heute stehe ich auch auf meiner eigenen Liste. Nicht ganz unten. <em>Ganz oben.</em>','Was kommt diese Woche ganz oben auf deine Liste?'],
];
const card=(s,i)=>`<div class="c"><div class="no">${i+1}</div><p class="q">${s[0]}</p><p class="f"><b>Frag dich:</b> ${s[1]}</p><div class="l"></div><div class="l"></div></div>`;
const html=`<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Great+Vibes&display=swap" rel="stylesheet"><style>
@page{size:A4;margin:0}
body{margin:0;font-family:'Cormorant Garamond',serif;color:#2b2118}
.p{width:210mm;height:297mm;box-sizing:border-box;padding:22mm 22mm;page-break-after:always;position:relative;background:linear-gradient(160deg,#fbf5ea,#f3e6cd)}
.p:last-child{page-break-after:auto}
.cover{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:radial-gradient(ellipse at 70% 30%,#fbf3e4,#f1e2c6 55%,#e2c99d)}
h1{font-size:64pt;font-weight:500;margin:0;line-height:1}
.sc{font-family:'Great Vibes',cursive;color:#a8782c;font-weight:400}
.sub{font-size:20pt;margin-top:10mm;line-height:1.3}
.by{position:absolute;bottom:22mm;font-size:13pt;letter-spacing:5px;text-transform:uppercase;color:#8a6a3a}
.d{color:#a8782c;font-size:22pt;margin:8mm 0}
h2{font-size:30pt;font-weight:500;margin:0 0 6mm}
p,li{font-size:14.5pt;line-height:1.5}
em{color:#a8782c;font-style:italic;font-weight:600}
.c{border-top:1px solid #c9a46a;padding:6mm 0 4mm;position:relative}
.no{position:absolute;left:0;top:5mm;font-family:'Great Vibes';font-size:34pt;color:#a8782c}
.q{font-size:19pt;line-height:1.3;margin:0 0 3mm 16mm}
.f{margin:0 0 2mm 16mm;font-size:13.5pt;color:#5a4630}
.l{margin-left:16mm;border-bottom:1px dotted #b8955a;height:9mm}
.box{border:1.5px solid #c9a46a;border-radius:4mm;padding:4mm 6mm;margin-top:6mm;background:rgba(255,255,255,.4)}
.big{border-bottom:1px dotted #b8955a;height:12mm}
a{color:#a8782c}
.foot{position:absolute;bottom:12mm;left:22mm;right:22mm;text-align:center;font-size:10pt;color:#8a6a3a}
</style></head><body>
<div class="p cover"><h1>9 Sätze</h1><div class="sc" style="font-size:54pt">für dich</div><div class="d">— ♡ —</div><div class="sub">Für Frauen, die immer an alle denken.<br>Nur nicht an sich.</div><div class="by">${NAME}</div></div>
<div class="p"><h2>Bevor du anfängst</h2>
<p>Du bist es gewohnt, für andere da zu sein. Du merkst, was andere brauchen, bevor sie es aussprechen. Und irgendwo ganz unten auf der Liste stehst du.</p>
<p>Dazu bekommst du Satzhilfen, mit denen du Nein sagen kannst, ohne dich zu rechtfertigen. Diese 9 Sätze sind keine Zauberformeln. Sie sind kleine Erinnerungen daran, dass du auch zählst.</p>
<div class="box"><p style="margin:0"><b>So nutzt du sie:</b></p><ul style="margin:2mm 0">
<li>Nimm dir <b>einen Satz pro Tag.</b> Lies ihn morgens laut.</li>
<li>Beantworte die <b>Frage darunter</b> mit nur einem Satz. Ehrlich, nicht schön.</li>
<li>Schreib den Satz, der dich am meisten trifft, auf einen Zettel oder mach ihn zu deinem Handy-Hintergrund.</li>
<li>Wenn dein schlechtes Gewissen sich meldet: Das ist normal. Mach trotzdem weiter.</li></ul></div>
<div class="foot">9 Sätze für dich · ${NAME}</div></div>
<div class="p">${S.slice(0,3).map(card).join('')}<div class="foot">9 Sätze für dich · ${NAME}</div></div>
<div class="p">${S.slice(3,6).map((s,i)=>card(s,i+3)).join('')}<div class="foot">9 Sätze für dich · ${NAME}</div></div>
<div class="p">${S.slice(6,9).map((s,i)=>card(s,i+6)).join('')}<div class="foot">9 Sätze für dich · ${NAME}</div></div>
<div class="p"><h2>Nein sagen <span class="sc" style="font-size:30pt">ohne Rechtfertigung</span></h2>
<p>Ein Nein braucht keine lange Erklärung. Je mehr du dich rechtfertigst, desto mehr lädst du zum Verhandeln ein. <b>Kurz, freundlich, klar</b> reicht.</p>
<div class="box"><p style="margin:0"><b>Der wichtigste Satz zuerst – er verhindert das automatische Ja:</b></p>
<p style="font-size:19pt;margin:2mm 0"><em>„Ich schaue in meinen Kalender und sage dir morgen Bescheid.“</em></p>
<p style="margin:0;font-size:12.5pt">So hast du Zeit zu spüren, ob du wirklich willst.</p></div>
${H.map(h=>`<div class="c" style="padding:3.5mm 0"><p class="f" style="margin:0">${h[0]}</p><p class="q" style="font-size:16pt;margin:1mm 0 0 0">${h[1]}</p></div>`).join('')}
<div class="foot">9 Sätze für dich · ${NAME}</div></div>
<div class="p"><h2>Wenn jemand nachhakt</h2>
<p>Manche Menschen sind es gewohnt, dass du nachgibst. Bleib einfach freundlich bei deiner Antwort:</p>
<div class="box"><p style="font-size:18pt;margin:1mm 0"><em>„Ich verstehe, dass das blöd für dich ist. Meine Antwort bleibt trotzdem Nein.“</em></p>
<p style="font-size:18pt;margin:3mm 0 1mm"><em>„Das passt für mich gerade nicht.“</em> – und dann nichts mehr hinzufügen.</p></div>
<h2 style="margin-top:10mm;font-size:24pt">Was du weglassen darfst</h2>
<ul><li>Lange Entschuldigungen („Es tut mir so leid, aber …“)</li><li>Ausreden, die du dir erst ausdenken musst</li><li>Versprechen fürs nächste Mal, die du gar nicht willst</li><li>Das schlechte Gewissen danach. Es darf da sein, es muss aber nicht entscheiden.</li></ul>
<div class="box"><p style="margin:0"><b>Mein Nein-Satz für diese Woche:</b></p><div class="big"></div></div>
<div class="foot">9 Sätze für dich · ${NAME}</div></div>
<div class="p"><h2>Meine eigene Liste <span class="sc" style="font-size:30pt">diese Woche</span></h2>
<p>Drei Dinge, die ich diese Woche <b>nur für mich</b> tue. Nicht für die Familie, nicht für die Arbeit. Für mich.</p>
<div class="box"><p style="margin:0">1.</p><div class="big"></div><p style="margin:3mm 0 0">2.</p><div class="big"></div><p style="margin:3mm 0 0">3.</p><div class="big"></div></div>
<p style="margin-top:8mm">Und eine Sache, zu der ich diese Woche <b>Nein</b> sage:</p><div class="big"></div>
<div class="foot">9 Sätze für dich · ${NAME}</div></div>
<div class="p" style="display:flex;flex-direction:column;justify-content:center"><h2>Wenn dich diese Sätze berührt haben …</h2>
<p>… dann bist du vielleicht schon sehr lange für alle da. Genau dafür habe ich mein Buch geschrieben:</p>
<div class="box" style="text-align:center"><p style="font-size:24pt;margin:2mm 0;line-height:1.2"><em>„Ich stand nie auf meiner eigenen Liste“</em></p><p style="margin:0">Du hast an alle gedacht. Nur nicht an dich.</p></div>
<ul><li>30+ kurze Kapitel, die du auch an vollen Tagen schaffst</li><li>Übungen und ein Schritt pro Woche</li><li>Satzhilfen für Momente, in denen du sonst automatisch Ja sagst</li></ul>
<p>Erkenne wieder, was du selbst brauchst, bevor du automatisch Ja sagst.</p>
<p style="font-size:17pt;text-align:center;margin-top:6mm">Jetzt auf Amazon:<br>Taschenbuch: <a href="https://www.amazon.de/dp/B0HGT4PX8H">amazon.de/dp/B0HGT4PX8H</a><br>Kindle: <a href="https://www.amazon.de/dp/B0HGSBZS18">amazon.de/dp/B0HGSBZS18</a></p>
<div class="box" style="text-align:center;margin-top:10mm"><p style="margin:0 0 2mm"><b>Alle meine Bücher:</b> <a href="${AUTORLINK}">auf Amazon „Petra Tanner“</a></p>
<p style="margin:0">${NAME} · <a href="mailto:${EMAIL}">${EMAIL}</a> · Instagram ${INSTA}</p></div>
<div class="foot">9 Sätze für dich · ${NAME}</div></div>
</body></html>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.setContent(html,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:process.argv[2],format:'A4',printBackground:true});
await p.setViewportSize({width:794,height:1123});await p.screenshot({path:'pdfprev.png',fullPage:true});await b.close()})();
