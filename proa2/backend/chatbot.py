import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import sqlite3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

app = Flask(__name__)

def fetch_recommended_events():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("SELECT name, date, url FROM events LIMIT 3")
    events = [{"name": row[0], "date": row[1], "url": row[2]} for row in c.fetchall()]
    conn.close()
    return events

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    msg = response.message()

    if "event" in incoming_msg:
        events = fetch_recommended_events()
        reply_text = "🎉 Recommended Events:\n"
        for event in events:
            reply_text += f"\n📌 {event['name']} - {event['date']}\n🔗 {event['url']}\n"
        msg.body(reply_text)
    else:
        msg.body("Hi! Type 'event' to get event recommendations!")

    return str(response)

# Telegram Bot Setup
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! Type 'event' to get event recommendations!")

def event_recommendations(update: Update, context: CallbackContext):
    events = fetch_recommended_events()
    reply_text = "🎉 Recommended Events:\n"
    for event in events:
        reply_text += f"\n📌 {event['name']} - {event['date']}\n🔗 {event['url']}\n"
    update.message.reply_text(reply_text)

def run_telegram_bot():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("event", event_recommendations))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    app.run(port=5001, debug=True)
    run_telegram_bot()
