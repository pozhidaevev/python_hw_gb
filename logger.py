import os
from datetime import datetime
from data_create import id_note, title_note, body_note, time_note


def input_data():
    id_nt = id_note()
    title = title_note()
    body = body_note()
    time = time_note()

    with open('data_notebook.csv', 'a', encoding='utf-8') as f:
        f.write(f'{id_nt};{title};{body};{time}\n')


def print_data():
    print('Вывожу все данные из файла: ')
    with open('data_notebook.csv', 'r', encoding='utf-8') as f:
        data_all = f.readlines()
        print(*data_all)


def search_date():
    date_note = input('     Введите дату по которой хотите найти записи. \n'
                      '                      ВАЖНО!!! \n'
                      'Дата должна быть в формате: год-месяц-число (2024-01-01): ')
    print(f'Вывожу записи от {date_note}:')
    with open('data_notebook.csv', encoding='utf-8') as my_f, open('copy_notebook.csv', 'w',
                                                                   encoding='utf-8') as copy_f:
        for line in my_f:
            if date_note in line:
                copy_f.write(line)
    with open('copy_notebook.csv', 'r',encoding='utf-8') as copy_f:
        content = copy_f.readlines()
        print(*content)


def print_note():
    search_note = input('Введите ID записи, которую хотите прочитать: ')
    print(f'Вывожу запись с ID {search_note}:')
    with open('data_notebook.csv', encoding='utf-8') as my_f, open('copy_notebook.csv', 'w',
                                                                   encoding='utf-8') as copy_f:
        for line in my_f:
            if (search_note + ';') in line:
                copy_f.write(line)
    with open('copy_notebook.csv', 'r',encoding='utf-8') as copy_f:
        content = copy_f.readlines()
        print(*content[0].split(';')[2:3])


def print_all_note():
    with open('data_notebook.csv', 'r', encoding='utf-8') as f:
        print('Вывожу все записи поочередно:')
        cont = f.readlines()
        for i in range(len(cont)):
            print(cont[i].split(';')[2])


def edit_note():
    search_note = input('Введите ID записи, которую хотите изменить: ')
    new_title = input('Введите новое название заголовка: ')
    new_body = input('Введите текст новой записи: ')
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_string = f'{search_note};{new_title};{new_body};{time}\n'
    with open('data_notebook.csv', encoding='utf-8') as my_f, open('copy_notebook.csv', 'w',
                                                                   encoding='utf-8') as copy_f:
        for line in my_f:
            if (search_note + ';') in line:
                copy_f.write(new_string)
            else:
                copy_f.write(line)
    os.remove('data_notebook.csv')
    os.rename('copy_notebook.csv', 'data_notebook.csv')


def delete_note():
    id_delete = input('Введите ID записи, которую хотите удалить: ')
    with open('data_notebook.csv', encoding='utf-8') as my_f, open('copy_notebook.csv', 'w', encoding='utf-8') as copy_f:
        for line in my_f:
            if (id_delete + ';') not in line:
                copy_f.write(line)
    os.remove('data_notebook.csv')
    os.rename('copy_notebook.csv', 'data_notebook.csv')

