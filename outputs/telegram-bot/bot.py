"""
Impact-Fragen-Bot
Sendet jeden Samstag um 12:00 Uhr 10 Fragen der Zielgruppe.
Befehle: /fragen  → sofort 10 Fragen abrufen
          /start   → Bot starten und Chat-ID anzeigen
"""

import logging
import random
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from fragen import FRAGEN

# ─── KONFIGURATION ───────────────────────────────────────────────
BOT_TOKEN = "DEIN_BOT_TOKEN_HIER"   # Token von @BotFather einfügen
CHAT_ID   = "DEINE_CHAT_ID_HIER"    # nach /start im Bot ausgegeben
# ─────────────────────────────────────────────────────────────────

logging.basicConfig(level=logging.INFO)


def zehn_fragen_auswählen() -> str:
    """Wählt 10 Fragen aus – 1-2 pro Kategorie, zufällig aber ausgewogen."""
    kategorien = list(FRAGEN.keys())
    random.shuffle(kategorien)
    ausgewählt = []

    # Erst eine Frage pro Kategorie bis 10 erreicht
    for kat in kategorien:
        if len(ausgewählt) >= 10:
            break
        frage = random.choice(FRAGEN[kat])
        ausgewählt.append((kat, frage))

    # Falls weniger als 10, nochmal durch die Kategorien
    if len(ausgewählt) < 10:
        for kat in kategorien:
            if len(ausgewählt) >= 10:
                break
            frage = random.choice([f for f in FRAGEN[kat] if (kat, f) not in ausgewählt])
            ausgewählt.append((kat, frage))

    # Nachricht formatieren
    heute = datetime.now().strftime("%d.%m.%Y")
    text = f"🔥 *Deine 10 Zielgruppen-Fragen – {heute}*\n\n"
    text += "_Nutze diese Fragen für Content, Posts und Angebote._\n"
    text += "─" * 30 + "\n\n"

    for i, (kat, frage) in enumerate(ausgewählt, 1):
        text += f"*{i}. [{kat}]*\n{frage}\n\n"

    text += "─" * 30 + "\n"
    text += "💡 _Welche Frage trifft deine Community am meisten? Baue darauf deinen nächsten Post._"
    return text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(
        f"✅ Bot gestartet!\n\nDeine Chat-ID: `{chat_id}`\n\n"
        f"Trage diese ID als CHAT_ID in bot.py ein.\n"
        f"Befehl /fragen → sofort 10 Fragen abrufen.",
        parse_mode="Markdown"
    )


async def fragen_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = zehn_fragen_auswählen()
    await update.message.reply_text(text, parse_mode="Markdown")


async def samstags_job(context: ContextTypes.DEFAULT_TYPE):
    text = zehn_fragen_auswählen()
    await context.bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Befehle
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fragen", fragen_command))

    # Wöchentlicher Job: Samstag 12:00 UTC (= 12:00 Schweiz im Winter, 14:00 im Sommer)
    # Für Schweizer Sommerzeit (CEST = UTC+2): Uhrzeit auf 10:00 UTC setzen
    job_queue = app.job_queue
    job_queue.run_daily(
        samstags_job,
        time=datetime.strptime("10:00", "%H:%M").time(),  # 10:00 UTC = 12:00 CEST
        days=(5,),  # 0=Mo, 5=Sa
    )

    print("Bot läuft. Drücke Ctrl+C zum Stoppen.")
    app.run_polling()


if __name__ == "__main__":
    main()
