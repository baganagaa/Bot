from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '6106957558:AAHBF_uAJzN9f6jleveGLHjafVrx0PAm6O8'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
 
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Деда сдесь не любят.")
 
@dp.message_handler(content_types=['text'])
async def text_handler(message):
    if message.chat.type == 'private':
        await bot.send_message(message.chat.id, 'Да пошел ты нахрен, козел')
 
if name == 'main':
   executor.start_polling(dp, skip_updates=True)