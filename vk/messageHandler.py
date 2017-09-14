import vkapi
import bayes
import yandex

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
