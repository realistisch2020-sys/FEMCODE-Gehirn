# Wegweiser: 50.000/Monat mit dem Bücher-Geschäft

Ein Dokument, von oben nach unten lesbar. Details verlinkt, nicht dupliziert. Stand 29.09.2026.

## Wo du stehst

- **Petra Tanner** — Autorin (Selbsthilfe/emotionale Gesundheit: Schuldgefühle, Selbstverlust im Funktionieren, erschöpfende Beziehungen, Loslassen) + Mentorin (Mentoring aktuell **nicht** Teil dieser Strategie)
- **Katalog:** 5 Bücher live, plus „Du brauchst kein letztes Gespräch" am 16.09. gelauncht (offen: zählt als Buch 5 oder 6 — siehe unten)
- **Fokusbuch:** „Ich stand nie auf meiner eigenen Liste" — ca. 4 Verkäufe/Tag, Taschenbuch 16,04€ / Kindle 7,99€
- **Ziel:** 50.000 (€ oder Fr., offen) Monatsumsatz in 12 Monaten — **rein aus dem Bücher-Geschäft**
- **Kein Mentoring-Verkauf.** Social Media (Insta+Facebook) läuft seit 29.09. zusätzlich mit, ist aber nicht der Haupthebel
- **Katalog-Ziel:** Bündel von 10 Büchern bis Dezember 2026

## Die Rechnung, kurz

Nur Buchverkauf reicht rechnerisch nicht: bei ~5,50–6€ Netto-Royalty/Exemplar bräuchte es für 50.000€ ~10.000 Exemplare/Monat gesamt. Verteilt auf 10 Titel: **Ø ~33 Verkäufe/Tag pro Titel** — das 8-Fache des heutigen Fokusbuch-Stands, aber machbar über Backlist-Effekt, mehrere Ads-Kampagnen gleichzeitig und einen Bündel-Preis (Kindle-Bündel bis 12,99€ möglich bei 70% Tantieme, seit der Anhebung im Juli 2026). Ehrliche Einschätzung: das System stimmt, "12 Monate" ist der optimistische Rand, nicht der Erwartungswert.

→ Vollständige Rechnung + Entscheidungshistorie: `plans/weg-zu-50k.md`

## Die Bausteine, auf die alles läuft

1. **Amazon Ads** — bereits aktiv, Aufwand ist Optimierung, nicht Content-Produktion
2. **Backmatter** — jedes Buch verweist aufs nächste + auf den Newsletter, einmal geschrieben, läuft dauerhaft
3. **E-Mail-Sequenz (Tentary)** — von "nur Beziehung aufbauen" zu "Backlist/neue Bücher empfehlen"
4. **Katalog-Erweiterung** — weitere Bücher bis Dezember
5. **Social Media (Insta+Facebook), zusätzlich** — Automatisierung fertig gebaut, wartet auf Meta-Zugänge

→ Operativer Spielplan (Kategorien/Keywords, Ads-Struktur, KU-vs-Wide, Launch-Fahrplan): `plans/kdp-wachstumsplan.md`
→ Backmatter-Text: `reference/backmatter-vorlage.md`
→ Neue Tentary-Serie: `outputs/tentary-willkommensserie.md`
→ Social-Media-Automatisierung: `automation/` (Setup-Anleitung: `reference/meta-setup.md`) — 6 Reel-Entwürfe liegen schon fertig in `automation/content_queue.json`

## Was ich von dir brauche

**A — Damit die Zahlen exakt statt ungefähr werden** (alles aus dem KDP-Dashboard, ~15 Min):
1. Royalty pro Titel/Format — KDP Bookshelf → Preisgestaltung ablesen
2. Taschenbuch/Kindle-Split der Verkäufe — KDP Sales Dashboard, letzte 30 Tage
3. KDP-Select-Status pro E-Book — Rechte & Preisgestaltung, plus bewusste Entscheidung KU oder wide pro Titel (mind. 1 Titel ist bei Apple Books, das schließt KU dafür aus)
4. Amazon-Ads ACOS / Kosten pro Verkauf
5. Währung fürs 50k-Ziel: € oder Fr.?
6. Ist "Du brauchst kein letztes Gespräch" Buch 5 oder Buch 6? (bestimmt, ob 4 oder 5 weitere Bücher bis Dezember fehlen)

**B — Damit der Dezember-Takt real wird:**
7. Status der übrigen neuen Manuskripte (1 mit Positionierung bekannt: Lust/Beziehung/Mental Load/Begehren — die anderen offen)

**C — Damit Social Media wirklich postet:**
8. Meta-Setup durchklicken: `reference/meta-setup.md` — dein Login, kann ich nicht übernehmen
9. Die 4 daraus entstehenden Werte + `ANTHROPIC_API_KEY` als GitHub-Secrets hinterlegen (Liste in `automation/README.md`)
10. Video-Entscheidung treffen: filmst du selbst und ich liefere nur Skript (Option A), ein Template-Tool mit B-Roll (Option B), oder ein KI-Avatar-Dienst (Option C)? Ohne das bleibt `video_url` in den Entwürfen leer, und nichts kann gepostet werden — siehe `plans/automatisierung-social-media.md` Baustein 2

**D — Damit die Buch-Seite live geht** (kein Datei-/Kontozugriff meinerseits, deshalb nur du):
11. Backmatter-Vorlage (`reference/backmatter-vorlage.md`) in die Manuskripte einfügen bzw. mit deinem Formatter abstimmen
12. Neue Tentary-Serie (`outputs/tentary-willkommensserie.md`) in dein Tentary-Konto einpflegen

**E — Kurzes Update, wenn Zeit ist:**
13. Wie lief der Launch von „Du brauchst kein letztes Gespräch"?

## Wo was steht

- `context/business.md` — wer du bist, was du anbietest
- `context/strategie.md` — Ziel & Prioritäten, kurz gehalten
- `plans/weg-zu-50k.md` — die Rechnung + Entscheidungshistorie + ehrliche Einschätzung
- `plans/kdp-wachstumsplan.md` — der operative Spielplan im Detail
- `reference/backmatter-vorlage.md` — der Backmatter-Text
- `reference/kdp-keywords-entwurf.md` — Backend-Keywords + Kategorie-Ideen pro Buch
- `outputs/tentary-willkommensserie.md` — die neue 4-Mail-Serie
- `outputs/kurzfassung-buchgeschaeft.md` — portable Kurzfassung für externe Tools
- `automation/` + `reference/meta-setup.md` — Social-Media-Automatisierung, aktiv als Zusatzkanal
- `plans/offene-punkte.md` — laufende ToDos, wird bei `/shutdown` gepflegt
