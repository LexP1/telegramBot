from aiogram import Bot, Dispatcher
from config import TOKEN

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.change_data import Database

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

data_manager = Database()
