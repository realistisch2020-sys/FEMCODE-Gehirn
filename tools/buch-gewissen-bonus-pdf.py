# -*- coding: utf-8 -*-
"""Bonus-PDF (Freebie) fuer "Das schlechte Gewissen",
Farben vom Buchcover (dunstiges Blau/Petrol, Gold)."""
from reportlab.lib.colors import HexColor
import sys
sys.path.insert(0, '/home/user/FEMCODE-Gehirn/tools')
from bonus_pdf_common import render

PALETTE = {
    'CREAM': HexColor('#FAF6EF'),
    'COVER_BG': HexColor('#3E5C6B'),      # dunstiges Blau vom Himmel/See auf dem Cover
    'ACCENT': HexColor('#C9A24A'),        # Gold vom Cover
    'ACCENT_DARK': HexColor('#9C7A2E'),
    'ACCENT_LIGHT': HexColor('#F3E7CB'),
    'ACCENT2': HexColor('#6E8B94'),       # helleres Seeblau
    'ACCENT2_DARK': HexColor('#4C6B75'),
    'ACCENT2_LIGHT': HexColor('#DCE7EA'),
    'PLUM': HexColor('#33322E'),
    'WHITE': HexColor('#FFFFFF'),
    'LINE': HexColor('#D9CFC0'),
    'COVER_TEXT': HexColor('#F5EFE3'),
}

EXERCISES = [
    {
        'title': "Echte Schuld oder falsches Gewissen?", 'track': 'A',
        'intro': ("Aus Kapitel 3: Echte Schuld und falsches Gewissen. Nutze diese "
                  "Tabelle eine Woche lang, für jede Situation, in der sich ein "
                  "schlechtes Gewissen meldet."),
        'kind': 'table', 'n_rows': 3,
        'field1': "Wobei ich mich schuldig fühle", 'field2': "Echte Schuld?",
        'field3_lines': ["Habe ich jemandem wirklich", "geschadet?  ja / nein"],
    },
    {
        'title': "Der Verantwortungs-Kreis", 'track': 'B',
        'intro': ("Aus Kapitel 11: Verantwortung ja, Schuld nein. Was liegt "
                  "wirklich in deiner Verantwortung, und was hast du dir nur "
                  "angewöhnt zu tragen?"),
        'kind': 'lines', 'n_lines': 5,
        'note': "Schreib zu jedem Punkt, wessen Verantwortung es eigentlich ist.",
    },
    {
        'title': "Dein Vergebungs-Satz an dich selbst", 'track': 'A',
        'intro': ("Aus Kapitel 13: Sich selbst vergeben. Drei Sätze, die dir "
                  "schwerfallen, die du dir aber gerne öfter selbst sagen "
                  "würdest."),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 15, 'box_h': 55,
        'note': ("Häng den Zettel irgendwo hin, wo du ihn zufällig siehst, bis er "
                 "dir vertraut wird."),
    },
    {
        'title': "Der Notfallplan für den nächsten Anruf", 'track': 'B',
        'intro': ("Aus Kapitel 6: Wenn die Familie das Gewissen benutzt. Bereite "
                  "dich jetzt schon vor, für das nächste Gespräch, in dem ein "
                  "schlechtes Gewissen als Druckmittel eingesetzt wird."),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 11, 'box_h': 76,
        'heading': ["Drei Sätze, die ich bereithalten will, wenn Druck kommt:"],
        'extra_label': "Eine Person, die ich danach anrufen kann, ohne mich zu rechtfertigen:",
    },
    {
        'title': "Die Drei-Monats-Standortbestimmung", 'track': 'A',
        'intro': ("Komm nach drei Monaten zu dieser Seite zurück, mit etwas "
                  "Abstand zum Buch, und beantworte die folgenden Fragen ehrlich."),
        'kind': 'qa', 'questions': [
            "Was hat sich in den letzten drei Monaten spürbar verändert, auch wenn es klein ist?",
            "In welcher Situation meldet sich das schlechte Gewissen heute noch am lautesten?",
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
    'out': "/home/user/FEMCODE-Gehirn/outputs/buch-schuldgefuehle/buch4-Bonus-PDF.pdf",
    'palette': PALETTE,
    'title_lines': ['„Das schlechte', 'Gewissen“'],
    'title_size': 26, 'title_leading': 10, 'pill_w': 100,
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
    'book_title_short': "Das schlechte Gewissen",
    'exercises': EXERCISES,
    'contact_email': "info.safetothrive@gmail.com",
}

if __name__ == '__main__':
    render(CFG)
