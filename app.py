from aiogram import executor
from aiogram.utils.executor import start_webhook

import logging

from data.config import WEBHOOK_PATH
from loader import dp, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)

    await bot.set_webhook(WEBHOOK_PATH, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await on_shutdown_notify(dispatcher)


def main(WEBAPP_HOST=None, WEBAPP_PORT=None):
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
