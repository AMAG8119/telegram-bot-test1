import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging

logging.basicConfig(level=logging.INFO)

# دریافت Token از environment variable
TOKEN = os.getenv('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"سلام {user.first_name}! من در Render کار می‌کنم! ☁️🎉")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"شما گفتید: {update.message.text}")

def main():
    print("🚀 Bot starting on Render...")
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("✅ Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
