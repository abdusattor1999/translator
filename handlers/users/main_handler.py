from loader import dp 
from aiogram.types import Message,CallbackQuery
from states.user_control_state import ChooseOption
from keyboards.inline.tillar_inline import tillar, til_call, navigatsiya, glavniga
from googletrans import Translator
translator = Translator()
from aiogram.dispatcher import FSMContext
from utils.other_funs import dubledan_ajrat

@dp.message_handler(text="π Tarjimon")
async def tarjimon(ms:Message):
    await ChooseOption.trans.set()
    await ms.answer("Tarjimon bo'limi tanlandi endi tilni tanlang",reply_markup=tillar)

    
@dp.callback_query_handler(state=ChooseOption.trans)
async def set_language(call:CallbackQuery):
    kelgan_data = call.get_current()
    call_matni = kelgan_data.data
    royxat = await dubledan_ajrat(call_matni)
    call_matni = royxat[1]

    if call_matni == "uz_en":
        await call.message.answer("πΊπΏ O'zbek yoki πΊπΈ Ingliz tilida matn yuboring", reply_markup=glavniga)
        await ChooseOption.til1.set()
    elif call_matni == "uz_ru":
        await call.message.answer("πΊπΏ O'zbek yoki π·πΊ Rus tilida matn yuboring", reply_markup=glavniga)
        await ChooseOption.til2.set()
    elif call_matni == "ru_en":
        await call.message.answer("π·πΊ Rus yoki πΊπΈ Ingliz tilida matn yuboring", reply_markup=glavniga)
        await ChooseOption.til3.set()
    elif call_matni == "ar_uz":
        await call.message.answer("πΊπΏ O'zbek yoki πΈπ¦ Arab tilida matn yuboring", reply_markup=glavniga)
        await ChooseOption.til4.set()
    elif call_matni == "tr_uz":
        await call.message.answer("πΉπ· Turk yoki πΊπΏ O'zbek tilida matn yuboring", reply_markup=glavniga)    
        await ChooseOption.til5.set()
    elif call_matni == "ko_uz":
        await call.message.answer("π°π·Koreys yoki πΊπΏO'zbek tilida matn yuboring", reply_markup=glavniga)    
        await ChooseOption.til6.set()
    await call.message.delete()


@dp.message_handler(state=ChooseOption.trans)
async def tugri_turi(ms:Message):
    await ms.answer("Oldin tilni tanlang βοΈ")


@dp.message_handler(state=ChooseOption.til1)# 1. Uz En
async def tarjima_qil_uje(ms:Message):
    lang = translator.detect(ms.text).lang
    if lang == "en":
        dest = "uz"
        javob = translator.translate(ms.text, dest).text
        await ms.answer(text=javob)
    elif lang == "uz":
        dest = "en"
        await ms.answer(translator.translate(ms.text, dest).text)
    else:
        await ms.answer("πΊπΈ Ingliz yoki πΊπΏ O'zbek tilida matn kiriting βοΈ", reply_markup=glavniga)

@dp.message_handler(state=ChooseOption.til2)# 2.  Uz Ru
async def tarjima_qil_uje(ms:Message):
    lang = translator.detect(ms.text).lang
    if lang == "ru":
        dest = "uz"
        await ms.answer(translator.translate(ms.text, dest).text)
    elif lang == "uz":
        dest = "ru"
        await ms.answer(translator.translate(ms.text, dest).text)
    else:
        await ms.answer("π·πΊ Rus yoki πΊπΏ O'zbek tilida matn kiriting βοΈ", reply_markup=glavniga)


@dp.message_handler(state=ChooseOption.til3)# 3. Ru En
async def tarjima_qil_uje(ms:Message):
    lang = translator.detect(ms.text).lang
    if lang == "en":
        dest = "ru"
        await ms.answer(translator.translate(ms.text, dest).text)
    elif lang == "ru":
        dest = "en"
        await ms.answer(translator.translate(ms.text, dest).text)
    else:
        await ms.answer("π·πΊ Rus yoki πΊπΈ Ingliz tilida matn kiriting βοΈ",reply_markup=glavniga)

@dp.message_handler(state=ChooseOption.til4)# 4. Arab Uz
async def tarjima_qil_uje(ms:Message):
    lang = translator.detect(ms.text).lang
    if lang == "ar":
        dest = "uz"
        await ms.answer(translator.translate(ms.text, dest).text)
    elif lang == "uz":
        dest = "ar"
        await ms.answer(translator.translate(ms.text, dest).text)
    else:
        await ms.answer("πΈπ¦ Arab yoki πΊπΏ O'zbek tilida matn kiriting βοΈ", reply_markup=glavniga)



@dp.message_handler(state=ChooseOption.til5)# 5. Tr Uz
async def tarjima_qil_uje(ms:Message):
    lang = translator.detect(ms.text).lang
    if lang == "tr":
        dest = "uz"
        await ms.answer(translator.translate(ms.text, dest).text)
    elif lang == "uz":
        dest = "tr"
        await ms.answer(translator.translate(ms.text, dest).text)
    else:
        await ms.answer("πΉπ· Turk yoki πΊπΏ O'zbek tilida matn kiriting βοΈ",reply_markup=glavniga)


@dp.message_handler(state=ChooseOption.til6)# 6. Ko Uz
async def tarjima_qil_uje(ms:Message):
    lang = translator.detect(ms.text).lang
    if lang == "ko":
        dest = "uz"
        await ms.answer(translator.translate(ms.text, dest).text)
    elif lang == "uz":
        dest = "ko"
        await ms.answer(translator.translate(ms.text, dest).text)
    else:
        await ms.answer("π°π·Koreys yoki πΊπΏO'zbek tilida matn kiriting βοΈ",reply_markup=glavniga)

