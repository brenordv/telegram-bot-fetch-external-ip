# -*- coding: utf-8 -*-
import logging
from typing import Union
from telegram.ext import Updater, CommandHandler

from network_helper import get_external_ip

owner_id: Union[str, None] = None


def start(update, context):
    """Basic start function"""
    update.message.reply_text("Hi! We are friends now!")


def fetch_ip(update, context):
    """Gets the external IP and sends as a message"""
    global owner_id
    ip = get_external_ip()

    # Will ignore messages from anyone else.
    if update.message.chat.id != owner_id:
        return

    if ip is None:
        update.message.reply_text("Could not get external IP. :(")
        return

    update.message.reply_text(f"External ip: {ip}")


def start_bot(token: str, chat_id: int) -> None:
    """
    This will create an instance of the bot and start listening for messages.
    :param token: bot token
    :param chat_id: chat id. bot will respond just to that id.
    :return: None.
    """
    global owner_id
    owner_id = chat_id

    logging.info("Starting up IP Bot...")

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ip", fetch_ip))

    # Notifying user that the bot is starting
    updater.bot.send_message(chat_id=chat_id, text="External IP bot starting up!")

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    shut_down_msg = "Bot shutting down..."
    logging.info(shut_down_msg)
    updater.bot.send_message(chat_id=chat_id, text=shut_down_msg)
