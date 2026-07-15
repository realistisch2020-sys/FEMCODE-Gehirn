const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const path = require('path');

function dailyPage() {
  return `
  <div class="page daily-page">
    <div class="top-bar">
      <div class="date-field">DATE <span class="date-line"></span></div>
      <div class="energy-mood">
        <span class="em-label">ENERGY</span>
        <span class="circles"><span class="circle"></span><span class="circle"></span><span class="circle"></span><span class="circle"></span><span class="circle"></span></span>
        <span class="mood-row">MOOD &nbsp; 😴 &nbsp; 😐 &nbsp; 🙂 &nbsp; ⚡ &nbsp; 🔥</span>
      </div>
    </div>

    <div class="section brain-dump-section">
      <div class="section-header">🧠 BRAIN DUMP — Get it out of your head first</div>
      <div class="lines-4">
        <div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div>
      </div>
    </div>

    <div class="two-col">
      <div class="col-left">
        <div class="section-header dark">⭐ TOP 3 PRIORITIES</div>
        <div class="priority"><span class="pnum">1</span><div class="pline"></div></div>
        <div class="priority"><span class="pnum">2</span><div class="pline"></div></div>
        <div class="priority"><span class="pnum">3</span><div class="pline"></div></div>
        <div style="height:8px"></div>
        <div class="section-header mid">📋 ADDITIONAL TASKS</div>
        <div class="line"></div><div class="line"></div><div class="line"></div>
        <div class="line"></div><div class="line"></div><div class="line"></div>
        <div class="line"></div><div class="line"></div>
      </div>
      <div class="col-right">
        <div class="section-header dark">⏰ TIME BLOCKS</div>
        <div class="time-grid">
          <div class="ts"><span class="tl">6:00 AM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">7:00 AM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">8:00 AM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">9:00 AM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">10:00 AM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">11:00 AM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">12:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">1:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">2:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">3:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">4:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">5:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">6:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">7:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">8:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">9:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">10:00 PM</span><div class="tline"></div></div>
          <div class="ts"><span class="tl">Evening</span><div class="tline"></div></div>
        </div>
      </div>
    </div>

    <div class="section habits-section">
      <div class="section-header dark">✅ DAILY HABITS</div>
      <div class="habit-grid">
        <div class="habit"><span class="cb"></span>Medication / Supplements</div>
        <div class="habit"><span class="cb"></span>8 Glasses of Water</div>
        <div class="habit"><span class="cb"></span>Movement / Exercise</div>
        <div class="habit"><span class="cb"></span>Healthy Meal</div>
        <div class="habit"><span class="cb"></span>Fresh Air / Outside</div>
        <div class="habit"><span class="cb"></span>Sleep by 11pm</div>
        <div class="habit"><span class="cb"></span>______________________</div>
        <div class="habit"><span class="cb"></span>______________________</div>
      </div>
    </div>

    <div class="two-col bottom-row">
      <div class="col-left">
        <div class="section-header mid">📝 NOTES / OVERFLOW</div>
        <div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div>
      </div>
      <div class="col-right">
        <div class="win-box">
          <div class="win-label">🌟 WIN OF THE DAY</div>
          <div class="win-line"></div>
          <div class="win-line"></div>
          <div class="win-line"></div>
          <div class="win-hint">Even small wins count.</div>
        </div>
      </div>
    </div>
  </div>`;
}

function weeklyPage() {
  return `
  <div class="page weekly-page">
    <div class="weekly-title">WEEKLY REVIEW</div>
    <div class="weekly-sub">Reflect · Reset · Recharge</div>

    <div class="w-section">
      <div class="w-q">📅 WEEK OF ____________________</div>
    </div>
    <div class="w-section">
      <div class="w-q">✅ What went well this week?</div>
      <div class="line"></div><div class="line"></div><div class="line"></div>
    </div>
    <div class="w-section">
      <div class="w-q">⚡ What was hard or draining?</div>
      <div class="line"></div><div class="line"></div><div class="line"></div>
    </div>
    <div class="w-section">
      <div class="w-q">🔄 What will I do differently next week?</div>
      <div class="line"></div><div class="line"></div><div class="line"></div>
    </div>
    <div class="w-section">
      <div class="w-q">🌟 Biggest win of the week</div>
      <div class="line"></div><div class="line"></div>
    </div>
    <div class="w-section">
      <div class="w-q">✅ WEEKLY HABIT TRACKER</div>
      <table class="htable">
        <thead><tr>
          <th class="hl">HABIT</th>
          <th>MON</th><th>TUE</th><th>WED</th><th>THU</th><th>FRI</th><th>SAT</th><th>SUN</th>
        </tr></thead>
        <tbody>
          <tr><td class="hl">Medication</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
          <tr><td class="hl">Movement</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
          <tr><td class="hl">Water</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
          <tr><td class="hl">Sleep by 11pm</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
          <tr><td class="hl">_______________</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
        </tbody>
      </table>
    </div>
    <div class="w-section">
      <div class="w-q">🎯 TOP 3 FOCUS FOR NEXT WEEK</div>
      <div class="priority"><span class="pnum">1</span><div class="pline"></div></div>
      <div class="priority"><span class="pnum">2</span><div class="pline"></div></div>
      <div class="priority"><span class="pnum">3</span><div class="pline"></div></div>
    </div>
  </div>`;
}

function notePage(n) {
  const lines = Array(28).fill('<div class="line"></div>').join('');
  return `
  <div class="page notes-page">
    <div class="notes-header">NOTES</div>
    <div class="notes-lines">${lines}</div>
    <div class="page-num">${n}</div>
  </div>`;
}

const css = `
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family: 'Montserrat', Arial, sans-serif; background: white; }

.page {
  width: 8.5in; height: 11in;
  padding: 0.5in 0.55in 0.4in 0.55in;
  display: flex; flex-direction: column;
  page-break-after: always; background: white;
  position: relative;
}

/* TOP BAR */
.top-bar { display:flex; justify-content:space-between; align-items:flex-start; border-bottom:2px solid #0A1628; padding-bottom:5px; margin-bottom:8px; }
.date-field { font-size:10px; font-weight:800; color:#0A1628; letter-spacing:1.5px; text-transform:uppercase; display:flex; align-items:center; gap:6px; }
.date-line { display:inline-block; border-bottom:1.5px solid #0A1628; width:120px; }
.energy-mood { text-align:right; }
.em-label { font-size:9px; font-weight:800; color:#0A1628; letter-spacing:1.5px; text-transform:uppercase; }
.circles { display:inline-flex; gap:3px; margin-left:4px; vertical-align:middle; }
.circle { width:11px; height:11px; border-radius:50%; border:1.5px solid #0A1628; display:inline-block; }
.mood-row { display:block; font-size:10px; color:#333; margin-top:3px; }

/* SECTION HEADERS */
.section-header { font-size:8px; font-weight:800; letter-spacing:2px; text-transform:uppercase; padding:3px 8px; margin-bottom:5px; }
.section-header.dark, .section-header:not(.mid) { color:white; background:#0A1628; }
.section-header.mid { color:white; background:#1a3a6b; }
.section-header.dark { color:white; background:#0A1628; }

/* LINES */
.line { border-bottom:1px solid #ddd; height:19px; width:100%; }
.lines-4 { display:flex; flex-direction:column; }

/* TWO COL */
.two-col { display:flex; gap:10px; flex:1; margin-bottom:7px; }
.col-left { flex:1; display:flex; flex-direction:column; }
.col-right { flex:1; display:flex; flex-direction:column; }

/* PRIORITIES */
.priority { display:flex; align-items:center; gap:6px; margin-bottom:5px; }
.pnum { font-size:14px; font-weight:800; color:#0A1628; min-width:16px; }
.pline { flex:1; border-bottom:1.5px solid #bbb; height:18px; }

/* TIME GRID */
.time-grid { display:grid; grid-template-columns:1fr 1fr; gap:2px 8px; }
.ts { display:flex; align-items:center; gap:4px; border-bottom:1px solid #ddd; height:18px; }
.tl { font-size:7.5px; font-weight:700; color:#0A1628; min-width:38px; letter-spacing:0.3px; }
.tline { flex:1; }

/* HABITS */
.habits-section { margin-bottom:7px; }
.habit-grid { display:grid; grid-template-columns:1fr 1fr; gap:4px 10px; }
.habit { display:flex; align-items:center; gap:6px; font-size:8.5px; font-weight:600; color:#222; }
.cb { width:12px; height:12px; border:1.5px solid #0A1628; border-radius:2px; flex-shrink:0; display:inline-block; }

/* BOTTOM ROW */
.bottom-row { flex:0 0 auto; }

/* WIN BOX */
.win-box { background:#f0f4ff; border-left:3px solid #0A1628; padding:5px 8px; height:100%; }
.win-label { font-size:8px; font-weight:800; color:#0A1628; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:4px; }
.win-line { border-bottom:1px solid #bbb; height:19px; margin-bottom:3px; }
.win-hint { font-size:7px; color:#999; font-style:italic; margin-top:3px; }

/* BRAIN DUMP */
.brain-dump-section { margin-bottom:7px; }

/* WEEKLY */
.weekly-page { justify-content:flex-start; gap:0; }
.weekly-title { font-size:24px; font-weight:800; color:#0A1628; letter-spacing:3px; text-transform:uppercase; text-align:center; margin-bottom:4px; }
.weekly-sub { font-size:9px; font-weight:600; color:#666; text-align:center; letter-spacing:2px; text-transform:uppercase; padding-bottom:10px; border-bottom:2px solid #0A1628; margin-bottom:10px; }
.w-section { margin-bottom:11px; }
.w-q { font-size:9px; font-weight:800; color:#0A1628; letter-spacing:1px; text-transform:uppercase; margin-bottom:4px; }
.htable { width:100%; border-collapse:collapse; }
.htable th { font-size:8px; font-weight:800; color:white; background:#0A1628; padding:4px; text-align:center; }
.htable td { border:1px solid #ddd; padding:5px 3px; text-align:center; font-size:8px; }
.htable td.hl { text-align:left; font-weight:700; padding-left:6px; color:#0A1628; }

/* NOTES */
.notes-page { justify-content:flex-start; }
.notes-header { font-size:18px; font-weight:800; color:#0A1628; letter-spacing:3px; text-transform:uppercase; border-bottom:2px solid #0A1628; padding-bottom:6px; margin-bottom:12px; }
.notes-lines { display:flex; flex-direction:column; flex:1; }
.page-num { font-size:8px; color:#bbb; text-align:center; margin-top:8px; letter-spacing:1px; }

/* INTRO */
.intro-page { justify-content:center; align-items:center; text-align:center; gap:16px; }
.i-title { font-size:36px; font-weight:800; color:#0A1628; letter-spacing:2px; text-transform:uppercase; line-height:1.15; }
.i-sub { font-size:11px; font-weight:400; color:#666; letter-spacing:3px; text-transform:uppercase; }
.i-div { width:60px; height:3px; background:#0A1628; margin:0 auto; }
.i-features { text-align:left; list-style:none; display:flex; flex-direction:column; gap:8px; max-width:360px; }
.i-features li { font-size:11px; color:#333; display:flex; align-items:center; gap:8px; }
.i-features li::before { content:''; width:7px; height:7px; background:#0A1628; border-radius:50%; flex-shrink:0; }

/* HOW TO */
.howto-box { background:#f0f4ff; border:1.5px solid #0A1628; border-radius:6px; padding:18px 24px; max-width:440px; text-align:left; }
.howto-box h3 { font-size:10px; font-weight:800; letter-spacing:2px; text-transform:uppercase; color:#0A1628; margin-bottom:10px; }
.howto-box p { font-size:10.5px; color:#333; line-height:1.75; }
.howto-note { font-size:9px; color:#999; letter-spacing:1px; text-transform:uppercase; text-align:center; }
`;

(async () => {
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    args: ['--no-sandbox']
  });
  const page = await browser.newPage();

  // Build all pages
  let body = '';

  // Page 1: Title
  body += `
  <div class="page intro-page" style="display:flex;flex-direction:column;justify-content:center;align-items:center;gap:16px;text-align:center;">
    <div>
      <div class="i-title">ADHD Daily<br>Planner<br>for Men</div>
      <div style="margin-top:10px" class="i-sub">Undated · Start Any Day</div>
    </div>
    <div class="i-div"></div>
    <ul class="i-features">
      <li>Daily Brain Dump — clear your mind first</li>
      <li>Top 3 Priorities — focus on what matters</li>
      <li>Hourly Time Blocking — 6am to 10pm</li>
      <li>Mood &amp; Energy Check-In</li>
      <li>Daily Habit Tracker</li>
      <li>Win of the Day — celebrate progress</li>
      <li>Weekly Review &amp; Reset</li>
    </ul>
  </div>`;

  // Page 2: How to Use
  body += `
  <div class="page" style="display:flex;flex-direction:column;justify-content:center;align-items:center;gap:16px;text-align:center;">
    <div class="i-title" style="font-size:22px;">How to Use This Planner</div>
    <div class="i-div"></div>
    <div class="howto-box">
      <h3>Your Daily Rhythm</h3>
      <p>
        <strong>Morning (5 min):</strong> Start with the Brain Dump. Write everything that's in your head — tasks, worries, ideas. Then choose your Top 3 Priorities. Fill in your Time Blocks.<br><br>
        <strong>Throughout the day:</strong> Tick off Habits as you complete them. Check your Energy and Mood when you notice a shift.<br><br>
        <strong>Evening (5 min):</strong> Write your Win of the Day — even small wins count. Note any overflow tasks.<br><br>
        <strong>Every 7 days:</strong> Complete a Weekly Review page. Reflect, reset, plan the next week.
      </p>
    </div>
    <div class="howto-note">This planner is undated — start any day, any time.</div>
  </div>`;

  // Pages 3–128: 13 weeks × (7 daily + 1 weekly) = 104 + 13 = 117 pages + 2 intro = 119
  // We do 13 weeks to get ~117 content pages, then 7 notes pages = 126 total
  for (let week = 0; week < 13; week++) {
    for (let day = 0; day < 7; day++) {
      body += dailyPage();
    }
    body += weeklyPage();
  }

  // 6 notes pages
  for (let n = 1; n <= 6; n++) {
    body += notePage(n);
  }

  const html = `<!DOCTYPE html><html><head><meta charset="UTF-8"><style>${css}</style></head><body>${body}</body></html>`;

  await page.setContent(html, { waitUntil: 'networkidle' });

  const pdf = await page.pdf({
    width: '8.5in',
    height: '11in',
    printBackground: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 }
  });

  fs.writeFileSync('/home/user/FEMCODE-Gehirn/outputs/planner-interior/ADHD-Daily-Planner-for-Men-INTERIOR.pdf', pdf);
  console.log('PDF generated:', pdf.length, 'bytes,', Math.round(pdf.length/1024), 'KB');

  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
