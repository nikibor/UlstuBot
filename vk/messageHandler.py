import vkapi


def get_answer(body):
    message = "Привет, я новый бот!"
    return message


def create_answer(data, token):
    user_id = data['user_id']
    message = get_answer(data['body'].lower())
    vkapi.send_message(user_id, token, message)
