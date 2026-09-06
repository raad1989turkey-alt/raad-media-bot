import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً بك! البوت يعمل الآن بنجاح على مدار الساعة 🚀")

if __name__ == '__main__':
    TOKEN = os.environ.get("TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    print("البوت يعمل الآن...")
    application.run_polling()
