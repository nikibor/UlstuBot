import vkapi
import bayes
import yandex
import weather

def get_answer(body):
    message = "Привет, я новый бот!"
    return message


def create_answer(data, token):
    user_id = data['user_id']
    message = get_answer(data['body'].lower())
    cat = bayes.classify(sentence=message)
    if cat[0] == 'news':
        res = yandex.Parse_scv()
        for news in res:
            vkapi.send_message(user_id, token, news)
    elif cat[0] == 'weather':
        res = weather.TakeWeather()
        vkapi.send_message(user_id, token, 'Погода за окном ' + res['status'])
        vkapi.send_message(user_id, token, 'Облачность ' + res['description'])
        vkapi.send_message(user_id, token, 'Восход ' + res['sunrise'])
        vkapi.send_message(user_id, token, 'Закат ' + res['sunset'])
        vkapi.send_message(user_id, token, 'Скорость ветра = ' + str(res['windspeed']))
    elif cat[0] == 0:
        vkapi.send_message(user_id, token, 'Простите, я вас не понимаю')
