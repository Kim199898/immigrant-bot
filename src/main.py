import telebot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CRYPTOBOT_API_TOKEN = os.getenv("CRYPTOBOT_API_TOKEN")
SHOP_ID = os.getenv("SHOP_ID")
PDF_PATH = "9_steps_for_immigrants.pdf"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "👋 Привет! Нажмите, чтобы оплатить гайд за $9.99:")
    pay_url = f"https://t.me/CryptoBot?start=shop_{SHOP_ID}_guide"
    bot.send_message(message.chat.id, f"[💳 Оплатить PDF-гайд]({pay_url})", parse_mode="Markdown")

@bot.message_handler(content_types=['successful_payment'])
def payment_success(message):
    with open(PDF_PATH, 'rb') as file:
        bot.send_document(message.chat.id, file, caption="✅ Спасибо за оплату. Вот ваш PDF-гайд!")

bot.polling()