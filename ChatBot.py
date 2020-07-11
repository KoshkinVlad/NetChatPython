import math
import re

BotName = 'Кошачий чат-бот'
BotPass = 'SuperSecretPassWord!!!'


def welcome(name):
    text = f'Приветствую, {name}! Набери +команды для вывода всех доступных команд ☻'
    return text


def show_comands():
    return 'Начинай команды с символа +, чтобы я понял, что ты обращаешься ко мне. Список команд:\n' \
           '+стата : показывает статистику по участникам\n' \
           '+морзе <текст> : зашифрует текст в азбуку Морзе\n' \
           '+уравнение <a> <b> <c> : решает квадратное уравнение'


def show_statistics(users, messages):
    result = f'В этой конфе сидит {len(users)} пользователя. За всё время её существования было написано {len(messages)} сообщений.\n'
    for user in users:
        temp = 0
        result += user
        for message in messages:
            if message['name'] == user:
                temp += 1
        result += f' написал(а) {temp} сообщений\n'
    return result


def text_to_morze(text):
    dict = {
        'а': '.-',
        'б': '-...',
        'в': '.--',
        'г': '--.',
        'д': '-..',
        'е': '.',
        'ё': '.',
        'ж': '...-',
        'з': '--..',
        'и': '..',
        'й': '.---',
        'к': '-.-',
        'л': '.-..',
        'м': '--',
        'н': '-.',
        'о': '---',
        'п': '.--.',
        'р': '.-.',
        'с': '...',
        'т': '-',
        'у': '..-',
        'ф': '..-.',
        'х': '....',
        'ц': '-.-.',
        'ч': '---.',
        'ш': '----',
        'щ': '--.-',
        'ъ': '--.--',
        'ы': '-.--',
        'ь': '-..-',
        'э': '..-..',
        'ю': '..--',
        'я': '.-.-',
        ' ': ' '
    }
    result = ''
    for char in text.lower():
        try:
            result += dict[char]
            print(f'{char} : {dict[char]}')
        except:
            result += '?'
    return result


def solve_quadric_equation(text):
    coeff = re.split(r'\s', text)
    a = float(coeff[0])
    b = float(coeff[1])
    c = float(coeff[2])
    solve = f'Исходное уравнение: {a}x² + {b}x + {c} = 0\n'
    D = b * b - 4 * a * c
    if D > 0:
        sqrtD = math.sqrt(D)
        solve += f'Дискриминант: D = b² + 4ac = {D} >0. Уравнение имеет два действительных корня. √D = {sqrtD}\n'
        x1 = (-b + sqrtD) / 2 * a
        x2 = (-b - sqrtD) / 2 * a
        solve += f'x1=(-b+√D)/2a={x1}\n'
        solve += f'x2=(-b-√D)/2a={x2}\n'
    elif D == 0:
        solve += f'Дискриминант: D = b² + 4ac = {D}. Уравнение имеет один действительный корень.\n'
        x = -b / (2 * a)
        solve += f'x = -b/2a = {x}\n'
    else:
        sqrtD = math.sqrt(math.fabs(D))
        solve += f'Дискриминант: D = b² + 4ac = {D} < 0. Уравнение имеет два мнимых корня. √|D| = {sqrtD}\n'
        x = -b / (2 * a);
        y = sqrtD / (2 * a);
        solve += f'x1=(-b+i√|D|)/2a={x} + {y}i\n'
        solve += f'x2=(-b-i√|D|)/2a={x} - {y}i\n'
    return solve


def handler(text, users, messages):
    text = text[1:]
    if text == 'команды':
        return show_comands()
    elif text == 'стата':
        return show_statistics(users, messages)
    elif text[0:6] == 'морзе ':
        return text_to_morze(text[6:])
    elif text[0:10] == 'уравнение ':
        return solve_quadric_equation(text[10:])
    else:
        return 'А?'
