import logging

from aiogram.utils import executor

from config import dp
from handlers import client
from decouple import config
client.register_handlers_client(dp)

bot = executor.Bot(token=config('TOKEN'))






if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)