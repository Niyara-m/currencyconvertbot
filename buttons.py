from telebot import types

def choice_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    euro = types.KeyboardButton('евро')
    dollar = types.KeyboardButton('доллар')
    ruble = types.KeyboardButton('рубль')

    kb.add(euro, dollar, ruble)
    return kb