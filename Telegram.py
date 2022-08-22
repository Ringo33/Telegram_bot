import os
import telebot
from telebot import types
import vk, currency, sms
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('token_tg')
bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить веб сайт Яндекс', url='http://ya.ru'))
    buttonA = types.InlineKeyboardButton('Фильмы', callback_data='movie')
    buttonB = types.InlineKeyboardButton('Валюта', callback_data='currency')
    buttonC = types.InlineKeyboardButton('Криптовалюта', callback_data='cryptocurrency')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id,
                     'Добро пожаловать, я Helper_Bot!'
                     ' Выберите интересующую Вас категорию.',
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5, one_time_keyboard=True)
    website = types.KeyboardButton("Веб сайт")
    start = types.KeyboardButton("Старт")
    # markup.row(item1, item2, item3, item4)
    markup.add(website, start)

    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    data = call.data
    if data == 'movie':
        image = vk.vk_status(-14785431)['image']
        text = vk.vk_status(-14785431)['text']
        bot.send_photo(call.message.chat.id,
                       photo=image,
                       caption=text)
    elif data == 'currency':
        data = currency.currency_rate()
        bot.send_message(call.message.chat.id, f'{data}')
    elif data == 'cryptocurrency':
        data = currency.cryptocurrency_rate()
        bot.send_message(call.message.chat.id, f'{data}')

    bot.answer_callback_query(call.id)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() in ['привет', 'добрый день']:
        bot.send_message(message.chat.id, 'Привет, мой друг')
    elif message.text.lower() in ['пока', 'до свидания']:
        bot.send_message(message.chat.id, 'Прощай, друг')


bot.polling(none_stop=True)
