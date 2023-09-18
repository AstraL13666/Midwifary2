from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# TODO Перенаправить в файл .env
bot = Bot(token='6502333537:AAGz2eeLZC0NTinL9hR1hRwVf6GmEwy9B4c')
dp = Dispatcher(storage=MemoryStorage())
