from utils.transliterate import to_cyrillic , to_latin
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp 
from states.user_control_state import ChooseOption
from keyboards.inline.tillar_inline import navigatsiya, tillar,glavniga
from keyboards.default.main_keyboards import start


@dp.message_handler(text="✍️ Lotin - Kiril")
async def kiril_to_latin(ms:Message):
    await ChooseOption.kiril.set()
    await ms.answer("✅Kiril & Lotin opsiyasi tanlandi \nMatnni yuboring", reply_markup=glavniga)

@dp.message_handler(text="🧩 Bosh menuga", state=ChooseOption)
async def boshsh(ms:Message, state:FSMContext):
    await state.finish()
    await ms.answer("Bosh menuga qaytildi", reply_markup=start)

@dp.message_handler(state=ChooseOption.kiril)
async def ugir(ms:Message):
    xabar = ms.text
    if xabar.isascii():
        javob = to_cyrillic(xabar)
    else :
        javob = to_latin(xabar)
    await ms.answer(text=javob, reply_markup=glavniga)


@dp.callback_query_handler(state=ChooseOption, text='tillarga')
async def tillargaa(call:CallbackQuery, state:FSMContext):
    await ChooseOption.trans.set()
    await call.message.answer("Tilni tanlang",reply_markup=tillar)
    await call.message.delete()



@dp.callback_query_handler(state=ChooseOption, text="bosh_menuga")
async def glavnigaaaa(call:CallbackQuery, state:FSMContext):
    await state.finish()
    await call.message.answer("Bosh menuga qaytildi", reply_markup=start)
    await call.message.delete()

