# -*- coding: utf-8 -*-
"""Bonus-PDF (Freebie) fuer Buch 3 "Wenn Beziehungen erschoepfen",
Farben vom Buchcover (dunkles Petrol-Gruen, Kupfer)."""
from reportlab.lib.colors import HexColor
import sys
sys.path.insert(0, '/home/user/FEMCODE-Gehirn/tools')
from bonus_pdf_common import render

PALETTE = {
    'CREAM': HexColor('#FAF5EC'),
    'COVER_BG': HexColor('#242E29'),      # dunkles Petrol-Gruen vom Cover
    'ACCENT': HexColor('#B9743F'),        # Kupfer
    'ACCENT_DARK': HexColor('#8F5626'),
    'ACCENT_LIGHT': HexColor('#F2E2D0'),
    'ACCENT2': HexColor('#5C7568'),       # gedaemptes Salbei-Gruen (2. Cover-Ton)
    'ACCENT2_DARK': HexColor('#455A4C'),
    'ACCENT2_LIGHT': HexColor('#E4EAE3'),
    'PLUM': HexColor('#33322E'),
    'WHITE': HexColor('#FFFFFF'),
    'LINE': HexColor('#DCCEBB'),
    'COVER_TEXT': HexColor('#F5EFE3'),
}

EXERCISES = [
    {
        'title': "Deine Rollen-Inventur", 'track': 'A',
        'intro': ("Aus Kapitel 5: Die Rollen, die wir spielen. Welche Rollen "
                  "übernimmst du in deinen Beziehungen automatisch, und wie viel "
                  "Energie kostet dich jede davon?"),
        'kind': 'lines', 'n_lines': 5,
        'note': "Schreib zu jeder Rolle auch dazu, für wen du sie spielst.",
    },
    {
        'title': "Der Grenzen-Check", 'track': 'B',
        'intro': ("Aus Kapitel 7: Grenzen, das missverstandene Wort. Nutze diese "
                  "Tabelle eine Woche lang, für jede Situation, in der eine Grenze "
                  "gefragt gewesen wäre."),
        'kind': 'table', 'n_rows': 3,
        'field1': "Was passiert ist", 'field2': "Grenze gesetzt?",
        'field3_lines': ["Wie hat es sich danach", "angefühlt?  gut / schwer / neutral"],
    },
    {
        'title': "Dein Satz für Nein", 'track': 'A',
        'intro': ("Aus Kapitel 10: Nein sagen. Drei Sätze, die dir schwerfallen, "
                  "die du aber gerne öfter aussprechen würdest."),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 15, 'box_h': 55,
        'note': ("Häng den Zettel irgendwo hin, wo du ihn zufällig siehst, bis er "
                 "dir vertraut wird."),
    },
    {
        'title': "Die Muster-Erkennung", 'track': 'B',
        'intro': ("Aus Kapitel 2 und 14: Welches Beziehungsmuster wiederholt sich "
                  "bei dir, mit wem, und was ist jeweils der erste Moment, an dem "
                  "du es erkennst?"),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 11, 'box_h': 76,
        'heading': ["Das Muster, das sich wiederholt, und bei wem:"],
        'extra_label': "Der erste Moment, an dem ich es diesmal erkannt habe:",
    },
    {
        'title': "Die Drei-Monats-Standortbestimmung", 'track': 'A',
        'intro': ("Komm nach drei Monaten zu dieser Seite zurück, mit etwas "
                  "Abstand zum Buch, und beantworte die folgenden Fragen ehrlich."),
        'kind': 'qa', 'questions': [
            "Was hat sich in deinen Beziehungen spürbar verändert, auch wenn es klein ist?",
            "Bei wem ist es dir am schwersten gefallen, eine Grenze zu setzen?",
            "Welches Kapitel würdest du heute nochmal lesen, wenn du nur eines auswählen könntest?",
        ],
    },
    {
        'title': "Ein Satz an dich, drei Monate später", 'track': 'B',
        'intro': ("Schreib dir jetzt, direkt nach dem Buch, einen einzigen Satz "
                  "auf, den du in drei Monaten wiederlesen sollst."),
        'kind': 'closing_note',
        'contact_note': ("Und wenn du magst, schreib mir, was sich bei dir seit "
                          "dem Buch verändert hat. Ich lese jede Nachricht:"),
    },
]

CFG = {
    'out': "/home/user/FEMCODE-Gehirn/outputs/buch-beziehungen/buch3-Bonus-PDF.pdf",
    'palette': PALETTE,
    'title_lines': ['„Wenn Beziehungen', 'erschöpfen“'],
    'title_size': 24, 'title_leading': 10, 'pill_w': 100,
    'pill_line1': "Sechs kurze Übungen für die Zeit",
    'pill_line2': "nach dem Buch",
    'welcome_title1': "Danke, dass du dieses Buch",
    'welcome_title2': "gelesen hast",
    'welcome_intro1': ("Dieses Bonus-PDF ist keine Fortsetzung, sondern eine "
        "Vertiefung. Sechs kurze Übungen, die du direkt ausfüllen kannst, für "
        "die Wochen nach dem Buch, wenn der erste Schwung nachlässt und die "
        "eigentliche Arbeit beginnt."),
    'welcome_intro2': ("Nimm dir für jede Übung so viel Zeit, wie du brauchst. "
        "Es gibt keine feste Reihenfolge und kein Richtig oder Falsch."),
    'book_title_short': "Wenn Beziehungen erschöpfen",
    'exercises': EXERCISES,
    'contact_email': "info.safetothrive@gmail.com",
}

if __name__ == '__main__':
    render(CFG)
