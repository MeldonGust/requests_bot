from aiogram.utils import executor
from bot import dp
from handlers import commands, callbacks

commands.register_commands(dp)
callbacks.register_callbacks(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)

    
