from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = 8789562762:AAET4qzA2dyEm09zOnI3izPHgi-CLCD3Yp8

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Bot ishlayapti.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
