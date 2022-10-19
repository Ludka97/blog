from django.conf import settings
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from game.services import message, start


def run_bot():
    app = ApplicationBuilder().token(settings.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(~filters.COMMAND, message))
    app.run_polling()
