# Amazon Ads – Analyse Hero-Buch (Stand 05.10.2026, vorläufig)

Hero-Buch: „Ich stand nie auf meiner eigenen Liste“ – TB B0HGT4PX8H (12,99 €), Kindle B0HGSBZS18 (7,99 €)
Datenbasis: nur die im Auftrag genannten Screenshot-Werte (aggregiert). Kein Direktzugriff auf Amazon Ads (siehe 1).
Kennzeichnung: **[B]** belegt · **[A]** Annahme · **[P]** Prognose

---

## 1. Zugriff

- Amazon Ads und amazon.de sind aus dieser Cloud-Umgebung gesperrt (Netzwerk-Proxy antwortet 403). Kein Browser mit Amazon-Anmeldung, keine Amazon-Ads-Integration verbunden.
- Im Arbeitsbereich liegen keine Berichte oder Screenshots. Es gibt nur die Zahlen aus deinem Auftrag.
- Nicht umgangen. Ein Login über diese Umgebung wäre auch nicht sinnvoll, denn Amazon blockiert Cloud-Clients in der Regel. Der robuste Weg sind Berichtsexporte (Abschnitt 8).

## 2. Wirtschaftliche Basis

| Größe | TB | Kindle |
|---|---|---|
| Preis brutto [B] | 12,99 € | 7,99 € |
| netto (7 % MwSt. DE) [A] | 12,14 € | 7,47 € |
| Tantiemen-Satz [A] | 60 % − Druckkosten | 70 % − Downloadgebühr |
| Druckkosten 118 S. s/w (1,00 € + 0,012 €/S.) [A] | 2,42 € | – |
| **Tantieme je Verkauf (Schätzung)** [A] | **≈ 4,87 €** | **≈ 5,17 €** |
| Break-even-Kosten je Bestellung | ≈ 4,87 € | ≈ 5,17 € |
| Break-even-ACOS (auf Bruttopreis) | ≈ 37 % | ≈ 65 % |

Die Tantiemen sind geschätzt und müssen mit KDP abgeglichen werden. Bis dahin gilt die profitable Kostenobergrenze als **offen**. KENP-Lesungen (Kindle Unlimited) erscheinen nicht im Werbeumsatz. Falls das Buch in KDP Select ist, unterschätzt der ROAS den Werbewert.

## 3. Was die vorhandenen Daten sagen

**Belegt (28.09.–05.10., Konto-Aggregat, Inhalt nicht verifiziert):** 41.764 Impr. · 110 Klicks · 41,77 € · 2 Bestellungen · 28,90 € · CTR 0,26 % · CPC 0,38 € · CVR 1,82 % · CPA 20,89 € · ACOS 144,5 %

Befunde:

1. **Verlust je Werbebestellung ≈ 16 €** (20,89 € Kosten gegenüber ≈ 4,87 € Tantieme). Hauptproblem ist die Wirtschaftlichkeit pro Klick, nicht die Auslieferungsmenge. Bei CPC 0,38 € braucht Break-even eine Conversion-Rate von ≈ 8 %. Gemessen sind 1,8 %.
2. **Die Stichprobe ist zu klein für ein Urteil.** 2 von 110 Klicks → 95-%-Intervall der CVR: 0,5 %–6,4 %. Die wahre CVR kann gut oder schlecht sein.
3. **Werbeumsatz 14,45 € je Bestellung** (28,90 € = 2 × 14,45 €, älterer Zeitraum 1 × 14,45 €). Das passt weder zu 12,99 € noch zu 7,99 €. Wahrscheinlich wurde ein anderes Produkt bzw. ein anderer Titel gekauft (Halo) oder ein alter Preis erfasst. **Möglicherweise ist bisher keine Werbebestellung ein Hero-TB zu 12,99 €.** Das muss der Bericht „Gekaufte Produkte“ klären.
4. **CTR 0,26 % ist niedrig.** Das spricht für viel unpassenden Traffic aus Auto- und ASIN-Platzierungen oder für ein schwaches Erscheinungsbild in der Anzeige (Cover, Preis, Bewertungsanzahl).
5. **Auslieferungseinbruch nicht aus Aggregaten beweisbar.** Überlappungsrechnung: (25.–27.09.) − (03.–05.10. teilw.) = 48,98 € − 41,77 € = 7,21 €. Bei 6–8 €/Tag davor ergibt das für 03.10.–05.10. früh zusammen ≈ 11–17 €. Das ist ein Rückgang, aber kein Totalausfall. Zusätzlich gilt: Amazon-Ads-Werte der letzten 24–72 h werden nachträglich vervollständigt. Ein am Morgen des 05.10. gesehener 04.10. kann noch zu niedrig sein.

## 4. Ursachen des Einbruchs – Prüfreihenfolge

| # | Ursache | Plausibilität | Prüfung |
|---|---|---|---|
| 1 | Berichtsverzögerung (04.10. unvollständig) | hoch | 04.10. am 07.10. neu ansehen |
| 2 | Gebotssenkungen unter bisherigen CPC (Suchhinweise 0,15–0,30 € gegenüber Ø-CPC 0,38 €) | hoch | Änderungsverlauf + Target-Impressionen je Tag |
| 3 | Kontowarnungen (3, Inhalt unbekannt): Zahlung, Anzeigenberechtigung, Buch nicht beworbbar | mittel, schnell zu klären | Warnungen öffnen, Text kopieren |
| 4 | Pausen, Enddaten, Budget erreicht | mittel | Kampagnenübersicht Status/Budget/„Budget aufgebraucht“ |
| 5 | Produktverfügbarkeit / A+-Prüfung / Listing-Änderung | niedrig–mittel | Anzeigenstatus „berechtigt“ |
| 6 | Neue negative Keywords/ASINs, Platzierungs- oder Strategieänderung | niedrig | Änderungsverlauf |
| 7 | Nachfrage/Auktion (Wochenende 03./04.10., Feiertag 03.10.) | mittel | Vergleich mit Vorwochen-Wochenende |

Hinweis: Der 03.10. (Tag der Deutschen Einheit) und der 04.10. (Sonntag) sind beide keine normalen Werktage. Ein Vergleich mit Werktagen verzerrt das Bild.

## 5. Budgetentscheidung (vorläufig, wird mit Berichten konkretisiert)

**Empfehlung: 7-Tage-Lerntest mit Kampagnenbudgets von zusammen 15 €/Tag, erwartete tatsächliche Ausgaben 8–12 €/Tag, harter Rahmen 85 € tatsächliche Ausgaben in 7 Tagen.**

Begründung: Die entscheidende offene Größe ist die Conversion-Rate auf relevantem Traffic. Um ≤ 2 % von ≥ 6 % zu unterscheiden, braucht es ≈ 150–200 Klicks auf relevanten Targets. Bei 0,40 € CPC sind das 60–80 €. Mehr Geld kauft in 7 Tagen kaum mehr Erkenntnis, weniger Geld liefert kein Urteil. Die frühere Empfehlung „15 €/Tag bzw. 105 €“ ist als **Budgetobergrenze** vertretbar. Als **Ausgabenziel** ist sie zu hoch, solange kein Target belegt profitabel ist.

Vorläufige Verteilung (mit Berichten final):

| Kampagne | Tagesbudget | Rolle |
|---|---|---|
| SP/EXACT/Ich stand nie/DE | 6 € | relevanteste Suchanfragen, Hauptlernquelle |
| SP/ASIN/Ich stand nie/DE | 5 € | nur Ziel-ASINs mit Klicks/CTR über Schnitt |
| SP/AUTO/Ich stand nie/DE | 4 € | Suchbegriff-Entdeckung, close-match im Fokus |

Budget wirkt nur, wenn die Kampagnen budgetbegrenzt sind. Werden die Budgets nicht erreicht, steuert das Gebot die Auslieferung, nicht das Budget.

### Szenarien für 7 Tage (10 €/Tag tatsächlich, CPC 0,40 € → ≈ 175 Klicks) [P]

| CVR | Bestellungen 7 T. | pro Tag | Tantieme (4,87 €) | Netto vs. 70 € Spend |
|---|---|---|---|---|
| 2 % (heute) | ≈ 3,5 | 0,5 | ≈ 17 € | ≈ −53 € |
| 5 % | ≈ 8,8 | 1,25 | ≈ 43 € | ≈ −27 € |
| 8 % | ≈ 14 | 2,0 | ≈ 68 € | ≈ 0 € |

KENP und mögliche Folgekäufe anderer Bücher (Backmatter) sind nicht eingerechnet. Sie verbessern das Ergebnis, sind aber unbelegt.

### Abbruch- und Erhöhungskriterien

- **Erhöhen** (Budget +50 %, Gebote ausgewählter Targets +15–20 %): ein Target mit ≥ 2 Bestellungen und CPA ≤ 8 € oder Gesamt-CVR ≥ 5 % nach ≥ 120 Klicks. Bewertung erst 3 Tage nach Testende (Zuordnung reift).
- **Ende des Tests**: ≥ 150 relevante Klicks mit CVR ≤ 2 %. Dann liegt das Problem am Produktauftritt (Cover-Wirkung, Bewertungen, Preis, A+), nicht an der Werbung. Mehr Budget wäre dann Verschwendung, bis der Auftritt verbessert ist.
- **Target senken/pausieren**: Kosten ≥ 2 × Break-even-CPA (≈ 10 €) ohne Bestellung **und** Suchbegriffe erkennbar unpassend. Bei passenden Begriffen: Gebot −20 % statt Pause.

## 6. Skalierung – was 10 bzw. 15 Verkäufe täglich kosten [P]

Benötigte Werbebestellungen = Ziel − belegter Basisabsatz (noch unbekannt: KDP-Tagesverkäufe der letzten 30 Tage nötig).

| Basisabsatz | nötige Ads-Bestellungen | Spend/Tag bei CVR 2 % | bei 5 % | bei 8 % |
|---|---|---|---|---|
| 2/Tag → Ziel 10 | 8 | ≈ 160 € | ≈ 64 € | ≈ 40 € |
| 4/Tag → Ziel 10 | 6 | ≈ 120 € | ≈ 48 € | ≈ 30 € |
| 4/Tag → Ziel 15 | 11 | ≈ 220 € | ≈ 88 € | ≈ 55 € |

(CPC 0,40 €.) Grenzen:
- **Wirtschaftlich**: Erst ab einer CVR von ≈ 8 % trägt sich jede Werbebestellung über die Tantieme selbst. Darunter ist Skalieren bewusst finanzierter Verlust, der nur über Ranking-Effekte (organischer Zusatzabsatz) gerechtfertigt wäre. Dieser Effekt ist bisher unbelegt.
- **Inventar**: Heute ≈ 6.000 Impressionen/Tag → ≈ 15 Klicks/Tag. 8 Bestellungen bei 5 % CVR brauchen 160 Klicks/Tag, also rund das Zehnfache an Reichweite. Im deutschen Nischenmarkt ist das mit einem einzigen Buch kaum ohne deutlich höhere Gebote erreichbar.
- **50.000 €/Monat**: Als Buchumsatz entspricht das ≈ 128 TB-Verkäufen/Tag, als Tantieme ≈ 340/Tag. 10/Tag Hero-TB ≈ 1.460 € Tantieme/Monat. Das Ziel erfordert einen Katalog mit mehreren werbefähigen Titeln. Das Hero-Buch dient dabei als Prüfstein dafür, ob Ads im Thema überhaupt profitabel funktionieren.

## 7. Vorläufige Prioritäten (JETZT) – noch nicht freigabereif

1. Die 3 Kontowarnungen auslesen (Zahlung/Berechtigung schließt Ursache 3–5 aus oder bestätigt sie).
2. Letzte 5 Gebotsänderungen im Verlauf verifizieren. Wo das neue Gebot unter dem vorherigen Ø-CPC des Targets liegt und das Target relevant ist: auf das vorherige Gebot zurück (konkrete Werte nach Bericht).
3. Budgets wie in Abschnitt 5 setzen, aber nur, falls Kampagnen tatsächlich budgetbegrenzt waren.
4. Klären, welches Produkt die 14,45-€-Bestellungen waren (Bericht „Gekaufte Produkte“).
5. Kein Target pausieren, bevor Target- und Suchbegriffsbericht vorliegen.

## 8. Benötigte Unterlagen (einmal gebündelt)

Siehe Chat-Nachricht vom 05.10.2026 bzw. `plans/offene-punkte.md`.
