from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api_key = '...'
bot = Bot(token=api_key)
dsp = Dispatcher(bot=bot, storage=MemoryStorage())

@dsp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я -- бот помогающий твоему здоровью.')

@dsp.message_handler()
async def all_messages(message):
    # print(type(message))
    # print(f'Получено сообщение: {message}')
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dsp, skip_updates=True)
