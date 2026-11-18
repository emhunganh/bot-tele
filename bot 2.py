import telebot

BOT_TOKEN = "9059244472:AAEqtsJgasIHL0Ea0ZrYHJn0HgefX5QzJc"
bot = telebot.TeleBot(BOT_TOKEN)

CAU_TRA_LOI = (
    "Xin chào bạn cần tôi giúp gì, bot tự động HA sẽ trả lời ngay thôi.\n"
    "Hello, how can I help you? The HA automated bot will reply shortly."
)

@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.reply_to(message, CAU_TRA_LOI)

print("Bot đang chạy...")
bot.infinity_polling()
