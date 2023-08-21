from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils import config

bot = Bot(token = config.bot_token, parse_mode = "HTML")
dp = Dispatcher(bot, storage = MemoryStorage())
