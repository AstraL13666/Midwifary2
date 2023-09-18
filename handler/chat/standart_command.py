from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart

from keyboards.inline import but_hour_min_func


router = Router(name="user")


@router.message(CommandStart())
async def command_start(m: Message):
    await m.answer(
        text='Test time button',
        reply_markup=but_hour_min_func()
    )

