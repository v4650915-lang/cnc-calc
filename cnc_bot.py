import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Токен и ссылки на твои калькуляторы
TOKEN = "8562167394:AAH50NNr1uVlR5UA3OVIDlPUjiex98ahExg"
URL_TRIANGLE = "https://v4650915-lang.github.io/cnc-calc/index.html"
URL_G12 = "https://v4650915-lang.github.io/cnc-calc/G12.1.html"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    # Кнопки будут одна под другой
    builder.row(types.KeyboardButton(text="📐 Треугольник", web_app=types.WebAppInfo(url=URL_TRIANGLE)))
    builder.row(types.KeyboardButton(text="🌀 Полярка G12.1", web_app=types.WebAppInfo(url=URL_G12)))
    
    await message.answer(
        f"Привет, Владимир! Выбери нужный инструмент:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())