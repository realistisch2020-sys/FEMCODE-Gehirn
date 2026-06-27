var BOT_TOKEN = "HIER_TOKEN_EINFÜGEN";
var CHAT_ID = "447547765";

var FRAGEN = [
  "Wie baue ich ein Business auf, das zu meinem Leben passt – nicht umgekehrt?",
  "Wie spreche ich über meine Produkte, ohne mich wie eine Verkäuferin zu fühlen?",
  "Wie finde ich die richtigen Menschen für mein Team?",
  "Wie bleibe ich motiviert, wenn das Business langsam wächst?",
  "Was brauche ich wirklich, um im Network-Marketing erfolgreich zu sein?",
  "Wie kombiniere ich Coaching und Produkte in einem Angebot?",
  "Wie baue ich Vertrauen auf, bevor jemand bei mir kauft?",
  "Was ist der Unterschied zwischen einem Kunden und einem Teampartner?",
  "Wie finde ich heraus, was mich wirklich antreibt – jenseits von Geld?",
  "Was hält mich davon ab, mein volles Potenzial zu leben?",
  "Wie setze ich Ziele, die ich wirklich erreiche – und nicht nur plane?",
  "Was bedeutet es, aus der Opferrolle herauszutreten?",
  "Wie verändere ich Glaubenssätze, die mich seit Jahren blockieren?",
  "Wie erkenne ich, ob ich aus Angst handle oder aus Stärke?",
  "Was tue ich, wenn mein Umfeld mein Business nicht ernst nimmt?",
  "Wie gehe ich mit Ablehnung um, ohne aufzugeben?",
  "Wie höre ich auf, anderen zu gefallen, und fange an, mir selbst treu zu sein?",
  "Was bedeutet es, eine starke weibliche Identität zu entwickeln?",
  "Wie komme ich in meine Kraft, wenn ich mich klein fühle?",
  "Was ist der Unterschied zwischen Selbstliebe und Selbstgefälligkeit?",
  "Wie baue ich echtes Vertrauen in mich selbst auf?",
  "Was bedeutet es, eine Frau zu sein, die von innen heraus führt?",
  "Wie erkenne ich emotionale Erschöpfung, bevor sie zum Burnout wird?",
  "Wie fange ich neu an, wenn ich nicht mehr weiss, wer ich bin?",
  "Was brauche ich, um den nächsten grossen Schritt in meinem Leben zu wagen?",
  "Wie lasse ich los, was mich zurückhält – ohne zu wissen, was danach kommt?",
  "Was tue ich, wenn ich weiss, dass sich etwas ändern muss, aber nicht weiss wie?",
  "Wie trenne ich mich von Mustern, die mich seit Jahren begleiten?",
  "Was bedeutet es, sich selbst neu zu erfinden?",
  "Wie finde ich Mut, wenn die Angst grösser ist als der Wunsch nach Veränderung?"
];

function jetztSenden() {
  var kopie = FRAGEN.slice();
  for (var i = kopie.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = kopie[i]; kopie[i] = kopie[j]; kopie[j] = temp;
  }
  var auswahl = kopie.slice(0, 10);
  var text = "Deine 10 Zielgruppen-Fragen:\n\n";
  for (var k = 0; k < 10; k++) {
    text += (k+1) + ". " + auswahl[k] + "\n\n";
  }
  var url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage";
  UrlFetchApp.fetch(url, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify({ chat_id: CHAT_ID, text: text })
  });
  Logger.log("Gesendet!");
}
