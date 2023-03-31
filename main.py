import logging

from aiogram.utils import executor

from config import dp
from handlers import client
from aiogram import Bot, Dispatcher

client.register_handlers_client(dp)


TOKEN='5651777397:AAHQ_SX6AYfnzfbDQvA5iK_VxCbc4o9gmp0'

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
ADMIN_ID = [661114436,]



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)