import os

import telebot
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="MARKDOWN")
BOT_USERNAME = bot.get_me().username
logger.info(f"Running bot with username: {BOT_USERNAME}")
