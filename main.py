import telebot, buttons
import requests, json

#Использование апи Центробанка Узбекистана
based_url = "https://cbu.uz/ru/arkhiv-kursov-valyut/json/all/"
response = requests.get(based_url)
y = response.json()
usd_cost = y[0]["Rate"]
usd_date = y[0]["Date"]
usd = y[0]["Ccy"]

eur_cost = y[1]["Rate"]
eur_date = y[1]["Date"]
eur = y[1]["Ccy"]

rub_cost = y[2]["Rate"]
rub_date = y[2]["Date"]
rub = y[2]["Ccy"]


bot = telebot.TeleBot('6427032515:AAEKHg6HJYzsW8RpXBgOokTrcZfVglcNEls')

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.from_user.id, f'{message.from_user.first_name}! Добро пожаловать в конвертинг валют!')
    bot.send_message(message.from_user.id, f'{message.from_user.first_name}! Выберите валюту для обмена', reply_markup=buttons.choice_buttons())

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == 'евро':
        bot.send_message(message.from_user.id, 'Введите сумму?', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, convert_euro)
    elif message.text.lower() == 'доллар':
        bot.send_message(message.from_user.id, 'Введите сумму?', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, convert_dollar)
    elif message.text.lower() == 'рубль':
        bot.send_message(message.from_user.id, 'Введите сумму?', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, convert_ruble)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понял')

def convert_euro(message):
    try:
        bot.send_message(message.from_user.id, f'Цена евро на дату {eur_date}: {eur_cost}{eur}; Конвертация Вашей суммы ровна: {round((int(message.text)) / float(eur_cost), 1)} {eur}',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(message.from_user.id, f'{message.from_user.first_name}! Выберите валюту для обмена', reply_markup=buttons.choice_buttons())
    except ValueError:
        bot.send_message(message.from_user.id, 'Я вас не понял, Введите пожалуйста сумму в цифрах!')
        bot.register_next_step_handler(message, convert_euro)


def convert_dollar(message):
    try:
        bot.send_message(message.from_user.id, f'Цена доллара на дату {usd_date}: {usd_cost}{usd}; Конвертация Вашей суммы ровна: {round((int(message.text)) / float(usd_cost), 1)} {usd}', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(message.from_user.id, f'{message.from_user.first_name}! Выберите валюту для обмена', reply_markup=buttons.choice_buttons())
    except ValueError:
        bot.send_message(message.from_user.id, 'Я вас не понял, Введите пожалуйста сумму в цифрах!')
        bot.register_next_step_handler(message, convert_dollar)

def convert_ruble(message):
    try:
        bot.send_message(message.from_user.id, f'Цена Рубля на дату {rub_date}: {rub_cost}{rub}; Конвертация Вашей суммы ровна: {round((int(message.text)) / float(rub_cost), 1)} {rub}', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(message.from_user.id, f'{message.from_user.first_name}! Выберите валюту для обмена', reply_markup=buttons.choice_buttons())
    except ValueError:
        bot.send_message(message.from_user.id, 'Я вас не понял, Введите пожалуйста сумму в цифрах!')
        bot.register_next_step_handler(message, convert_ruble)


bot.polling(non_stop=True)