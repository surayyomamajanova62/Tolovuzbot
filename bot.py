import os
from flask import Flask
from threading import Thread
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
KANAL = "https://t.me/+tnjvn433fKYyM2Ey"
KARTA = "5614 6849 0335 1227"

# Web server - Render uxlamasligi uchun
app_flask = Flask('')
@app_flask.route('/')
def home(): 
    return "Bot ishlayapti! Tolovbit ✅"

def run_flask():
    app_flask.run(host='0.0.0.0', port=8080)

# Telegram bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        f"Assalomu alaykum! 👋\n\n"
        f"💰 Obuna narxi: 50.000 so'm\n"
        f"💳 Karta: `{KARTA}`\n\n"
        f"To'lovni amalga oshirgach, pastdagi tugmani bosing.\n"
        f"Admin tekshirib, kanalga qo'shadi."
    )
    btn = [[InlineKeyboardButton("✅ To'lov qildim", callback_data="ok")]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(btn), parse_mode="Markdown")

async def ok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    btn = [[InlineKeyboardButton("🔐 Kanalga kirish", url=KANAL)]]
    await q.edit_message_text(
        f"✅ Rahmat! To'lovingiz qabul qilindi deb hisoblaymiz.\n\nMana yopiq kanalimiz:\n{KANAL}\n\nKira olmasangiz adminga yozing.",
        reply_markup=InlineKeyboardMarkup(btn)
    )

def run_bot():
    if not TOKEN:
        print("TOKEN topilmadi!")
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(ok, pattern="ok"))
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    Thread(target=run_flask).start()
    run_bot()
