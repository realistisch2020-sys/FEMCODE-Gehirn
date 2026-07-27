# TikTok-KDP-Karussell-System ("Kupka-System")

Aus dem KDP-Kurs, Ende Juli 2026 gesichert. Vollständige Anleitung lag als
PDF vor (`tiktok_kdp_aufbauanleitung.pdf`, 19 Seiten) — hier die destillierte
Fassung inklusive der Anpassung auf diese Arbeitsumgebung.

## Was das Originalsystem macht (aus dem Kurs, für Windows + Claude Desktop)

Wöchentlich, jeden Montag automatisch: 7 TikTok-Karussells (je 7 Slides,
9:16-Format) mit KI-Bildern (Ideogram V3, Graphic-Novel-Stil) und deutschem
Text-Overlay, plus eine Word-Datei mit Captions/Hashtags, alles automatisch
in Google Drive synchronisiert. Kosten ca. 2,94 USD/Woche für Ideogram.

**Kernbausteine:**
- `config.json` — API-Key und Grundeinstellungen
- `angles.json` — Pool von 20 recherchierten, emotionalen Content-Angles je
  Buch; jeder Angle wird nach Verwendung als "erledigt" markiert, damit sich
  nichts wiederholt
- `generate_images_core.py` — technischer Kern: ruft Ideogram auf, legt
  Safe-Zones fest (oben 5 %, rechts 80 %, unten 70 % bleiben frei von
  UI-Overlays), zeichnet abgerundete weisse Textboxen mit automatischem
  Zeilenumbruch, nutzt das erste generierte Bild eines Karussells als
  Stil-Referenz für die folgenden Slides (visuelle Konsistenz), 3 Versuche
  pro Slide bei Fehlern
- Wöchentlicher Ablauf: Batch-Nummer ermitteln → Web-Recherche zur
  Zielgruppensprache → 7 offene Angles auswählen → Slide-Texte + Prompts
  schreiben (Slide 1 immer als sofortiger Hook) → Bilder generieren →
  Word-Datei mit Captions/Hashtags → Google-Drive-Sync

**Handy-Schritt am Ende (bleibt bei jedem System gleich):** fertige Bilder
aus Google Drive laden, in TikTok als Karussell hochladen, Caption aus der
Word-Datei einfügen, Hashtags ergänzen, veröffentlichen.

## Anpassung für diese Arbeitsumgebung

Das Originalsystem läuft lokal auf Petras Windows-PC (Python, Windows Task
Scheduler, Ideogram-API-Key). In dieser Cloud-Arbeitsumgebung gilt stattdessen:

- **Kein Ideogram-Zugang, aber Canva ist verbunden** — Bildgenerierung läuft
  über die Canva-MCP-Werkzeuge statt Ideogram. Gleiches Prinzip (Prompt →
  Bild → Text-Overlay), anderes Werkzeug.
- **Kein Windows Task Scheduler** — stattdessen `CronCreate`/`ScheduleWakeup`
  bzw. eine Routine, die wöchentlich montags die Session anstösst und den
  Ablauf (Recherche → Angles → Slides → Bilder → Word-Datei) selbst ausführt.
- **Google Drive** muss als Connector in der Session aktiviert werden (Petra
  macht das einmalig in den Verbindungseinstellungen), danach läuft der
  Datei-Upload direkt darüber, kein lokaler Sync-Ordner nötig.
- **angles.json-Prinzip bleibt gleich:** ein laufend gepflegter Pool von
  Content-Angles je Buch, mit Status "offen"/"erledigt", damit sich Themen
  nicht wiederholen — sinnvoll als Datei im Projektordner auch hier.
- Das manuelle Handy-Hochladen bei TikTok bleibt gleich, ausser Metricool
  übernimmt später auch das automatische Posten (siehe eigene Absprache
  zu Metricool als Scheduler).

## Wiederverwendung für jedes neue Buch

Pro Buch: eigener Angles-Pool, eigener wöchentlicher Rhythmus, unabhängig von
anderen Büchern — aber alle über **ein** TikTok-Konto (`petratanner.autorin`)
ausgespielt, nicht über separate Konten (siehe Entscheidung dazu vom
27. Juli 2026).
