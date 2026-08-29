# -*- coding: utf-8 -*-
"""Bonus-PDF (Freebie) fuer Buch 5 "Deine Reaktion gehoert dir. Nicht mir.",
Farben vom Buchcover (dunkles Petrol, Gold)."""
from reportlab.lib.colors import HexColor
import sys
sys.path.insert(0, '/home/user/FEMCODE-Gehirn/tools')
from bonus_pdf_common import render

PALETTE = {
    'CREAM': HexColor('#FAF6F0'),
    'COVER_BG': HexColor('#0E2B2E'),      # dunkles Petrol vom Cover
    'ACCENT': HexColor('#C99A43'),        # Gold vom Cover
    'ACCENT_DARK': HexColor('#9C752B'),
    'ACCENT_LIGHT': HexColor('#F3E7CB'),
    'ACCENT2': HexColor('#3E7A78'),       # helleres Petrol/Tuerkis
    'ACCENT2_DARK': HexColor('#295452'),
    'ACCENT2_LIGHT': HexColor('#DCEAE9'),
    'PLUM': HexColor('#232323'),
    'WHITE': HexColor('#FFFFFF'),
    'LINE': HexColor('#D8CDB8'),
    'COVER_TEXT': HexColor('#F5EFE3'),
}

EXERCISES = [
    {
        'title': "Die Reaktionsübernahme erkennen", 'track': 'A',
        'intro': ("Aus Kapitel 3: Die Reaktionsübernahme. In welchen Momenten "
                  "übernimmst du diese Woche die Gefühle einer anderen "
                  "Person, statt bei deinen eigenen zu bleiben?"),
        'kind': 'lines', 'n_lines': 5,
        'note': "Notiere auch, wessen Gefühl es eigentlich war.",
    },
    {
        'title': "Empathie oder Verschmelzung?", 'track': 'B',
        'intro': ("Aus Kapitel 3c: Der Unterschied zwischen Empathie und "
                  "Verschmelzung. Nutze diese Tabelle eine Woche lang, für "
                  "jede Situation, in der du das Gefühl eines anderen stark "
                  "gespürt hast."),
        'kind': 'table', 'n_rows': 3,
        'field1': "Wessen Gefühl ich gespürt habe", 'field2': "Blieb ich ich?",
        'field3_lines': ["Habe ich gehandelt oder nur", "mitgefühlt?  gehandelt / mitgefühlt"],
    },
    {
        'title': "Dein Grenzen-Satz-Baukasten", 'track': 'A',
        'intro': ("Aus Kapitel 15: Grenzen ohne Erklärung. Drei Sätze, mit "
                  "denen du eine Grenze setzen kannst, ohne dich zu "
                  "rechtfertigen."),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 15, 'box_h': 55,
        'note': ("Häng den Zettel irgendwo hin, wo du ihn zufällig siehst, bis er "
                 "dir vertraut wird."),
    },
    {
        'title': "Der Rückfall-Notfallplan", 'track': 'B',
        'intro': ("Aus Kapitel 17: Der Rückfall. Bereite dich jetzt schon "
                  "vor, für den Tag, an dem du wieder übernimmst, obwohl du "
                  "es besser weisst."),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 11, 'box_h': 76,
        'heading': ["Drei Sätze, die ich mir sage, wenn ich merke,", "dass ich wieder übernehme:"],
        'extra_label': "Eine Person, die ich anrufen kann, ohne die Situation zu retten:",
    },
    {
        'title': "Die Drei-Monats-Standortbestimmung", 'track': 'A',
        'intro': ("Komm nach drei Monaten zu dieser Seite zurück, mit etwas "
                  "Abstand zum Buch, und beantworte die folgenden Fragen ehrlich."),
        'kind': 'qa', 'questions': [
            "Was hat sich in den letzten drei Monaten spürbar verändert, auch wenn es klein ist?",
            "Bei wem übernimmst du die Reaktion heute noch am häufigsten?",
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
    'out': "/home/user/FEMCODE-Gehirn/outputs/buch-reaktion/buch5-Bonus-PDF.pdf",
    'palette': PALETTE,
    'title_lines': ['„Deine Reaktion gehört dir.', 'Nicht mir.“'],
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
    'book_title_short': "Deine Reaktion gehört dir. Nicht mir.",
    'exercises': EXERCISES,
    'contact_email': "info.safetothrive@gmail.com",
}

if __name__ == '__main__':
    render(CFG)
