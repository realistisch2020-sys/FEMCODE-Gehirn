// ── DEINE EINSTELLUNGEN ──────────────────────────────────────────
var BOT_TOKEN     = "HIER_BOT_TOKEN_EINFÜGEN";
var ANTHROPIC_KEY = "HIER_ANTHROPIC_KEY_EINFÜGEN";
var CHAT_ID       = "";  // wird automatisch gefunden – leer lassen
// ─────────────────────────────────────────────────────────────────

function meineChatIdFinden() {
  var url = "https://api.telegram.org/bot" + BOT_TOKEN + "/getUpdates";
  var antwort = UrlFetchApp.fetch(url);
  var daten = JSON.parse(antwort.getContentText());
  if (daten.result && daten.result.length > 0) {
    var id = daten.result[0].message.chat.id;
    Logger.log("Deine Chat-ID: " + id);
    SpreadsheetApp.getUi && SpreadsheetApp.getUi();
    Browser.msgBox("Deine Chat-ID: " + id + "\n\nKopiere diese Zahl und trage sie oben bei CHAT_ID ein.");
  } else {
    Browser.msgBox("Keine Nachrichten gefunden. Schreibe zuerst /start an deinen Bot auf Telegram.");
  }
}

function fragenGenerieren() {
  var profil = "Du bist Assistentin für eine Expertin in Zyklusarbeit, Naturheilpraktik, Coaching, Network-Marketing und Emotionsarbeit. Ihre Zielgruppe: Frauen 25-45 Jahre, die sich nach Veränderung sehnen, aber feststecken. Schmerzpunkte: trockene Haare, Schlafstörungen, Geldangst, emotionale Erschöpfung, Identitätsverlust.";

  var anfrage = {
    "model": "claude-opus-4-8",
    "max_tokens": 1024,
    "system": profil,
    "messages": [{
      "role": "user",
      "content": "Generiere genau 10 brennende Fragen, die Frauen dieser Zielgruppe gerade auf Instagram, TikTok, Reddit und Google stellen. Jede Frage muss sich wie eine echte, persönliche Suchanfrage anfühlen. Verteile sie auf mindestens 5 Themenfelder. Format: nummerierte Liste mit Kategorie in eckigen Klammern. Nur die Fragen, kein Intro."
    }]
  };

  var optionen = {
    "method": "post",
    "headers": {
      "x-api-key": ANTHROPIC_KEY,
      "anthropic-version": "2023-06-01",
      "content-type": "application/json"
    },
    "payload": JSON.stringify(anfrage)
  };

  var antwort = UrlFetchApp.fetch("https://api.anthropic.com/v1/messages", optionen);
  var daten = JSON.parse(antwort.getContentText());
  return daten.content[0].text;
}

function nachrichtSenden(text) {
  var datum = Utilities.formatDate(new Date(), "Europe/Zurich", "dd.MM.yyyy");
  var nachricht = "🔥 *Deine 10 Zielgruppen-Fragen – " + datum + "*\n\n_Was Frauen gerade wirklich fragen._\n\n" + text + "\n\n💡 _Welche Frage trifft deine Community am stärksten?_";

  var url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage";
  var optionen = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify({
      "chat_id": CHAT_ID,
      "text": nachricht,
      "parse_mode": "Markdown"
    })
  };
  UrlFetchApp.fetch(url, optionen);
}

function jetztSenden() {
  var fragen = fragenGenerieren();
  nachrichtSenden(fragen);
  Logger.log("Fragen gesendet!");
}
