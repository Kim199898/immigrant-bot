import os
from dotenv import load_dotenv

load_dotenv()
import telebot
from flask import Flask, request
API_TOKEN = os.getenv("API_TOKEN")
CRYPTOBOT_TOKEN = os.getenv("CRYPTOBOT_TOKEN")

PDF_FILE_PATH = 'pdf/9_steps_guide.pdf'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.json
    if 'invoice' in update and update['invoice']['status'] == 'paid':
        user_id = update['invoice']['customer']['telegram_user_id']
        bot.send_message(user_id, "✅ Спасибо за оплату! Вот ваш PDF-гайд:")
        bot.send_document(user_id, open(PDF_FILE_PATH, 'rb'))
    return 'OK'

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Оплатите PDF через CryptoBot и получите файл автоматически.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
