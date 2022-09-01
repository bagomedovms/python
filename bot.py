import telebot
import Config
from telebot import types

bot = telebot.TeleBot(Config.TOKEN, parse_mode=None)

@bot.message_handler(content_types=['text', 'document', 'audio' ])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.inlineKeyboardMarkup()
    markup.add(types.inlinekeyboardButton("Посетить веб сайт, url=https://www.google.ru/?client=safari"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)
#

bot.polling(none_stop=True, interval=0)

