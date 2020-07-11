from flask import Flask, request, abort
import datetime
import time
import ChatBot

app = Flask(__name__)

messages = [
    {'name': 'Jack', 'time': time.time(), 'text': 'пример текста'},
]
users = {'Jack': '12345'}


def filter_dicts(elements, key, min_value):
    new_elements = []
    for element in elements:
        if element[key] > min_value:
            new_elements.append(element)
    return new_elements

def send_message(name, text):
    messages.append({'name': name, 'time': time.time(), 'text': text})


@app.route("/")
def hello_view():
    return 'Hello, World! <a href="/status">Status</a>'


@app.route("/status")
def status_view():
    return {
        'status': 200,
        'Name': 'KoshkinChat',
        'Time': datetime.datetime.now().strftime('%d.%M.%Y %H:%M:%S'),
        'TotalMessages': len(messages),
        'TotalUsers': len(users)
    }


@app.route("/send", methods=['POST'])
def send_view():
    name = request.json.get('name')
    password = request.json.get('password')
    text = request.json.get('text')

    if name in users:
        if users[name] != password:
            abort(401)

    for token in [name, password, text]:
        if not (isinstance(token, str)) or not token or len(token) > 1024:
            abort(400)

    if name in users:
        # auth
        if users[name] != password:
            abort(401)
    else:
        # register
        users[name] = password
        send_message(ChatBot.BotName, ChatBot.welcome(name))
    send_message(name, text)

    if text[0] == '+':
        result = ChatBot.handler(text, users, messages)
        send_message(ChatBot.BotName, result)

    return {'ok': True}


@app.route("/messages", methods=['GET'])
def messages_view():
    try:
        after = float(request.args['after'])
    except:
        abort(400)
    filtred_messages = filter_dicts(elements=messages, key='time', min_value=after)
    return {'messages': filtred_messages}


app.run()
