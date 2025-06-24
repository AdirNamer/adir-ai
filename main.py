# ADIR AI Bot - גרסה מלאה עם טלגרם + דשבורד גרפי
from flask import Flask, request, render_template_string
import os
import requests

app = Flask(__name__)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def send_message(chat_id, text):
    requests.post(f"{TELEGRAM_URL}/sendMessage", json={"chat_id": chat_id, "text": text})

@app.route('/')
def dashboard():
    return render_template_string(open("dashboard.html").read())

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')

    if text == '/start':
        send_message(chat_id, "🤖 ADIR AI Bot הופעל!")
    elif text == '/stop':
        send_message(chat_id, "🛑 הבוט נעצר (בכאילו 😉)")
    elif text == '/roi':
        send_message(chat_id, "📊 הרווח שלך היום הוא: ₪420")  # דוגמה
    elif text.startswith('/generate'):
        send_message(chat_id, f"🧠 נבנה בוט חדש לפי: {text[10:].strip()}")
    else:
        send_message(chat_id, "🤔 לא זיהיתי את הפקודה... נסה /start /roi או /generate")

    return '', 200