// ── DEINE EINSTELLUNGEN ──────────────────────────────────────────
var BOT_TOKEN = "HIER_BOT_TOKEN_EINFÜGEN";
var CHAT_ID   = "";  // wird automatisch gefunden
// ─────────────────────────────────────────────────────────────────

var ALLE_FRAGEN = [
  // Haare & Körper
  "Warum sind meine Haare immer so trocken, egal welches Shampoo ich benutze?",
  "Was hilft wirklich gegen kaputte Haarspitzen – ohne teuren Salon?",
  "Warum verliere ich so viele Haare und was kann ich dagegen tun?",
  "Kann Ernährung wirklich die Haarqualität verändern?",
  "Was tun, wenn die Haare nach dem Waschen sofort wieder fettig sind?",
  "Welche natürlichen Öle sind wirklich gut für die Kopfhaut?",
  "Wie pflege ich coloriertes Haar, ohne es noch mehr zu schädigen?",
  // Geld & Finanzen
  "Wie komme ich raus aus dem Gefühl, nie genug Geld zu haben?",
  "Was blockiert mich unbewusst beim Geldverdienen?",
  "Wie ändere ich meine innere Einstellung zu Geld?",
  "Was ist der erste Schritt, wenn man am Ende des Monats immer im Minus ist?",
  "Wie spreche ich über Preise, ohne mich dabei schlecht zu fühlen?",
  "Was bedeutet Geldenergie und wie nutze ich sie?",
  "Wie setze ich einen fairen Preis für meine Leistungen?",
  // Schlaf & Hormone
  "Warum wache ich nachts immer um 3 Uhr auf und kann nicht mehr schlafen?",
  "Was hilft wirklich bei Einschlafproblemen – ohne Schlafmittel?",
  "Wie beruhige ich meinen Kopf, bevor ich schlafen gehe?",
  "Was ist der Zusammenhang zwischen meinem Zyklus und meinem Schlaf?",
  "Warum bin ich morgens noch müde, obwohl ich 8 Stunden geschlafen habe?",
  "Wie beeinflussen Emotionen meinen Schlaf?",
  "Kann Magnesium wirklich beim Schlafen helfen?",
  // Emotionen & Identität
  "Warum fühle ich mich manchmal tagelang leer, ohne zu wissen warum?",
  "Wie erkenne ich, was ich wirklich will – und nicht, was andere erwarten?",
  "Wie höre ich auf, meine Emotionen zu unterdrücken?",
  "Was bedeutet es, sich selbst treu zu sein?",
  "Wie komme ich raus aus dem Gefühl, nicht gut genug zu sein?",
  "Wie lerne ich, Nein zu sagen, ohne mich schuldig zu fühlen?",
  "Wie gehe ich mit starker Selbstkritik um?",
  // Loslassen & Neuanfang
  "Wie lasse ich jemanden los, der mir wichtig war?",
  "Was hält mich in alten Mustern fest – und wie breche ich daraus aus?",
  "Wie schaffe ich Platz für Neues in meinem Leben?",
  "Wie lasse ich Kontrolle los, ohne das Gefühl zu haben, alles zu verlieren?",
  "Wie fange ich nach einem Rückschlag neu an?",
  "Wie trenne ich mich von Gewohnheiten, die mich belasten?",
  "Wie unterscheide ich, was ich loslassen soll und was ich festhalten darf?",
  // Zyklus & Frausein
  "Warum bin ich kurz vor der Periode so reizbar – was steckt dahinter?",
  "Wie nutze ich meinen Zyklus, um produktiver zu sein?",
  "Was ist Zyklusarbeit und wie fange ich damit an?",
  "Was sagt mir mein Zyklus über meine Gesundheit?",
  "Wie beeinflusst der Zyklus meine Energie und Stimmung?",
  "Was sind häufige Zeichen, dass mein Hormonsystem aus dem Gleichgewicht ist?",
  "Wie ernähre ich mich zyklusgerecht?",
  // Systeme & Struktur
  "Wie baue ich eine Morgenroutine auf, die ich wirklich durchhalte?",
  "Was ist der einfachste Weg, meinen Tag zu strukturieren?",
  "Wie organisiere ich mein Business neben dem Job?",
  "Wie höre ich auf, alles auf einmal anzugehen?",
  "Wie bleibe ich fokussiert, wenn es tausend Ablenkungen gibt?",
  "Was tue ich, wenn ich immer prokrastiniere?",
  "Ich weiß was ich ändern müsste – aber tue es trotzdem nicht. Warum sabotiere ich mich selbst?",
  // Coaching & Blockaden
  "Wie weiß ich, ob ich eine Beziehung oder ein Projekt wirklich loslassen soll?",
  "Was ist ein Glaubenssatz – und wie löse ich ihn auf?",
  "Wie fange ich neu an, wenn ich nicht mal mehr weiß, wer ich bin?",
  "Wie höre ich auf, für alle da zu sein, bevor ich für mich selbst da bin?",
  "Was ist der Unterschied zwischen Traurigkeit und Depression?",
  "Wie erkenne ich emotionale Erschöpfung, bevor sie zum Burnout wird?",
  "Wie lerne ich, meine eigenen Bedürfnisse ernst zu nehmen?"
];

function zufälligeFragen() {
  var kopie = ALLE_FRAGEN.slice();
  // mischen
  for (var i = kopie.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = kopie[i]; kopie[i] = kopie[j]; kopie[j] = temp;
  }
  var auswahl = kopie.slice(0, 10);
  var text = "";
  for (var k = 0; k < auswahl.length; k++) {
    text += (k + 1) + ". " + auswahl[k] + "\n\n";
  }
  return text;
}

function meineChatIdFinden() {
  var url = "https://api.telegram.org/bot" + BOT_TOKEN + "/getUpdates";
  var antwort = UrlFetchApp.fetch(url);
  var daten = JSON.parse(antwort.getContentText());
  if (daten.result && daten.result.length > 0) {
    var id = daten.result[0].message.chat.id;
    Browser.msgBox("Deine Chat-ID: " + id + "\n\nKopiere diese Zahl und trage sie oben bei CHAT_ID ein.");
  } else {
    Browser.msgBox("Keine Nachrichten gefunden.\nSchreibe zuerst /start an deinen Bot auf Telegram, dann nochmal versuchen.");
  }
}

function jetztSenden() {
  var datum = Utilities.formatDate(new Date(), "Europe/Zurich", "dd.MM.yyyy");
  var text = "🔥 Deine 10 Zielgruppen-Fragen – " + datum + "\n\nWas Frauen gerade wirklich fragen:\n\n" + zufälligeFragen() + "💡 Welche Frage trifft deine Community am stärksten?";

  var url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage";
  UrlFetchApp.fetch(url, {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify({
      "chat_id": CHAT_ID,
      "text": text
    })
  });
}
