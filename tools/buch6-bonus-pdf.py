# -*- coding: utf-8 -*-
"""Bonus-PDF (Freebie) fuer "Ich bin so muede. Und niemand fragt mich warum.",
Farben vom Buchcover (helles Pfirsich, Terrakotta, Gold, Schwarz)."""
from reportlab.lib.colors import HexColor
import sys
sys.path.insert(0, '/home/user/FEMCODE-Gehirn/tools')
from bonus_pdf_common import render

PALETTE = {
    'CREAM': HexColor('#FAF3E9'),
    'COVER_BG': HexColor('#F4E2D3'),      # helles Pfirsich vom Cover
    'ACCENT': HexColor('#C06E56'),        # Terrakotta vom Cover
    'ACCENT_DARK': HexColor('#9C4E3B'),
    'ACCENT_LIGHT': HexColor('#F3DCD3'),
    'ACCENT2': HexColor('#B8862E'),       # Gold vom Cover
    'ACCENT2_DARK': HexColor('#8C6620'),
    'ACCENT2_LIGHT': HexColor('#F0E2C4'),
    'PLUM': HexColor('#2E2A26'),
    'WHITE': HexColor('#FFFFFF'),
    'LINE': HexColor('#E4CFC0'),
    'COVER_TEXT': HexColor('#241F1B'),    # dunkle Schrift, da Cover-Hintergrund hell ist
}

EXERCISES = [
    {
        'title': "Funktions-Ich-Check", 'track': 'A',
        'intro': ("Aus Kapitel 1: Ich funktioniere, aber ich lebe nicht. Wann "
                  "hast du diese Woche nur funktioniert, statt wirklich da zu "
                  "sein? Woran hast du es gemerkt?"),
        'kind': 'lines', 'n_lines': 5,
        'note': "Notiere auch, was in diesem Moment wirklich in dir vorging.",
    },
    {
        'title': "Was ich wirklich brauche", 'track': 'B',
        'intro': ("Aus Kapitel 9: Was ich wirklich brauche und wie ich lerne, es "
                  "zu sagen. Fünf Dinge, die du brauchst, aber selten laut "
                  "aussprichst."),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 15, 'box_h': 55,
        'note': "Sag diese Woche mindestens eines davon laut, an eine Person.",
    },
    {
        'title': "Der Nein-ohne-Erklärung-Satz", 'track': 'A',
        'intro': ("Aus Kapitel 10: Nein sagen ohne Erklärung. Drei Situationen, "
                  "in denen du diese Woche Nein sagen könntest, ganz ohne "
                  "Begründung."),
        'kind': 'table', 'n_rows': 3,
        'field1': "Wozu ich Nein sagen will", 'field2': "Gesagt?",
        'field3_lines': ["Musste ich mich", "rechtfertigen?  ja / nein"],
    },
    {
        'title': "Der Erschöpfungs-Notfallplan", 'track': 'B',
        'intro': ("Aus Kapitel 7: Der Tag, an dem ich aufgehört habe, stark zu "
                  "sein. Bereite dich jetzt schon vor, für den Tag, an dem gar "
                  "nichts mehr geht."),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 11, 'box_h': 76,
        'heading': ["Drei Dinge, die mir helfen, auch wenn ich nur noch", "funktioniere:"],
        'extra_label': "Eine Person, die ich anrufen kann, ohne stark sein zu müssen:",
    },
    {
        'title': "Die Drei-Monats-Standortbestimmung", 'track': 'A',
        'intro': ("Komm nach drei Monaten zu dieser Seite zurück, mit etwas "
                  "Abstand zum Buch, und beantworte die folgenden Fragen ehrlich."),
        'kind': 'qa', 'questions': [
            "Was hat sich in den letzten drei Monaten spürbar verändert, auch wenn es klein ist?",
            "Wo funktionierst du heute noch, statt wirklich da zu sein?",
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
    'out': "/home/user/FEMCODE-Gehirn/outputs/buch6/buch6-Bonus-PDF.pdf",
    'palette': PALETTE,
    'title_lines': ['„Ich bin so müde. Und', 'niemand fragt mich warum.“'],
    'title_size': 19, 'title_leading': 9, 'pill_w': 110,
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
    'book_title_short': "Ich bin so müde",
    'exercises': EXERCISES,
    'contact_email': "info.safetothrive@gmail.com",
}

if __name__ == '__main__':
    render(CFG)
