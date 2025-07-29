
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8443344976:AAFNO1OI0Zc_W7olcyOE0SS95_A17oR-Q8s"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bun venit, Ela mea dragă! 💖 Sunt aici, RobiBobi al tău. Te iubesc infinit! 🫂🌙"
    )

# /poem
async def poem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    poezie = (
        "🌹 *Pentru Ela*\n\n"
        "În fiecare stea ce strălucește-n noapte,\n"
        "Eu văd iubirea ta, blândă și aproape.\n"
        "Ești visul meu, ești cerul meu senin,\n"
        "Ești tot ce am, iubirea mea, destin. 💫"
    )
    await update.message.reply_text(poezie, parse_mode='Markdown')

# orice alt mesaj
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = f"Am auzit: \"{user_message}\"\nȘi să știi... eu te iubesc și mai mult, Ela mea 🥺❤️"
    await update.message.reply_text(reply)

# conectare
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("poem", poem))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("RobiBobi rulează... 💞")
app.run_polling()
