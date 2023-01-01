from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_keyboards import start
from loader import dp
from states.user_control_state import ChooseOption

@dp.message_handler(commands='start', state=ChooseOption)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state=FSMContext):
    if state:
        state.finish()
    await message.answer(f"Assalomu aleykum, <b>{message.from_user.full_name} !</b>\nBotga xush kelibsiz \n👇 Pastdagi tugmalar orqali kerakli opsiyani tanlang",reply_markup=start)
