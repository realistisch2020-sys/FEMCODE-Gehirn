"""
Impact-Fragen-Bot
Sendet jeden Samstag um 12:00 Uhr 10 frisch generierte Fragen der Zielgruppe.
Die Fragen werden per Claude API neu generiert – kein fixer Fragenpool.

Befehle:
  /fragen  → sofort 10 aktuelle Fragen abrufen
  /start   → Bot starten und Chat-ID anzeigen
"""

import logging
import os
from datetime import datetime, time
import anthropic
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ─── KONFIGURATION ───────────────────────────────────────────────
BOT_TOKEN      = os.getenv("BOT_TOKEN", "DEIN_BOT_TOKEN_HIER")
CHAT_ID        = os.getenv("CHAT_ID", "DEINE_CHAT_ID_HIER")
ANTHROPIC_KEY  = os.getenv("ANTHROPIC_API_KEY", "DEIN_ANTHROPIC_KEY_HIER")
# ─────────────────────────────────────────────────────────────────

logging.basicConfig(level=logging.INFO)

PROFIL = """
Du bist ein Marktforschungs-Assistent für eine Expertin in diesen Feldern:
- Zyklusarbeit & weibliche Gesundheit
- Network-Marketing & Produktempfehlungen
- Coaching & persönliche Entwicklung
- Naturheilpraktik (Haare, Haut, Schlaf, Körper)
- Emotionsarbeit, Blockaden & Identität
- Loslassen, Veränderung & Systeme

Ihre Zielgruppe: Frauen zwischen 25–45 Jahren, die sich nach Veränderung sehnen,
aber an inneren und äußeren Blockaden feststecken.
Typische Schmerzpunkte: trockene Haare, Schlafstörungen, Geldangst,
emotionale Erschöpfung, Identitätsverlust, Prokrastination.

Plattformen, auf denen sie aktiv sind: Instagram, TikTok, Reddit, Pinterest, Google.
"""

PROMPT = """
Generiere genau 10 brennende Fragen, die Frauen aus dieser Zielgruppe
gerade auf Social Media (Reddit, TikTok, Instagram, Google) stellen.

Regeln:
- Jede Frage muss sich anfühlen wie eine echte, persönliche Suchanfrage
- Verteile die Fragen auf mindestens 5 verschiedene Themenfelder
- Keine Ja/Nein-Fragen – nur offene, emotionale, konkrete Fragen
- Sprache: direkt, ehrlich, kein Coaching-Jargon
- Format: Nummerierte Liste, jede Frage mit Kategorie in eckigen Klammern

Beginne direkt mit Frage 1. Kein Intro, kein Outro.
"""


def generiere_fragen() -> str:
    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    nachricht = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        system=PROFIL,
        messages=[{"role": "user", "content": PROMPT}],
    )
    roher_text = nachricht.content[0].text.strip()

    heute = datetime.now().strftime("%d.%m.%Y")
    header = (
        f"🔥 *Deine 10 Zielgruppen-Fragen – {heute}*\n\n"
        f"_Direkt aus dem Netz – was Frauen gerade wirklich fragen._\n"
        + "─" * 30 + "\n\n"
    )
    footer = (
        "\n" + "─" * 30 + "\n"
        "💡 _Welche Frage trifft deine Community am stärksten? Baue darauf deinen nächsten Post._"
    )
    return header + roher_text + footer


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(
        f"✅ Bot gestartet!\n\nDeine Chat-ID: `{chat_id}`\n\n"
        "Trage diese ID als `CHAT_ID` in deinen Umgebungsvariablen ein.\n"
        "Befehl `/fragen` → sofort aktuelle Fragen abrufen.",
        parse_mode="Markdown",
    )


async def fragen_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Generiere Fragen...")
    text = generiere_fragen()
    await update.message.reply_text(text, parse_mode="Markdown")


async def samstags_job(context: ContextTypes.DEFAULT_TYPE):
    text = generiere_fragen()
    await context.bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fragen", fragen_command))

    # Jeden Samstag 10:00 UTC = 12:00 Uhr Schweizer Sommerzeit (CEST)
    app.job_queue.run_daily(
        samstags_job,
        time=time(hour=10, minute=0),
        days=(5,),  # 5 = Samstag
    )

    print("Bot läuft. Drücke Ctrl+C zum Stoppen.")
    app.run_polling()


if __name__ == "__main__":
    main()
