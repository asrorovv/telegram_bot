from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Menyu 1"), KeyboardButton("Menyu 2"), KeyboardButton("Menyu 3"), KeyboardButton("Menyu 4")],
    [KeyboardButton("Menyu 5")], [KeyboardButton("Menyu 6")], [KeyboardButton("Menyu 7")], [KeyboardButton("Menyu 8")],
        ],
    resize_keyboard=True)



# async def get_all_product():
menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail.add(KeyboardButton("Product 1"), KeyboardButton("Product 2"))
menu_detail.add(KeyboardButton("Product 3"), KeyboardButton("Product 4"), KeyboardButton("Product5"))
menu_detail.add(KeyboardButton("Back"))


mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))
