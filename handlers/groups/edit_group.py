import io

from aiogram.types import Message, InputFile
from filters import IsGroup, AdminFilter
from aiogram.dispatcher.filters.builtin import Command
from loader import dp, bot


@dp.message_handler(IsGroup(), AdminFilter(),  Command('set_photo', prefixes='!/'))
async def set_new_title(message: Message):
    await message.delete()
    try:
        photo = message.reply_to_message.photo[-1]
        photo = await photo.download(destination=io.BytesIO())
        input_file = InputFile(photo)
        await message.chat.set_photo(photo=input_file)


    except Exception as e:
        print(e)



@dp.message_handler(IsGroup(), AdminFilter(), Command('set_title', prefixes='!/'))
async def set_new_title(message: Message):
    await message.delete()
    try:
        title = message.reply_to_message.text
        # full_name = message.reply_to_message.from_user.full_name
        await message.chat.set_title(title)
    except Exception as e:
        print(e)

@dp.message_handler(IsGroup(), AdminFilter(), Command('set_description', prefixes='!/'))
async def set_new_description(message: Message):
    await message.delete()
    try:
        description = message.reply_to_message.text
        # full_name = message.reply_to_message.from_user.full_name
        await message.chat.set_description(description)
    except Exception as e:
        print(e)
