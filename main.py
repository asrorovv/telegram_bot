import logging
from db import Database
from aiogram import Bot, Dispatcher, executor, types
from default_button import menu_keyboard, menu_detail, mahsulot_button
from inline_button import keyboard


API_TOKEN = "7292693891:AAFrGZpnpZIpBfW6auI8tTMy7HjsbGHTvGs"


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users(full_name, username, user_id) VALUES ('{full_name}', '{username}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Assalomu aleykum {full_name} yana ko'rishib turganimdan xursandman!", reply_markup=menu_keyboard)

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xushkelibsiz {full_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Menyu 1")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("1 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=menu_detail)


@dp.message_handler(lambda message: message.text == "Menyu 2")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:")


@dp.message_handler(lambda message: message.text == "Back")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Menyulardan birini tanglang:", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Mahsulot 1")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=mahsulot_button)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
