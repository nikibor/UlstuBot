from flask import Flask, request, json
import settings
import vk
import messageHandler

app = Flask(__name__)


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return settings.confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], settings.token)
        return 'ok'
