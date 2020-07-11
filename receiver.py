from datetime import datetime

import requests
import time


def format_message(message):
    name = message['name']
    text = message['text']
    time = datetime.fromtimestamp(message['time']).strftime('%d.%M.%Y %H:%M:%S')
    return f'{name} {time}\n{text}\n'


# response=requests.get('http://127.0.0.1:5000/messages?after=0')
after = time.time() - 24 * 60 * 60
while True:
    response = requests.get('http://127.0.0.1:5000/messages', params={'after': after})
    messages = response.json()['messages']
    for message in messages:
        print(format_message(message))
        after = message['time']
    time.sleep(1)
