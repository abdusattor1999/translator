from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

@dp.message_handler(commands='help', state=ChooseOption)
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - 🔄 Botni qayta ishga tushirish"
           )
    await message.answer("\n".join(text))
