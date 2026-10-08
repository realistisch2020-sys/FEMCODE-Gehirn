const {chromium}=require('playwright');
const OUT=process.argv[2];
// [teil1, teil2, nummer]
const S=[
 ['Du denkst<br>an <em>alle.</em>','Nur nicht<br><span class="sc">an dich?</span>',''],
 ['Ich muss mir Ruhe<br>nicht erst <em>verdienen.</em>','Ich darf sie mir<br><span class="sc">einfach nehmen.</span>','1'],
 ['Ein <em>Nein</em><br>zu anderen','ist manchmal<br>ein <span class="sc">Ja zu mir.</span>','2'],
 ['Ich bin nicht<br>verantwortlich<br>für die Gefühle<br>aller anderen.','Ich bin<br>verantwortlich<br>für <em>meine.</em>','3'],
 ['Bevor ich frage:<br>„Was brauchen<br><em>die anderen?</em>“','frage ich zuerst:<br>„Was brauche <span class="sc">ich?</span>“','4'],
 ['Mein schlechtes<br>Gewissen ist kein<br>Beweis, dass ich etwas<br><em>falsch</em> mache.','Es zeigt nur,<br>dass ich etwas<br><span class="sc">Neues lerne.</span>','5'],
 ['Ich höre auf,<br>mich <em>klein</em><br>zu machen,','nur damit es<br>für alle anderen<br><span class="sc">bequem bleibt.</span>','6'],
 ['Ich bin nicht nur<br>so viel wert,<br>wie ich <em>leiste.</em>','Ich bin wertvoll,<br><span class="sc">einfach so.</span>','7'],
 ['Müde sein<br>ist keine<br><em>Schwäche.</em>','Es ist mein Körper,<br>der sagt:<br><span class="sc">Jetzt bin ich dran.</span>','8'],
 ['Ab heute stehe ich<br>auch auf meiner<br><em>eigenen Liste.</em>','Nicht ganz unten.<br><span class="sc">Ganz oben.</span>','9'],
 ['Willst du alle<br>9 Sätze als <em>PDF?</em>','Kommentiere<br><span class="kw">LISTE</span><br><span class="small">und ich schicke sie dir.</span>',''],
];
const css=`body{margin:0}
.s{width:1080px;height:1920px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;
background:linear-gradient(160deg,#7A2251 0%,#5E1A3F 55%,#45122E 100%);font-family:'Fraunces',serif;color:#FFF5F8}
.s::before{content:"";position:absolute;width:900px;height:900px;border-radius:50%;right:-380px;top:-300px;background:#B8326A;opacity:.55}
.s::after{content:"";position:absolute;width:560px;height:560px;border-radius:50%;left:-260px;bottom:120px;background:#8E2A5C;opacity:.7}
.t{position:relative;z-index:1;font-size:96px;line-height:1.1;font-weight:400;padding:0 90px}
em{font-style:italic;color:#F7B7D0}
.sc{font-style:italic;color:#F7B7D0;font-weight:600}
.kw{display:inline-block;margin:30px 0;padding:14px 70px;background:#FFF5F8;border-radius:80px;letter-spacing:12px;color:#7A2251;font-family:'DM Sans',sans-serif;font-weight:700;font-size:.95em;font-style:normal}
.small{font-size:.55em;font-family:'DM Sans',sans-serif}
.d{position:relative;z-index:1;width:140px;height:8px;border-radius:8px;background:#F7B7D0;margin:70px 0;font-size:0}
.d span{display:none}
.n{position:absolute;top:300px;z-index:1;font-family:'DM Sans',sans-serif;font-weight:700;font-size:38px;letter-spacing:8px;color:#7A2251;background:#F7B7D0;padding:10px 34px;border-radius:40px}
.n:empty{display:none}
.hide{opacity:0}`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.setContent(`<html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400;1,9..144,600&family=DM+Sans:wght@400;700&display=swap" rel="stylesheet"><style>${css}</style></head><body><div class="s"><div class="n" id="n"></div><div class="t" id="a"></div><div class="d" id="d"><span></span>♡<span></span></div><div class="t" id="b"></div></div></body></html>`,{waitUntil:'networkidle'});
await p.evaluate(()=>document.fonts.ready);
let i=0;
for(const [a,bb,n] of S){for(const st of ['a','b']){
 await p.evaluate(([a,bb,n,st])=>{document.getElementById('a').innerHTML=a;document.getElementById('b').innerHTML=bb;
 document.getElementById('n').textContent=n?n+' / 9':'';
 document.getElementById('b').className='t'+(st==='a'?' hide':'');document.getElementById('d').className='d'+(st==='a'?' hide':'');},[a,bb,n,st]);
 await p.screenshot({path:`${OUT}/f${String(i++).padStart(2,'0')}.png`});}}
await b.close();console.log(i)})();
