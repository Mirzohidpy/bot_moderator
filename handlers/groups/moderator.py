import asyncio
import datetime

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ChatPermissions
import re
from filters import IsGroup, AdminFilter
from loader import dp


@dp.message_handler(IsGroup(), Command('ro', prefixes='!/'), AdminFilter())
async def read_only_mode(msg: Message):
    member = msg.reply_to_message.from_user
    member_id = member.id
    command_parse = re.compile(r'(!ro|/ro) ?(\d+)? ?([\w+\D]+)?')
    parsed = command_parse.match(msg.text)
    time = parsed.group(2)
    comment = parsed.group(3)

    if not time:
        time = 5

    time = int(time)

    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await msg.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
    except Exception as e:
        await msg.answer('Error')
        return
    not_comment = "Sabab ko'rsatilmadi"
    await msg.answer(
        f"Foydalanuvchi {msg.reply_to_message.from_user.full_name} {time} minut yozish huquqidan mahrum qilindi.\n"
        f"Sabab: \n<b>{comment if comment else not_comment}</b>")
    service_message = await msg.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    await asyncio.sleep(5)
    await msg.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command('unro', prefixes='!/'), AdminFilter())
async def undo_read_only_mode(msg: Message):
    member = msg.reply_to_message.from_user
    member_id = member.id

    user_allowed = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=False,
        can_invite_users=True,
        can_pin_messages=False,
    )

    await msg.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await msg.answer(f'Foydalanuvchi {member.full_name} tiklandi.')
    service_message = await msg.answer("Xabar 5 sekunddan so'ng o'chib ketadi.")
    await asyncio.sleep(5)
    await msg.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), AdminFilter(), Command('ban', prefixes='!/'))
async def ban_user(msg: Message):
    member = msg.reply_to_message.from_user
    member_id = member.id
    await msg.chat.kick(user_id=member_id)

    await msg.answer(f"Foydalanuvchi {msg.reply_to_message.from_user.full_name} guruhdan haydaldi.")
    service_message = await msg.answer("Xabar 5 sekunddan so'ng o'chib ketadi.")
    await asyncio.sleep(5)
    await msg.delete()
    await service_message.delete()
