from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from loader import dp, bot, data_manager

from keyboards import comands_default_keyboard
from keyboards import start_inline_keyboard, get_item_inline_keyboard
from keyboards import start_callback, navigation_callback


@dp.message_handler(commands='start')
async def answer_help_command(message: types.Message):
    print(message)
    await message.answer(text=f'{message.from_user.first_name}, привет!'
                                '\nЭто бот интернет магазина "РЭДИС"',
                            reply_markup=start_inline_keyboard)


@dp.callback_query_handler(start_callback.filter())
async def answer_help_command(call: types.CallbackQuery):
    await call.message.answer(text='Список команд представлен на клавиатуре',
                              reply_markup=comands_default_keyboard)
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)


@dp.message_handler(commands=['items'])
async def answer_help_command(message: types.Message):
    status, item_info = data_manager.get_item(0)
    item_text = f'Название товара: {item_info["name"]}'\
                f'\nКол-во товара: {item_info["count"]}'\
                f'\nОписание: {item_info["description"]}'
    await message.answer(text=item_text,
                         reply_markup=get_item_inline_keyboard())

@dp.callback_query_handler(start.callback.filter(for_data='items'))
async def answer_help_command(call: types.CallbackQuery):
    id = call.data.split(':')[-1]
    status, item_info = data_manager.get_item(int(id))
    item_text = f'Название товара: {item_info["name"]}' \
                f'\nКол-во товара: {item_info["count"]}' \
                f'\nОписание: {item_info["description"]}'
    await bot.edit_message.text(text=item_text,
                                chat_id=call.message.chat.id,
                                message_id = call.message.message_id)
    await bot.edit_message_reply_markup(reply_markup=get_item_inline_keyboard(id, status),
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id
                                        )
    

@dp.message_handler(content_types=['contact'])
async def answer_help_command(message: types.Message):
    print(message)
    if (message.from_user.id == message.contact.user_id):
        await message.answer(text='Круто! Спасибо, мы все проверили. Этот номер принадлежит вашей учетной записи ТГ!',
                            reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text='Этот контакт конечно не принадлежит этому пользователю, но спасибо за информацию!',
                             reply_markup=ReplyKeyboardRemove())



@dp.message_handler()
async def answer_help_command(message: types.Message):
    await message.answer(text='Я пока такого не знаю...',
                         reply_markup=ReplyKeyboardRemove())