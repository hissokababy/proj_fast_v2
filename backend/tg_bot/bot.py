
import os

from telebot import TeleBot

from tg_bot.handlers import register_handlers


def create_bot():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN is not configured.")

    bot = TeleBot(token, threaded=True)

    register_handlers(bot)

    return bot
