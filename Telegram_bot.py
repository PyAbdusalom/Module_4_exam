import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

TOKEN = os.environ["TOKEN"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply(f"Assalomu alaykum {message.from_user.full_name} 😊")
    await message.answer("Text Kiriting")
    await state.set_state("text")


@dp.message_handler(state="text")
async def echo(message: types.Message, state: FSMContext):
    All_vowels = "aeiouAEIOU"
    summa = sum([1 for i in message.text if i in All_vowels])
    if summa >= 5:
        await message.answer("Text unlilar soni 5 dan oshib ketti. Qayta kiriting")
        await state.set_state("text")
    else:
        await state.set_state("text")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
