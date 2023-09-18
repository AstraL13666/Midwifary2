from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# TODO Перенаправить в файл .env
bot = Bot(token='')
dp = Dispatcher(storage=MemoryStorage())


class LinkID:
    def __init__(self):
        self.chat = -923973234  # -1001571427188
        self.channel = -1001902560054
        self.admins = 1192511915
