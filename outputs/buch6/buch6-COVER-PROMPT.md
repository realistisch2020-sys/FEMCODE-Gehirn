# Buch 6 — Cover Prompt (Vorder- und Rückseite)

Stand: 96 Seiten, A5 Taschenbuch, Amazon KDP

---

## 1. Die genauen Masse

**Buchformat (Trim Size):** A5 = 14,8 × 21,0 cm (5,83 × 8,27 Zoll)

**Rückenbreite** hängt von der Seitenzahl und dem Papier ab:

| Papier | Rechnung | Rückenbreite |
|---|---|---|
| Creme (empfohlen) | 96 × 0,0025 Zoll | **6,1 mm** |
| Weiss | 96 × 0,002252 Zoll | **5,5 mm** |

Nimm **Creme**. Das ist bei deutschsprachigen Sachbüchern Standard und liest sich angenehmer.

**Anschnitt (Bleed):** 3,2 mm rundherum

### Gesamtmass für das durchgehende Cover (Full Wrap)

```
Breite  = 3,2 mm + 148 mm + 6,1 mm + 148 mm + 3,2 mm  =  308,5 mm  (30,85 cm)
Höhe    = 3,2 mm + 210 mm + 3,2 mm                     =  216,4 mm  (21,64 cm)
```

**In Pixel bei 300 DPI:** 3644 × 2556 px

**Wichtig:** Ab 79 Seiten erlaubt KDP Text auf dem Buchrücken. Mit 96 Seiten darfst du also Titel und Namen auf den Rücken setzen.

---

## 2. So gehst du vor

ChatGPT (DALL·E) kann keine exakten Druckmasse und schreibt Text auf Bildern meistens fehlerhaft. Deshalb in zwei Schritten:

1. **ChatGPT** erzeugt nur das **Bildmotiv** (ohne Schrift)
2. **Canva** setzt es auf die exakte Grösse und legt die Schrift darüber

Das ist der Weg, der zu einem druckfähigen Ergebnis führt.

---

## 3. Prompt für ChatGPT — Vorderseite

Kopiere das direkt:

> Create a book cover illustration in a warm, modern editorial style. Portrait orientation, aspect ratio 2:3.
>
> Scene: a woman in her forties sitting alone in the driver's seat of a parked car at dusk. Seen from outside through the side window, slightly from behind, so her face is not fully visible. Her hands rest in her lap, not on the steering wheel. Her shoulders are lowered. She is not crying dramatically — she is simply still.
>
> Outside the car it is early evening, soft blue hour light, a quiet residential street, warm yellow light in the windows of a house in the background, slightly out of focus.
>
> Style: painterly digital illustration, soft grain, muted palette of dusty blue, warm sand, muted terracotta and cream. Gentle light, no harsh contrast. Emotional, calm, dignified — not sad, not clinical, not stocky.
>
> Composition: leave the upper third of the image visually calm and uncluttered for typography. No text, no letters, no words, no logos anywhere in the image.

**Hinweis:** Falls dir das Auto-Motiv zu konkret ist, hier eine Alternative:

> Same style and palette. Scene: a woman sitting alone on a kitchen floor at night, back against a cupboard, knees drawn up, one hand resting on the floor tiles. Only a small light above the stove is on. The rest of the kitchen is in soft shadow. Quiet, intimate, dignified. Leave the upper third calm for typography. No text anywhere.

---

## 4. Prompt für ChatGPT — Rückseite (Hintergrund)

> Create a plain background image for the back cover of a book, matching this palette: dusty blue, warm sand, muted terracotta, cream. Very soft gradient from deep dusty blue at the top to warm cream at the bottom, with subtle paper grain. Completely empty — no objects, no figures, no text, no patterns. Calm and uncluttered so text can be placed on top.

---

## 5. Was in Canva auf das Cover kommt

Lege in Canva eine Fläche mit **30,85 × 21,64 cm** an und teile sie so auf:

```
│◄── Rückseite 148 mm ──►│◄6,1►│◄── Vorderseite 148 mm ──►│
                          Rücken
```

### Vorderseite (rechte Hälfte)

```
Ich bin so müde.
Und niemand fragt mich warum.

Wie du aufhörst, für alle stark zu sein —
und endlich wieder du selbst wirst

Petra Tanner
```

Titel gross und ruhig setzen, am besten eine klare Serifenlose. Untertitel deutlich kleiner. Name unten.

### Buchrücken (6,1 mm)

```
Petra Tanner   ·   Ich bin so müde. Und niemand fragt mich warum.
```

Schrift maximal 4 pt kleiner als die Rückenbreite, mit mindestens 1,5 mm Abstand zu beiden Kanten.

### Rückseite (linke Hälfte)

```
Du funktionierst.
Du bist für alle da.
Und irgendwann sitzt du nachts da und denkst:
Wie lange noch, bis ich nicht mehr kann?

Es gibt einen Namen für das, was du gerade lebst.
Das Funktions-Ich.

Der Teil von dir, der aufsteht. Kaffee macht.
Termine hält. Lächelt. Liefert.
Der immer weiss, was die anderen brauchen.
Und nicht mehr weiss, was er selbst braucht.

Dieses Buch ist kein Programm und keine Checkliste.
Es ist ein Weg in fünf Stufen:

SEHEN · VERSTEHEN · ERLAUBEN · LERNEN · WERDEN

17 kurze Kapitel. Echte Geschichten.
Und am Ende jedes Kapitels eine Frage,
die niemand dir bisher gestellt hat.

Du darfst aufhören.
Du darfst müde sein.
Du darfst du sein.

—

Petra Tanner ist Therapeutin und Coachin in der Schweiz.
Sie begleitet Frauen, die für alle stark sind
und dabei sich selbst verloren haben.
```

Unten rechts bleibt ein weisses Feld frei für den **Barcode**: mindestens 5,08 × 2,54 cm. KDP setzt ihn automatisch — leg dort einfach nichts hin.

---

## 6. Vor dem Hochladen prüfen

- [ ] Datei als **PDF** exportiert, 300 DPI, CMYK wenn möglich
- [ ] Gesamtmass 30,85 × 21,64 cm inklusive Anschnitt
- [ ] Kein wichtiger Text näher als 6 mm an einer Schnittkante
- [ ] Barcode-Feld unten rechts auf der Rückseite frei
- [ ] Seitenzahl in KDP steht auf 96, Papier auf Creme

**Achtung:** Wenn sich die Seitenzahl nach dem Korrekturlesen ändert, ändert sich die Rückenbreite. Dann das Cover neu rechnen. Formel: Seitenzahl × 0,0025 Zoll bei Creme.
