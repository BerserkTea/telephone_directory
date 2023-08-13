# """
# w - перезапись
# r - чтение
# a - дозапись
# encodinf = "UTF-8"

# справочник должен содержать данные:
# имя, телефон, комментарий
# хранится в файле phone.txt
# Кирилл; 899999999; Семинары

# выводить все контакты на экран
# добавить контакт
# удалить контакт
# изменить контакт
# найти контакт конкретный
# открыть сохранить файл целиком
# выход из меню
# можно сделать копию, поработать и сохранить
# """

file = "phone.txt"


def add_contact(contact, file):
    with open(file, 'a', encoding='UTF-8') as add_c:
        add_c.write(f'{contact}\n')


def delete_contact(file):
    with open(file, "r", encoding='UTF-8') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        data = list(enumerate(lines))
        for line in data:
            print(line)
        contact = int(input('Введите порядковый номер контакта для удаления'))
        print(f' Запись о контакте "{lines.pop(contact)}" удалена')
        data = list(enumerate(lines))                                                           #{Хочу попроще, но пока не понял как и куда}
        for line in data:
            print(line)
        with open(file, "w", encoding='UTF-8') as f:
            for line in lines:
                # if line.strip("\n") != contact:  # ТУт я чето пытался там изобразить, точнее мои коллеги, но я решил не изобретать велосипед.
                f.write(f'{line}\n')


def change_contact(file):
    with open(file, "r", encoding='UTF-8') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        data = list(enumerate(lines))
        for line in data:
            print(line)
        number = int(
            input("Введите порядковый номер конатакта который хотите изменить или введите 0 для выхода в главное меню: "))
        changes = input(
                "Введите изменение в формате <Имя; Номер; Комментарий> : ")
        lines[number] = (f"{changes}") # А может надо переност строки?
        with open(file, "w", encoding='UTF-8') as f:
            for line in lines:
                f.write(f'{line}\n')
        
        
def find_contact(file):
    with open(file, "r", encoding='UTF-8') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        name = input("Введите параметр поиска (имя, номер, комментарий): ")
        for line in lines:
            if name in line.split(';'):
                print(line)
        print('Поиск окончен')


def open_book(file):
    with open(file, "r", encoding='UTF-8') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        data = list(enumerate(lines))
        for i in range(len(data)):
            print(f'{i},{lines[i]}')
        save_choise = ''
        while save_choise != '0':
            save_choise = input('\nЖелаете сохранить файл? - введите 1, иначе - введите 0\n')
            if save_choise == '1':
                new_file_name = input(
                    'Введите имя файла и нажмите Enter для сохранения \n')
                with open(new_file_name, "w", encoding='UTF-8') as f:
                    for line in lines:
                        f.write(f'{line}\n')
                break
            else:
                continue


action = ''
while action != '0':
    print(
        """
    1. добавить контакт
    2. удалить контакт
    3. изменить контакт
    4. найти контакт 
    5. открыть сохранить файл целиком
    0. выход из меню
    """
    )
    action = input('Введите номер действия: ')
    if action == '1':
        contact = input("Введите данные контакта (имя; номер; комментарий): ")
        add_contact(contact, file)
    elif action == '2':
        delete_contact(file)
    elif action == '3':
        change_contact(file)
    elif action == '4':
        find_contact(file)
    elif action == '5':
        open_book(file)
