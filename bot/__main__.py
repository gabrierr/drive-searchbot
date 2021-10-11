from telegram.ext import CommandHandler
from bot import dispatcher, updater, botStartTime
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.telegram_helper.filters import CustomFilters
from .modules import authorize, list


def start(update, context):
    start_string = '\x1fPanggil aku Detective Minami, Tugasku adalah mencari File/Folder di Drive Pribadi\x1f'
    sendMessage(start_string, context.bot, update)


def log(update, context):
    sendLogFile(context.bot, update)


botcmds = [(f'{BotCommands.ListCommand}','Mencari File di Drive')]


def main():
    bot.set_my_commands(botcmds)

    start_handler = CommandHandler(BotCommands.StartCommand, start, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter, run_async=True)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(log_handler)

    updater.start_polling()
    LOGGER.info("Bot Berjalan!")
    updater.idle()

main()
