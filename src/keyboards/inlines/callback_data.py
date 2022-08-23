from aiogram.utils.callback_data import CallbackData

start_callback = CallbackData('start')
navigation_callback = CallbackData('navigation', 'for_data', 'id')
# просто передаем на вход заголовок start
# мы обозначили контейнер start, но в этом контейнере у нас ничего пока нет
