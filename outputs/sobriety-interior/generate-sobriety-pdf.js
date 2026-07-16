const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');

function dailyPage() {
  return `
  <div class="page daily-page">
    <div class="top-bar">
      <div class="date-field">DATE <span class="date-line"></span></div>
      <div class="sober-day">SOBER DAY # <span class="day-line"></span></div>
    </div>

    <div class="section morning-section">
      <div class="section-header dark">MORNING INTENTION</div>
      <div class="intention-row">My intention today: <span class="long-line"></span></div>
      <div class="intention-row">What could challenge me: <span class="long-line"></span></div>
    </div>

    <div class="two-col">
      <div class="col-left">
        <div class="section-header dark">TOP 3 PRIORITIES</div>
        <div class="priority"><span class="pnum">1</span><div class="pline"></div></div>
        <div class="priority"><span class="pnum">2</span><div class="pline"></div></div>
        <div class="priority"><span class="pnum">3</span><div class="pline"></div></div>
        <div style="height:6px"></div>
        <div class="section-header mid">ADDITIONAL TASKS</div>
        <div class="line"></div><div class="line"></div><div class="line"></div>
        <div class="line"></div><div class="line"></div><div class="line"></div>
        <div class="line"></div><div class="line"></div>
      </div>
      <div class="col-right">
        <div class="section-header dark">TIME BLOCKS</div>
        <div class="time-grid">
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
        </div>
      </div>
    </div>

    <div class="section habits-section">
      <div class="section-header dark">DAILY HABITS</div>
      <div class="habit-grid">
        <div class="habit"><span class="cb"></span>Water (8 glasses)</div>
        <div class="habit"><span class="cb"></span>Movement / Exercise</div>
        <div class="habit"><span class="cb"></span>Sleep (7-8 hrs)</div>
        <div class="habit"><span class="cb"></span>Meditation / Prayer</div>
        <div class="habit"><span class="cb"></span>Called sponsor / support</div>
        <div class="habit"><span class="cb"></span>Grateful moment</div>
        <div class="habit"><span class="cb"></span>_____________________</div>
        <div class="habit"><span class="cb"></span>_____________________</div>
      </div>
    </div>

    <div class="two-col bottom-row">
      <div class="col-left">
        <div class="section-header mid">MOOD &amp; ENERGY</div>
        <div class="tracker-row">Mood &nbsp;&nbsp; 1 &nbsp; 2 &nbsp; 3 &nbsp; 4 &nbsp; 5 &nbsp; 6 &nbsp; 7 &nbsp; 8 &nbsp; 9 &nbsp; 10</div>
        <div class="tracker-row">Energy &nbsp; 1 &nbsp; 2 &nbsp; 3 &nbsp; 4 &nbsp; 5 &nbsp; 6 &nbsp; 7 &nbsp; 8 &nbsp; 9 &nbsp; 10</div>
      </div>
      <div class="col-right">
        <div class="evening-box">
          <div class="section-header dark" style="margin-bottom:4px">EVENING REFLECTION</div>
          <div class="eve-row">One win today: <span class="med-line"></span></div>
          <div class="eve-row">One thing I learned: <span class="med-line"></span></div>
          <div class="eve-row">One thing I release: <span class="med-line"></span></div>
        </div>
      </div>
    </div>
  </div>`;
}

function weeklyPage(weekNum) {
  return `
  <div class="page weekly-page">
    <div class="weekly-title">WEEKLY REVIEW</div>
    <div class="weekly-sub">Week ${weekNum} &nbsp;·&nbsp; Reflect · Reset · Keep Going</div>

    <div class="w-two-col">
      <div>
        <div class="w-section">
          <div class="w-q">Days sober this week: _______&nbsp;&nbsp; Total sober days: _______</div>
        </div>
        <div class="w-section">
          <div class="w-q">What went well this week?</div>
          <div class="line"></div><div class="line"></div><div class="line"></div>
        </div>
        <div class="w-section">
          <div class="w-q">What was challenging?</div>
          <div class="line"></div><div class="line"></div><div class="line"></div>
        </div>
        <div class="w-section">
          <div class="w-q">My biggest win this week:</div>
          <div class="line"></div><div class="line"></div>
        </div>
        <div class="w-section">
          <div class="w-q">What I want to focus on next week:</div>
          <div class="line"></div><div class="line"></div>
        </div>
      </div>
      <div>
        <div class="w-section">
          <div class="w-q">WEEKLY HABIT TRACKER</div>
          <table class="htable">
            <thead><tr>
              <th class="hl">HABIT</th>
              <th>M</th><th>T</th><th>W</th><th>T</th><th>F</th><th>S</th><th>S</th>
            </tr></thead>
            <tbody>
              <tr><td class="hl">Water</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
              <tr><td class="hl">Movement</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
              <tr><td class="hl">Sleep 7-8h</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
              <tr><td class="hl">Meditation</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
              <tr><td class="hl">Sponsor</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
              <tr><td class="hl">__________</td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td><td><span class="cb"></span></td></tr>
            </tbody>
          </table>
        </div>
        <div class="w-section">
          <div class="w-q">TOP 3 FOCUS NEXT WEEK</div>
          <div class="priority"><span class="pnum">1</span><div class="pline"></div></div>
          <div class="priority"><span class="pnum">2</span><div class="pline"></div></div>
          <div class="priority"><span class="pnum">3</span><div class="pline"></div></div>
        </div>
        <div class="w-section">
          <div class="w-q">Notes:</div>
          <div class="line"></div><div class="line"></div><div class="line"></div>
        </div>
      </div>
    </div>
  </div>`;
}

function notePage() {
  const lines = Array(28).fill('<div class="line"></div>').join('');
  return `
  <div class="page notes-page">
    <div class="notes-header">NOTES</div>
    <div class="notes-lines">${lines}</div>
  </div>`;
}

const css = `
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family: Arial, Helvetica, sans-serif; background: white; }

.page {
  width: 8.5in; height: 11in;
  padding: 0.45in 0.5in 0.35in 0.5in;
  display: flex; flex-direction: column;
  page-break-after: always; background: white;
}

/* TOP BAR */
.top-bar { display:flex; justify-content:space-between; align-items:center; border-bottom:2.5px solid #1a1a2e; padding-bottom:6px; margin-bottom:8px; }
.date-field { font-size:9px; font-weight:700; color:#1a1a2e; letter-spacing:1.5px; text-transform:uppercase; display:flex; align-items:center; gap:6px; }
.date-line { display:inline-block; border-bottom:1.5px solid #1a1a2e; width:130px; }
.sober-day { font-size:9px; font-weight:700; color:#1a1a2e; letter-spacing:1.5px; text-transform:uppercase; display:flex; align-items:center; gap:6px; }
.day-line { display:inline-block; border-bottom:1.5px solid #1a1a2e; width:50px; }

/* MORNING */
.morning-section { margin-bottom:7px; }
.intention-row { font-size:9px; font-weight:600; color:#1a1a2e; display:flex; align-items:center; gap:4px; height:22px; }
.long-line { flex:1; border-bottom:1px solid #ccc; display:inline-block; }

/* SECTION HEADERS */
.section-header { font-size:7.5px; font-weight:800; letter-spacing:2px; text-transform:uppercase; padding:3px 8px; margin-bottom:5px; }
.section-header.dark { color:white; background:#1a1a2e; }
.section-header.mid { color:white; background:#2d4a7a; }

/* LINES */
.line { border-bottom:1px solid #ddd; height:19px; width:100%; }

/* TWO COL */
.two-col { display:flex; gap:10px; flex:1; margin-bottom:6px; }
.col-left { flex:1; display:flex; flex-direction:column; }
.col-right { flex:1; display:flex; flex-direction:column; }

/* PRIORITIES */
.priority { display:flex; align-items:center; gap:6px; margin-bottom:5px; }
.pnum { font-size:14px; font-weight:800; color:#1a1a2e; min-width:16px; }
.pline { flex:1; border-bottom:1.5px solid #bbb; height:18px; }

/* TIME GRID */
.time-grid { display:flex; flex-direction:column; gap:1px; }
.ts { display:flex; align-items:center; gap:4px; border-bottom:1px solid #ddd; height:17px; }
.tl { font-size:7.5px; font-weight:700; color:#1a1a2e; min-width:42px; }
.tline { flex:1; }

/* HABITS */
.habits-section { margin-bottom:6px; }
.habit-grid { display:grid; grid-template-columns:1fr 1fr; gap:4px 10px; }
.habit { display:flex; align-items:center; gap:6px; font-size:8.5px; font-weight:600; color:#222; }
.cb { width:12px; height:12px; border:1.5px solid #1a1a2e; border-radius:2px; flex-shrink:0; display:inline-block; }

/* BOTTOM ROW */
.bottom-row { flex:0 0 auto; }

/* TRACKER */
.tracker-row { font-size:9px; font-weight:700; color:#1a1a2e; letter-spacing:1px; padding:4px 8px; border-bottom:1px solid #eee; }

/* EVENING */
.evening-box { padding:4px 0; }
.eve-row { font-size:8.5px; font-weight:600; color:#1a1a2e; display:flex; align-items:center; gap:4px; height:22px; }
.med-line { flex:1; border-bottom:1px solid #ccc; display:inline-block; }

/* WEEKLY */
.weekly-page { justify-content:flex-start; }
.weekly-title { font-size:22px; font-weight:800; color:#1a1a2e; letter-spacing:3px; text-transform:uppercase; text-align:center; margin-bottom:4px; }
.weekly-sub { font-size:9px; font-weight:600; color:#666; text-align:center; letter-spacing:2px; text-transform:uppercase; padding-bottom:8px; border-bottom:2px solid #1a1a2e; margin-bottom:10px; }
.w-two-col { display:flex; gap:16px; }
.w-two-col > div { flex:1; }
.w-section { margin-bottom:10px; }
.w-q { font-size:8.5px; font-weight:800; color:#1a1a2e; letter-spacing:1px; text-transform:uppercase; margin-bottom:4px; }
.htable { width:100%; border-collapse:collapse; }
.htable th { font-size:7.5px; font-weight:800; color:white; background:#1a1a2e; padding:4px 2px; text-align:center; }
.htable td { border:1px solid #ddd; padding:4px 2px; text-align:center; font-size:8px; }
.htable td.hl { text-align:left; font-weight:700; padding-left:4px; color:#1a1a2e; font-size:7.5px; }

/* NOTES */
.notes-page { justify-content:flex-start; }
.notes-header { font-size:16px; font-weight:800; color:#1a1a2e; letter-spacing:3px; text-transform:uppercase; border-bottom:2px solid #1a1a2e; padding-bottom:6px; margin-bottom:12px; }
.notes-lines { display:flex; flex-direction:column; flex:1; }
`;

(async () => {
  const { chromium } = require('/opt/node22/lib/node_modules/playwright');
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    args: ['--no-sandbox']
  });
  const page = await browser.newPage();

  let body = '';

  // Page 1: Title
  body += `
  <div class="page" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:20px;">
    <div style="font-size:38px;font-weight:800;color:#1a1a2e;letter-spacing:2px;text-transform:uppercase;line-height:1.2;">
      SOBRIETY<br>JOURNAL<br>FOR MEN
    </div>
    <div style="width:60px;height:3px;background:#1a1a2e;"></div>
    <div style="font-size:11px;font-weight:400;color:#666;letter-spacing:3px;text-transform:uppercase;">
      120-Day Daily Recovery Planner
    </div>
    <div style="font-size:10px;color:#999;letter-spacing:2px;text-transform:uppercase;margin-top:8px;">
      Undated · Start Any Day
    </div>
  </div>`;

  // Page 2: Copyright + Disclaimer
  body += `
  <div class="page" style="display:flex;flex-direction:column;justify-content:center;align-items:flex-start;gap:16px;padding:1in;">
    <div style="font-size:11px;color:#333;line-height:1.8;">
      <p style="font-weight:700;margin-bottom:8px;">Sobriety Journal for Men</p>
      <p>Copyright © 2026 Petra Tanner. All rights reserved.</p>
      <p style="margin-top:12px;">No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the author.</p>
      <p style="margin-top:20px;padding:12px;border-left:3px solid #1a1a2e;font-size:10px;color:#555;line-height:1.7;">
        <strong>Disclaimer:</strong> This journal is a personal planning and tracking tool created for self-reflection and daily structure. It is not a substitute for professional medical advice, diagnosis, or treatment. If you are struggling with addiction or mental health challenges, please seek help from a qualified healthcare professional.
      </p>
      <p style="margin-top:20px;font-size:10px;color:#999;">Published by Petra Tanner · Amazon KDP · Printed in the USA</p>
    </div>
  </div>`;

  // Page 3: My Sobriety Start
  body += `
  <div class="page" style="display:flex;flex-direction:column;justify-content:center;align-items:center;gap:20px;">
    <div style="font-size:18px;font-weight:800;color:#1a1a2e;letter-spacing:3px;text-transform:uppercase;border-bottom:2px solid #1a1a2e;padding-bottom:8px;width:100%;text-align:center;">
      MY SOBRIETY
    </div>
    <div style="width:100%;max-width:420px;display:flex;flex-direction:column;gap:24px;">
      <div>
        <div style="font-size:8.5px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#1a1a2e;margin-bottom:4px;">I started this journal on:</div>
        <div style="border-bottom:1.5px solid #bbb;height:28px;"></div>
      </div>
      <div>
        <div style="font-size:8.5px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#1a1a2e;margin-bottom:4px;">My sobriety date:</div>
        <div style="border-bottom:1.5px solid #bbb;height:28px;"></div>
      </div>
      <div>
        <div style="font-size:8.5px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#1a1a2e;margin-bottom:4px;">My reason for staying sober:</div>
        <div style="border-bottom:1.5px solid #bbb;height:28px;"></div>
        <div style="border-bottom:1.5px solid #bbb;height:28px;margin-top:4px;"></div>
        <div style="border-bottom:1.5px solid #bbb;height:28px;margin-top:4px;"></div>
      </div>
      <div>
        <div style="font-size:8.5px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#1a1a2e;margin-bottom:4px;">What this journal means to me:</div>
        <div style="border-bottom:1.5px solid #bbb;height:28px;"></div>
        <div style="border-bottom:1.5px solid #bbb;height:28px;margin-top:4px;"></div>
      </div>
    </div>
  </div>`;

  // Page 4: How to Use
  body += `
  <div class="page" style="display:flex;flex-direction:column;justify-content:center;align-items:center;gap:16px;">
    <div style="font-size:18px;font-weight:800;color:#1a1a2e;letter-spacing:3px;text-transform:uppercase;border-bottom:2px solid #1a1a2e;padding-bottom:8px;width:100%;text-align:center;">
      HOW TO USE THIS JOURNAL
    </div>
    <div style="background:#f5f7ff;border-left:3px solid #1a1a2e;padding:18px 22px;width:100%;max-width:460px;">
      <p style="font-size:10.5px;color:#333;line-height:1.85;">
        <strong>Morning (5 minutes):</strong><br>
        Set your intention for the day. Identify what could challenge your sobriety today. Choose your Top 3 Priorities and fill in your Time Blocks.<br><br>
        <strong>Throughout the day:</strong><br>
        Tick off Habits as you complete them. Check your Mood and Energy when you feel a shift coming.<br><br>
        <strong>Evening (5 minutes):</strong><br>
        Write your Evening Reflection — one win, one lesson, one thing you release. Track your numbers.<br><br>
        <strong>Every 7 days:</strong><br>
        Complete a Weekly Review page. Count your sober days. Reflect on what worked and what was hard. Set your focus for the next week.
      </p>
    </div>
    <div style="font-size:9px;color:#999;letter-spacing:2px;text-transform:uppercase;text-align:center;margin-top:8px;">
      This journal is undated — start any day, any time.
    </div>
    <div style="font-size:9px;color:#1a1a2e;font-weight:700;letter-spacing:1px;text-transform:uppercase;text-align:center;margin-top:4px;">
      One day at a time. You've got this.
    </div>
  </div>`;

  // 17 weeks x (7 daily + 1 weekly) = 136 pages
  for (let week = 1; week <= 17; week++) {
    for (let day = 0; day < 7; day++) {
      body += dailyPage();
    }
    body += weeklyPage(week);
  }

  // 6 notes pages
  for (let n = 0; n < 6; n++) {
    body += notePage();
  }

  const html = `<!DOCTYPE html><html><head><meta charset="UTF-8"><style>${css}</style></head><body>${body}</body></html>`;

  await page.setContent(html, { waitUntil: 'networkidle' });

  const pdf = await page.pdf({
    width: '8.5in',
    height: '11in',
    printBackground: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 }
  });

  fs.writeFileSync('/home/user/FEMCODE-Gehirn/outputs/sobriety-interior/Sobriety-Journal-for-Men-INTERIOR.pdf', pdf);
  console.log('PDF generated:', pdf.length, 'bytes,', Math.round(pdf.length/1024), 'KB');

  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
