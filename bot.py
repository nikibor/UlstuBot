import config
import telebot
import bayes
import yandex
import pymorphy2

bot = telebot.TeleBot(config.token)

# @bot.message_handler(content_types=["text"])
# def teh_handler(message):
#     res = bayes.classify(message.text)
#     bot.send_message(message.chat.id, res)

@bot.message_handler(content_types=["text"])
def teh_handler(message):
    res = yandex.Parse_scv()
    print(res)
    bot.send_message(message.chat.id, res)

if __name__ == '__main__':
    bot.polling(none_stop=True)
