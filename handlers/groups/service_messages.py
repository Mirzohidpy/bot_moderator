from aiogram.types import ContentTypes, Message

from data.config import ADMINS
from filters import IsGroup
from loader import dp, bot
import asyncio


@dp.message_handler(IsGroup(), content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def new_member(msg: Message):
    message_id = msg.message_id + 1
    chat_id = msg.chat.id
    await msg.delete()
    members = ', '.join([item.get_mention(as_html=True) for item in msg.new_chat_members])
    await msg.reply(f'Xush kelibsiz, {members}')
    await asyncio.sleep(10)
    await bot.delete_message(chat_id, message_id)


@dp.message_handler(IsGroup(), content_types=ContentTypes.NEW_CHAT_PHOTO)
async def new_member(msg: Message):
    await msg.delete()


@dp.message_handler(IsGroup(), content_types=ContentTypes.NEW_CHAT_TITLE)
async def new_member(msg: Message):
    await msg.delete()


@dp.message_handler(IsGroup(), content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def left_member(msg: Message):
    message_id = msg.message_id + 1
    chat_id = msg.chat.id
    if msg.left_chat_member.id == msg.from_user.id:
        await msg.answer(f'{msg.left_chat_member.get_mention(as_html=True)} guruhni tark etdi.')
        # for admin_id in ADMINS:
        #     await bot.send_message(admin_id, f'{msg.left_chat_member.get_mention(as_html=True)} guruhni tark etdi.')
        await asyncio.sleep(10)
        await bot.delete_message(chat_id, message_id)
