import config
import telebot
from telebot import types
import bayes
import pymorphy2

bot = telebot.TeleBot(config.token)

#
# @bot.message_handler(commands=['help'])
# def help_statuses(message):
#     bot.send_message(message.chat.id, 'правки')
#     bot.send_message(message.chat.id, 'называется')
#     bot.send_message(message.chat.id, 'исправить/доработать/переработать')
#     bot.send_message(message.chat.id, 'авторизации/авторизация/авторизацией')
#     bot.send_message(message.chat.id, 'логин/пароль')
#
#
# @bot.message_handler(commands=['menu'])
# def show_menu(message):
#     markup = types.ReplyKeyboardMarkup()
#     markup.row('Техническая поддержка')
#     markup.row('Контакты')
#     markup.row('Авторизация')
#     bot.send_message(message.chat.id, 'Выберете пунки меню', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def teh_handler(message):
    res = bayes.classify(message.text)
    # words = message.text.split()
    # morph = pymorphy2.MorphAnalyzer()
    # res = ''
    # for word in words:
    #     original = morph.parse(word)[0].normal_form
    #     res = res + ' ' + original
    bot.send_message(message.chat.id, res)


if __name__ == '__main__':
    bot.polling(none_stop=True)
