from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.callback_data import CallbackData
til_call = CallbackData("language","til")


dict_langs = {
    "🇺🇿O'zbek 🔄 🇺🇸Ingliz":"uz_en",
    "🇺🇿O'zbek 🔄 🇷🇺Rus":"uz_ru",
    "🇸🇦Arab 🔄 🇺🇿O'zbek":"ar_uz",
    "🇷🇺Rus 🔄 🇺🇸Ingliz":"ru_en",
    "🇹🇷Turk 🔄 🇺🇿O'zbek":"tr_uz",
    "🇰🇷Koreys 🔄 🇺🇿O'zbek":"ko_uz"
}

tillar = InlineKeyboardMarkup(row_width=2)

for til, calll in dict_langs.items():
    tillar.insert(InlineKeyboardButton(text=til, callback_data=til_call.new(til=calll)))


navigatsiya = InlineKeyboardMarkup(row_width=2)
navigatsiya.insert(InlineKeyboardButton("◀️ Orqaga", callback_data="tillarga"))
navigatsiya.insert(InlineKeyboardButton("🧩 Bosh menuga", callback_data="bosh_menuga"))

glavniga = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
glavniga.insert(KeyboardButton("🧩 Bosh menuga"))