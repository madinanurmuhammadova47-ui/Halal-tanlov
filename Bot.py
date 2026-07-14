8789562762:AAGIVDY8yeS4rThv8mLlXh7ZUGwnwlhVIiM
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = 8851090613:AAEvbhwSKabmboIHxb0kIhVSaAw1KKolcVs

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
