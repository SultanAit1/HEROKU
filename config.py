from aiogram import Bot, Dispatcher
from  decouple import config


TOKEN='5651777397:AAHQ_SX6AYfnzfbDQvA5iK_VxCbc4o9gmp0'
TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
ADMIN_ID = [661114436,]
