from random import randint

n_comp = randint(1, 100)
print('Компьютер "загадал" число в интервале от 1 до 100. Какое?')
n = 0 #Счетчик числа попыток
while True: #Повторение попыток
    n = n + 1 #Номер очередной попытки
    otvet = int(input('Наберите это число '))
    if otvet > n_comp:
        print('Загаданное число меньше.')
    elif otvet < n_comp:
        print('Загаданное число больше.')
    else:
        print('Правильно! Число попыток отгадывания -', n)
        break #Выход из цикла
