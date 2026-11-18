import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CAU_TRA_LOI = (
    "Xin chào bạn cần tôi giúp gì, bot tự động\n"
    "Hello, how can I help you?"
)

@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.reply_to(message, CAU_TRA_LOI)

print("Bot đang chạy...")
bot.infinity_polling()
