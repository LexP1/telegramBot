from aiogram.dispatcher.filters.state import StatesGroup, State

class CustomerState(StatesGroup):
    wait_item_name = State()