from logger import input_data, print_data, search_date, print_note, print_all_note, edit_note, delete_note


def interface():
    print('             Привет! Вы попали в приложение Заметки! \n Если Вы решили полностью удалить всю информацию '
          'из файла и начать записи с чистого листа, '
          '\n Вам необходимо заполнить первую строчку в файле вручную.'
          '\n Если хотите работать с текущим файлом, выберете действие: '
          '\n1 - сохранить данные в файл \n2 - считать все данные из файла'
          '\n3 - сделать выборку по дате \n4 - вывести выбранную записку на экран \n5 - вывести список всех записок'
          '\n6 - редактировать записку \n7 - удалить запись')
    command = int(input('Введите число: '))

    while command != 1 and command != 2 and command != 3 and command != 4 and command != 5 and command != 6 \
            and command != 7:
        print('Неправильный ввод')
        command = int(input('Введите число: '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        search_date()
    elif command == 4:
        print_note()
    elif command == 5:
        print_all_note()
    elif command == 6:
        edit_note()
    elif command == 7:
        delete_note()
