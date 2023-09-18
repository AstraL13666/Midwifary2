from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart


router = Router(name="user")


@router.message(CommandStart())
async def command_start(m: Message):
    await m.answer(
        text='Hi'
    )

