# -*- coding: utf-8 -*-
"""Bonus-PDF (Freebie) fuer "Du brauchst kein letztes Gespräch",
Farben vom Buchcover (Nachtschwarz, Gold, warmes Morgenlicht)."""
from reportlab.lib.colors import HexColor
import sys
sys.path.insert(0, '/home/user/FEMCODE-Gehirn/tools')
from bonus_pdf_common import render

PALETTE = {
    'CREAM': HexColor('#FAF6EE'),
    'COVER_BG': HexColor('#17140F'),      # Nachtschwarz vom Cover
    'ACCENT': HexColor('#C9974A'),        # Gold der Titelschrift
    'ACCENT_DARK': HexColor('#9A7230'),
    'ACCENT_LIGHT': HexColor('#F1E3C4'),
    'ACCENT2': HexColor('#E0A96B'),       # warmes Morgenlicht aus dem Türspalt
    'ACCENT2_DARK': HexColor('#B87F42'),
    'ACCENT2_LIGHT': HexColor('#F7E7D2'),
    'PLUM': HexColor('#2B241C'),
    'WHITE': HexColor('#FFFFFF'),
    'LINE': HexColor('#E4D5BC'),
    'COVER_TEXT': HexColor('#FAF6EE'),
}

EXERCISES = [
    {
        'title': "Die Gesprächs-Uhr", 'track': 'A',
        'intro': ("Aus Kapitel 1: Warum du noch immer auf eine Antwort wartest. "
                  "Wie viel Zeit verbringst du in einer normalen Woche noch mit "
                  "dem Gespräch, das nie stattgefunden hat?"),
        'kind': 'lines', 'n_lines': 5,
        'note': "Notiere auch, in welchen Momenten es dich am meisten einholt.",
    },
    {
        'title': "Die Verantwortungs-Liste", 'track': 'B',
        'intro': ("Aus Kapitel 6: Verantwortung dorthin zurückgeben, wo sie "
                  "hingehört. Was du getragen hast, was aber nie deins war."),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 15, 'box_h': 55,
        'note': "Lies diese Liste laut, wenn der alte Vorwurf wieder auftaucht.",
    },
    {
        'title': "Der Realitäts-Anker", 'track': 'A',
        'intro': ("Aus Kapitel 5: Wenn deine Wahrheit abgestritten wird. Drei "
                  "Dinge, die wirklich passiert sind, so genau wie du sie kennst, "
                  "unabhängig davon, wie die andere Person sich erinnert."),
        'kind': 'table', 'n_rows': 3,
        'field1': "Was wirklich passiert ist", 'field2': "Geglaubt?",
        'field3_lines': ["Habe ich an mir", "gezweifelt?  ja / nein"],
    },
    {
        'title': "Der unversendete Brief", 'track': 'B',
        'intro': ("Aus Kapitel 7: Das letzte Gespräch in deinem Kopf beenden. "
                  "Schreib jetzt auf, was du dieser Person nie sagen konntest, "
                  "genau so, wie es in dir klingt."),
        'kind': 'numbered', 'n_items': 3, 'item_gap': 11, 'box_h': 76,
        'heading': ["Was ich ihr oder ihm sagen würde,", "wenn es noch möglich wäre:"],
        'extra_label': "Ein Satz, den ich stattdessen mir selbst sage:",
    },
    {
        'title': "Die Drei-Monats-Standortbestimmung", 'track': 'A',
        'intro': ("Komm nach drei Monaten zu dieser Seite zurück, mit etwas "
                  "Abstand zum Buch, und beantworte die folgenden Fragen ehrlich."),
        'kind': 'qa', 'questions': [
            "Wie oft denkst du heute noch an das unbeendete Gespräch, verglichen mit vor drei Monaten?",
            "Was hast du dir selbst geglaubt, auch ohne Bestätigung von aussen?",
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
    'out': "/home/user/FEMCODE-Gehirn/outputs/buch-letztes-gespraech/buch-letztes-gespraech-Bonus-PDF.pdf",
    'palette': PALETTE,
    'title_lines': ['„Du brauchst kein', 'letztes Gespräch.“'],
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
    'book_title_short': "Du brauchst kein letztes Gespräch",
    'exercises': EXERCISES,
    'contact_email': "info.safetothrive@gmail.com",
}

if __name__ == '__main__':
    render(CFG)
