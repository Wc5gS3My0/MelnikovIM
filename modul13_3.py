from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '***'
bot = Bot(token=api)
dsp = Dispatcher(bot=bot, storage=MemoryStorage())

@dsp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я -- бот помогающий твоему здоровью.')

@dsp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print(f'Получено сообщение: {message.text}')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dsp, skip_updates=True)