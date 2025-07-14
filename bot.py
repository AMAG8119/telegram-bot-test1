import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging

# تنظیمات logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# دریافت Token از environment variable
TOKEN = os.getenv('TOKEN')

if not TOKEN:
    print("❌ TOKEN environment variable not found!")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    print(f"🔥 Received /start from {user.first_name}")
    await update.message.reply_text(f"سلام {user.first_name}! من در Render کار می‌کنم! ☁️🎉")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"📨 Received: {update.message.text}")
    await update.message.reply_text(f"شما گفتید: {update.message.text}")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    print(f"Exception while handling an update: {context.error}")

def main():
    print("🚀 Bot starting on Render...")
    print(f"Token: {TOKEN[:20]}...")
    
    try:
        # ایجاد Application
        app = Application.builder().token(TOKEN).build()
        
        # اضافه کردن handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        
        # اضافه کردن error handler
        app.add_error_handler(error_handler)
        
        print("✅ Bot is running...")
        
        # اجرای بات
        app.run_polling(
            drop_pending_updates=True,
            allowed_updates=Update.ALL_TYPES
        )
        
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        raise

if __name__ == '__main__':
    main()
