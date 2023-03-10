from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.callback_data import CallbackData
til_call = CallbackData("language","til")


dict_langs = {
    "๐บ๐ฟO'zbek ๐ ๐บ๐ธIngliz":"uz_en",
    "๐บ๐ฟO'zbek ๐ ๐ท๐บRus":"uz_ru",
    "๐ธ๐ฆArab ๐ ๐บ๐ฟO'zbek":"ar_uz",
    "๐ท๐บRus ๐ ๐บ๐ธIngliz":"ru_en",
    "๐น๐ทTurk ๐ ๐บ๐ฟO'zbek":"tr_uz",
    "๐ฐ๐ทKoreys ๐ ๐บ๐ฟO'zbek":"ko_uz"
}

tillar = InlineKeyboardMarkup(row_width=2)

for til, calll in dict_langs.items():
    tillar.insert(InlineKeyboardButton(text=til, callback_data=til_call.new(til=calll)))


navigatsiya = InlineKeyboardMarkup(row_width=2)
navigatsiya.insert(InlineKeyboardButton("โ๏ธ Orqaga", callback_data="tillarga"))
navigatsiya.insert(InlineKeyboardButton("๐งฉ Bosh menuga", callback_data="bosh_menuga"))

glavniga = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
glavniga.insert(KeyboardButton("๐งฉ Bosh menuga"))