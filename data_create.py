from datetime import datetime


def id_note():
    with open('data_notebook.csv', 'r', encoding='utf-8') as f:
        cont = f.readlines()
        list_id = []
        for i in range(len(cont)):
            list_id.append(int(cont[i].split(';')[0]))
            new_id = max(list_id) + 1
    return new_id


def title_note():
    title = input('Введите Заголовок заметки: ')
    return title


def body_note():
    body = input('Введите Текст заметки: ')
    return body


def time_note():
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    return time
