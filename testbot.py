# Этот код является частью проекта для работы с Telegram-ботом 
# используя библиотеку aiogram

# Импортируем необходимые компоненты из библиотеки aiogram
from aiogram import Bot, Dispatcher, executor, types
# Импортируем токен из конфигурационного файла
from config import TOKEN

# Определяем константу API_TOKEN, которая хранит токен для доступа к Телеграм-боту
API_TOKEN = TOKEN

# Инициализируем бота с помощью токена
bot = Bot(token=API_TOKEN)
# Инициализируем диспетчер, который будет обрабатывать события
dp = Dispatcher(bot)

# Определяем обработчик сообщений для команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   # Отправляем пользователю сообщение "Выводим сообщение"
   await message.reply("Выводим сообщение")
 
# Определяем обработчик текстовых сообщений
@dp.message_handler(content_types=['text'])
async def text_handler(message):
   # Проверяем, что сообщение пришло из личного чата
   if message.chat.type == 'private':
      # Отправляем пользователю сообщение "Реагирую на сообщение"
      await bot.send_message(message.chat.id, 'Реагирую на сообщение')
      
# Если файл запущен как основной, то запускаем опрос обновлений
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)