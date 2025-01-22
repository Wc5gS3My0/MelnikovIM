from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = '***'  # Замените на ваш токен
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Добро пожаловать! Чтобы рассчитать свою норму калорий, введите "Калории" или "Calories".')

@dp.message_handler(text=['Calories', 'Калории', 'Ккал'])
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    try:
        age = float(data['age'])
        weight = float(data['weight'])
        growth = float(data['growth'])
    except ValueError:
        await message.answer('Не могу конвертировать введенные значения в числа. Пожалуйста, попробуйте снова.')
        await state.finish()
        return

    # Формулы для расчета нормы калорий
    calories_man = 10 * weight + 6.25 * growth - 5 * age + 5
    calories_wom = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Норма (муж.): {calories_man:.2f} ккал')
    await message.answer(f'Норма (жен.): {calories_wom:.2f} ккал')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
