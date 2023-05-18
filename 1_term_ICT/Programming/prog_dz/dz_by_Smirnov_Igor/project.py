import datetime

def from_file_to_list(name_file): #Получение элементов из файла, превращение в массив
    perem_file = open(name_file, 'r', encoding='utf-8')
    zapisi = []
    for i in perem_file:
        name_cost_category = list(map(str, i.split()))
        zapisi.append(name_cost_category)
    perem_file.close()
    for i in range(len(zapisi)):
        if zapisi[i] == zapisi[-1]:
            break
        zapisi[i]=zapisi[i]
    return zapisi

def minor(massive): #Все слова записываются с большой буквы
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            massive[i][j] = massive[i][j].capitalize()
    return massive

def category(massive): #Определение категории товара
    categories = {}
    for i in massive:
        if i[2] not in categories:
            categories.setdefault(i[2], [])
        categories[i[2]].append(i[0])
    return categories

def category_variable(dictionary, massive): #Отбор необходимых записей для вывода по датам
    keys_dict = list(dictionary.keys())
    print('Выберите категорию из списка возможных')
    for i in range(len(keys_dict)):
        print(i+1, keys_dict[i])
    picked_data = input('Введите одну из перечисленных категорий. Напишите название этой категории, а не порядковый номер ')
    print()
    view_data = []
    if picked_data in keys_dict:
        for i in range(len(massive)):
            if massive[i][2] == picked_data:
                view_data.append(massive[i])
        return view_data
    else:
        print('Такой категории нет в базе \nВывод записей невозможен') #возможно здесь придется как-то зацикливать



def prosmotr_zapis(massive): #Реализация функции №2
    if massive is not None:
        if len(massive) != 0:
            print('Все существующие записи: ')
            for i in range(len(massive)):
                print(i+1, ' '.join(massive[i]))
            print()
        else:
            print()
    else:
        print()

def zapis(massive): #Реализация функции №1
    current_day = datetime.datetime.now()
    use_date = str(current_day.day) + '-' + str(current_day.month) + '-' + str(current_day.year)
    new_elem = list(map(str, input('Введите продукт, его цену и категорию ').split()))
    print()
    for i in range(len(new_elem)):
        new_elem[i].capitalize()
    new_elem.append(use_date)
    if int(new_elem[1]) >= 0:
        for i in range(len(new_elem[1])):
            if new_elem[1][i] not in '01234456789':
                print('Неправильный ввод! Невозможно сохранить элемент')
                return massive
        else:
            massive.append(new_elem)
            print('Новый продукт успешно добавлен в базу!')
            return massive
    else:
        print('Неправильный ввод! Невозможно сохранить элемент')
        return massive


def cost_sort(massive): #Сортировка по цене - функция 5
    rvrs = input('Сортировка по цене: от большего к меньшему = max, от меньшего к большему = min ')
    massive_new = massive[:]
    if rvrs == 'min':
        for i in range(len(massive)-1):
            for j in range(len(massive)-i-1):
                if int(massive_new[j][1]) > int(massive_new[j+1][1]):
                    massive_new[j], massive_new[j+1] = massive_new[j+1], massive_new[j]
    elif rvrs == 'max':
        for i in range(len(massive) - 1):
            for j in range(len(massive) - i - 1):
                if int(massive_new[j][1]) < int(massive_new[j + 1][1]):
                    massive_new[j], massive_new[j + 1] = massive_new[j + 1], massive_new[j]
    else:
        massive_new = []
        print('Некорректный ввод!')
    return massive_new

def data_sort(massive): #сортировка по дате добавления
    dates = {}
    for i in massive:
        if i[-1] not in dates:
            dates.setdefault(i[-1], [])
        dates[i[-1]].append(i[0])
    return dates

def data_variable(dictionary, massive): #Отбор необходимых записей для вывода по датам
    keys_dict = list(dictionary.keys())
    print('Выберите дату из списка возможных ')
    for i in range(len(keys_dict)):
        print(i+1, keys_dict[i])
    picked_data = input('Введите одну из перечисленных дат. Введите дату, а не порядковый номер ')
    print()
    view_data = []
    if picked_data in keys_dict:
        for i in range(len(massive)):
            if massive[i][3] == picked_data:
                view_data.append(massive[i])
        return view_data
    else:
       print('Такой даты нет в базе \nВывод записей невозможен')
       return view_data


def deleted(massive): #функция 5 - удаление
    for i in range(len(massive)):
        print(i+1, 'запись:', ' '.join(massive[i]))
    numb_of_deleted = input('Введите номер записи, которую хотите удалить ')
    print()
    if int(numb_of_deleted) <= len(massive):
        del massive[int(numb_of_deleted)-1]
        print('Удаление прошло успешно')
    else:
        print('Такого номера нет в списке!')
    return massive

def upd(massive, name_file): #обновление файла
    with open(name_file, 'w', encoding='utf-8') as fin_file:
        for elem in massive:
            for i in elem:
                if i == elem[0]:
                    fin_file.write(i)
                else:
                    fin_file.write(' ' + i)
            fin_file.write('\n')
    fin_file.close()

def start():
    print('Вы вошли в систему')
    print()
    input('Нажмите Enter для продолжения')
    print()

def end():
    print('Вы вышли из системы')
    exit()


def main_page(massive, name_file):
    cmd = ['Просмотр', 'Новая запись', 'Просмотр по дате записи', 'Просмотр по категории', 'Сортировать по цене', 'Удалить запись', 'Выйти']
    print('Доступные команды:')
    for i in range(len(cmd)):
        print(str(i+1)+'.', cmd[i])
    command = (input('Введите номер желаемой команды '))
    print()
    massive = minor(massive)
    if command == '1':
        prosmotr_zapis(massive)
        input('Нажмите Enter для продолжения ')
        print()
        main_page(massive, name_file)
    elif command == '2':
        upd(zapis(massive), name_file)
        from_file_to_list(name_file)
        print()
        input('Нажмите Enter для продолжения')
        main_page(massive, name_file)
    elif command == '3':
        prosmotr_zapis(data_variable(data_sort(massive), massive))
        input('Нажмите Enter для продолжения ')
        print()
        main_page(massive, name_file)
    elif command == '4':
        prosmotr_zapis(category_variable(category(massive), massive))
        input('Нажмите Enter для продолжения ')
        print()
        main_page(massive, name_file)
    elif command == '5':
        prosmotr_zapis(cost_sort(massive))
        input('Нажмите Enter для продолжения ')
        print()
        main_page(massive, name_file)
    elif command == '6':
        upd(deleted(massive), name_file)
        print()
        input('Нажмите Enter для продолжения ')
        main_page(massive, name_file)
    elif command == '7':
        end()
    else:
        print('Ошибка! Такой команды нет. Повторите попытку')
        print()
        input('Нажмите Enter для продолжения ')
        main_page(massive, name_file)

#Основной блок
main_file= 'base.txt'
massive_file=from_file_to_list(main_file)
start()
main_page(massive_file, main_file)