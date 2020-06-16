import telebot
from telebot import types

bot = telebot.TeleBot('1283373857:AAGo1Sfa3rpgYjJdXBwUTjUpVq90JLVXmW8')


@bot.message_handler(commands=['link'])
def open_link(message):
    markup = types .InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти по ссылке", url="https://yandex.ru/"))
    bot.send_message(message.chat.id,
                     "Отличный выбор, прочитай статью прямо сейчас", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет, {message.from_user.first_name} {message.from_user.last_name}</b>" \
                f"\nКакой направление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)
