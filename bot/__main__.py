from telegram.ext import CommandHandler
from bot import dispatcher, updater, botStartTime
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.telegram_helper.filters import CustomFilters
from .modules import authorize, list

from telegram import InlineKeyboardMarkup
from bot.helper.telegram_helper import button_builder

def start(update, context):
    start_string = '\x1fPanggil aku Detective Minami, Tugasku adalah mencari File/Folder di Drive Pribadi\x1f'
    sendMessage(start_string, context.bot, update)

def log(update, context):
    sendLogFile(context.bot, update)

def index(update, context):
    buttons = button_builder.ButtonMaker()
    buttons.buildbutton("Index Frost", f"https://view.gabriersite.workers.dev/0:/")
    buttons.buildbutton("Index Zukky", f"https://media.gabriersite.workers.dev/0:/")
    buttons.buildbutton("Odrive", f"https://www.odrive.com/s/30ff3fb5-45d4-4563-b48c-fc174f9324bf-61a7a7cb")
    buttons.buildbutton("Team Drive", f"https://groups.google.com/u/1/g/jiwa-laknat")
    reply_markup = InlineKeyboardMarkup(buttons.build_menu(3))
    drive_string = f'''⇩ Akses ke Gabrier Index or join Team Drive ⇩'''
    sendMarkup(drive_string, context.bot, update, reply_markup)
    
botcmds = [(f'{BotCommands.ListCommand}','Mencari File di Drive')]


def main():
    bot.set_my_commands(botcmds)

    start_handler = CommandHandler(BotCommands.StartCommand, start, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter, run_async=True)
    index_handler = CommandHandler(BotCommands.IndexCommand, index, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(log_handler)
    dispatcher.add_handler(index_handler)

    updater.start_polling()
    LOGGER.info("Bot Berjalan!")
    updater.idle()

main()
