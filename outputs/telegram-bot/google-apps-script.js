var BOT_TOKEN = "HIER_TOKEN_EINFÜGEN";
var CHAT_ID = "447547765";

var FRAGEN = [
  "1. Warum weiss ich genau, was ich tun müsste – und tue es trotzdem nicht?\n↳ Freeze — der Körper schützt vor dem, was sich nach Versagen anfühlen könnte.\n↳ \"Ich weiss den nächsten Schritt. Aber ich komme nicht vom Fleck.\"",

  "2. Warum fühle ich mich schuldig, sobald ich Geld verdiene?\n↳ Altes Glaubenssystem: Geld trennt, verändert, macht unbeliebt.\n↳ \"Je mehr ich verdiene, desto mehr habe ich das Gefühl, mich erklären zu müssen.\"",

  "3. Warum sage ich Ja zu allem – obwohl ich schon längst am Limit bin?\n↳ Fawn — Konflikte vermeiden fühlt sich sicherer an als eigene Grenzen.\n↳ \"Ich kann nicht Nein sagen, ohne mich danach schuldig zu fühlen.\"",

  "4. Warum zweifle ich immer genau dann, wenn es gut läuft?\n↳ Angst vor Erfolg — das Nervensystem kennt Stillstand als sicher.\n↳ \"Kurz bevor ich durchstarte, kommt die Stimme: Was, wenn ich versage?\"",

  "5. Warum will ich sichtbar sein – aber verstecke mich trotzdem?\n↳ Sichtbarkeit = Angreifbarkeit. Das System schützt vor altem Schmerz.\n↳ \"Ich weiss, dass ich raus müsste. Aber ich finde immer einen Grund zu warten.\"",

  "6. Warum erschöpft mich mein Business, obwohl ich es liebe?\n↳ Flight — immer im Modus, nie im Moment. Der Tank läuft leer.\n↳ \"Ich arbeite viel, aber das Gefühl von Ankommen kommt einfach nicht.\"",

  "7. Warum ist es so schwer, über meine Produkte zu sprechen, ohne mich klein zu machen?\n↳ Aufdringlich-Glaubenssatz blockiert die Stimme — Verkaufen fühlt sich falsch an.\n↳ \"Ich glaube an das, was ich anbiete. Aber sobald ich es ausspreche, entschuldige ich mich dafür.\"",

  "8. Warum vergleiche ich mich ständig mit anderen – obwohl ich weiss, dass es mich nicht weiterbringt?\n↳ Vergleich aktiviert die alte Wunde — Wissen schützt nicht vorm Triggern.\n↳ \"Ich öffne Instagram und fühle mich danach kleiner als vorher.\"",

  "9. Warum kann ich nicht abschalten – obwohl ich weiss, dass ich Pause brauche?\n↳ Der Kopf hält den Betrieb aufrecht, weil Stillstand sich nach Versagen anfühlt.\n↳ \"Ich liege im Bett und mein Kopf macht einfach weiter.\"",

  "10. Warum zieht mich immer wieder jemand in mein Team – und zieht sich dann zurück?\n↳ Erwartungsmanagement fehlt — Beziehung vor Struktur.\n↳ \"Sie war so motiviert. Und jetzt höre ich nichts mehr von ihr.\"",

  "11. Warum fühlt es sich falsch an, Geld für meine Zeit zu verlangen?\n↳ Wert-Glaubenssatz: Helfen darf nichts kosten — sonst ist es nicht echt.\n↳ \"Ich fühle mich schlecht, wenn ich meinen Preis nenne.\"",

  "12. Warum tue ich mir so schwer, loszulassen – obwohl ich weiss, dass es nicht mehr passt?\n↳ Das Bekannte fühlt sich sicherer an als das Unbekannte — auch wenn es schmerzt.\n↳ \"Ich weiss, dass ich loslassen sollte. Aber was kommt dann?\"",

  "13. Warum fühle ich mich nach einem guten Gespräch erschöpft statt aufgeladen?\n↳ Empathie ohne Grenzen kostet Energie — Verbindung und Schutz gleichzeitig.\n↳ \"Ich gebe alles – und danach bin ich leer.\"",

  "14. Warum starte ich immer wieder neu, ohne je fertig zu werden?\n↳ Perfektion blockiert den Abschluss — Anfangen ist sicher, Zeigen ist es nicht.\n↳ \"Ich habe zehn angefangene Projekte. Keins ist raus.\"",

  "15. Warum fühle ich mich allein mit meinem Business – obwohl ich viele Menschen kenne?\n↳ Rolle und Identität trennen sich — nach aussen stark, innen ohne Echo.\n↳ \"Ich kann mit niemandem wirklich darüber reden. Die meisten verstehen es nicht.\"",

  "16. Warum glaube ich anderen mehr als mir selbst?\n↳ Fremde Meinung überschreibt innere Stimme — ein altes Muster aus der Kindheit.\n↳ \"Sobald jemand zweifelt, zweifle ich auch.\"",

  "17. Warum mache ich vieles richtig – und fühle mich trotzdem nicht erfolgreich?\n↳ Selbstwert ist nicht an Leistung gekoppelt — aber das Gehirn glaubt es noch.\n↳ \"Ich mache vieles, aber nie genug. Nie wirklich perfekt.\"",

  "18. Warum ist es so schwer, um Hilfe zu bitten?\n↳ Stärke-Glaubenssatz: Wer fragt, ist schwach. Wer trägt, ist wertvoll.\n↳ \"Ich würde anderen sofort helfen. Aber selbst fragen – das kann ich nicht.\"",

  "19. Warum sabotiere ich mich selbst, kurz bevor etwas Grosses passiert?\n↳ Unterbewusstsein schützt vor Verantwortung und Sichtbarkeit.\n↳ \"Genau wenn es läuft, mache ich irgendetwas, das alles wieder stoppt.\"",

  "20. Warum fühlt sich Veränderung so bedrohlich an – obwohl ich sie mir wünsche?\n↳ Das Nervensystem kennt Wandel als Gefahr — nicht als Chance.\n↳ \"Ich will mein Leben verändern. Aber sobald es losgeht, will ich zurück.\""
];

function jetztSenden() {
  var kopie = FRAGEN.slice();
  for (var i = kopie.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = kopie[i]; kopie[i] = kopie[j]; kopie[j] = temp;
  }
  var auswahl = kopie.slice(0, 10);

  var datum = Utilities.formatDate(new Date(), "Europe/Zurich", "dd.MM.yyyy");
  var text = "🔥 Deine 10 Zielgruppen-Fragen – " + datum + "\n";
  text += "Was deine Community wirklich bewegt:\n";
  text += "──────────────────\n\n";

  for (var k = 0; k < 10; k++) {
    var frage = auswahl[k];
    frage = frage.replace(/^\d+\./, (k+1) + ".");
    text += frage + "\n\n";
  }

  text += "──────────────────\n";
  text += "💡 Welche Frage trifft deine Zielgruppe am stärksten?";

  var url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage";
  UrlFetchApp.fetch(url, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify({ chat_id: CHAT_ID, text: text })
  });
  Logger.log("Gesendet!");
}
