import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters as Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Привет! Добро пожаловать в бота для предсказания исходов матчей!\n"
        "Напиши названия команд, например, 'Реал Мадрид vs Барселона'."
    )

def echo(update: Update, context: CallbackContext) -> None:
    match_info = update.message.text
    prediction = "Победит Реал Мадрид"
    update.message.reply_text(f"Предсказание для матча {match_info}: {prediction}")

def main() -> None:
    TOKEN = "8189992775:AAFsH3SzcngoeThToNWJ-Qr5Hgzdf6D24A0"
    bot = Bot(TOKEN)
    updater = Updater(bot=bot, use_context=True)

    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()