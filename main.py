import telebot
from telebot import types

bot = telebot.TeleBot('1283373857:AAGo1Sfa3rpgYjJdXBwUTjUpVq90JLVXmW8')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn_web = types.KeyboardButton('Веб-разработка')
    btn_mobile = types.KeyboardButton('Мобильная разработка')
    btn_ii = types.KeyboardButton('Искуственный интелект')
    btn_game = types.KeyboardButton('Game development')
    markup.add(btn_web, btn_mobile, btn_ii, btn_game)
    send_mess = f"<b>Привет, {message.from_user.first_name} {message.from_user.last_name}</b>" \
                f"\nКакой направление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text

    if get_message_bot == 'Веб-разработка':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Зачем писать на PHP в 2020?", url="https://habr.com/ru/company/skyeng"
                                                                                 "/blog/506704/"))
        markup.add(types.InlineKeyboardButton("10 полезных приёмов для JavaScript-программистов", url="https://habr"
                                                                                                      ".com/ru"
                                                                                                      "/company/ruvds"
                                                                                                      "/blog/505754/"))
        markup.add(types.InlineKeyboardButton("14 самых популярных Node.js-библиотек в 2020 году", url="https://habr"
                                                                                                       ".com/ru/post"
                                                                                                       "/506692/"))
        bot.send_message(message.chat.id, "Подборка полезных и актуальных статей про веб разаработку:",
                         parse_mode='html', reply_markup=markup)

    elif get_message_bot == 'Мобильная разработка':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Введение в мобильную разработку для Android: с каких языков начать изучение?",
                                              url="https://tproger.ru/articles/introduction-to-mobile-development/"))
        markup.add(types.InlineKeyboardButton("Натив или кроссплатформа — что выбрать начинающему мобильному разработчику?",
                                              url="https://tproger.ru/experts/native-or-crossplatform/"))
        markup.add(types.InlineKeyboardButton("Как разработать своё первое приложение на React Native",
                                              url="https://tproger.ru/articles/your-first-app-in-react-native/"))
        bot.send_message(message.chat.id, "Подборка полезных и актуальных статей про мобильную разработку:",
                         parse_mode='html', reply_markup=markup)

    elif get_message_bot == 'Искуственный интелект':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Как выучить машинное обучение: книги, курсы, подходы",
                                              url="https://tproger.ru/experts/how-to-learn-machine-learning/"))
        markup.add(types.InlineKeyboardButton("А вы уверены, что общаетесь с человеком?",
                                              url="https://tproger.ru/articles/criteria-of-humanness/"))
        markup.add(types.InlineKeyboardButton("Всё, что вам нужно знать об ИИ — за несколько минут",
                                              url="https://habr.com/ru/post/416889/"))
        bot.send_message(message.chat.id, "Подборка полезных и актуальных статей про искуственный интелект:",
                         parse_mode='html', reply_markup=markup)

    elif get_message_bot == 'Game development':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Реализация движения по лестницам в 2D-игре",
                                              url="https://habr.com/ru/post/506192/"))
        markup.add(types.InlineKeyboardButton("Разработка игр – это просто: 12 этапов изучения геймдева",
                                              url="https://proglib.io/p/gamedev-study-guide/"))
        markup.add(types.InlineKeyboardButton("Основные тенденции в левел-дизайне мультиплеерных шутеров",
                                              url="https://habr.com/ru/company/pixonic/blog/506768/"))
        bot.send_message(message.chat.id, "Подборка полезных и актуальных статей про game development:",
                         parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
