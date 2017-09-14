import config
import telebot
import bayes
import yandex
import weather
import pymorphy2

bot = telebot.TeleBot(config.token)

# @bot.message_handler(content_types=["text"])
# def teh_handler(message):
#     res = bayes.classify(message.text)
#     bot.send_message(message.chat.id, res)

@bot.message_handler(content_types=["text"])
def teh_handler(message):
    cat = bayes.classify(sentence= message.text)
    if cat[0] == 'news':
        res = yandex.Parse_scv()
        for news in res:
            bot.send_message(message.chat.id, news)
    elif cat[0] == 'weather':
        res = weather.TakeWeather()
        bot.send_message(message.chat.id, 'Погода за окном '+res['status'])
        bot.send_message(message.chat.id, 'Облачность ' + res['description'])
        bot.send_message(message.chat.id, 'Восход ' + res['sunrise'])
        bot.send_message(message.chat.id, 'Закат ' + res['sunset'])
        bot.send_message(message.chat.id, 'Скорость ветра = ' + str(res['windspeed']))
    elif cat[0] == 'traffic':
        photo = yandex.TraficJam()
        img = open('traffic.jpg','rb')
        bot.send_photo(message.chat.id,img)
        img.close()
    else:
        bot.send_message(message.chat.id, 'Простите, я вас не понимаю')

if __name__ == '__main__':
    bot.polling(none_stop=True)
