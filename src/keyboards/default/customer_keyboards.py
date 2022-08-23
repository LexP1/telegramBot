from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


comands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start')
        ],
        [
            KeyboardButton(text='/item')
        ],
        [
            KeyboardButton(text='/contact',
                           request_contact=True)
        ]
    ],
    resize_keyboard=True
)