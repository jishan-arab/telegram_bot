import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8235210406:AAHSAXlhZNH3Khh6QHkLDCsRj64EfizKCW0"

async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meme_url = data["url"]
        title = data["title"]
        await update.message.reply_photo(photo=meme_url, caption=title)
    else:
        await update.message.reply_text("Couldn't fetch meme 😔")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("meme", meme))
    print("🤖 Meme Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

