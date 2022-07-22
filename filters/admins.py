from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    async def check(self, messages: Message) -> bool:
        member = await messages.chat.get_member(messages.from_user.id)
        return member.is_chat_admin()