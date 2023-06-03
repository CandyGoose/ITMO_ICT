from random import randint

n_comp = randint(1, 100)
print(n_comp)
print('Компьютер "загадал" число в интервале от 1 до 100. Какое?')

def check_numder(numder, n_comp):
    if numder > n_comp:
        return 'Загаданное число меньше'
    elif otvet < n_comp:
        return 'Загаданное число больше.'
    else:
        return f'Правильно! Число попыток отгадывания - {n}'

n = 1               # Счетчик числа попыток
while True: 
    otvet = int(input('Введите Ваше число '))
    answer = check_numder(otvet, n_comp)
    print(answer)
    n = n + 1
    if otvet == n_comp:
        break 

'''
Замечания по реализации:
главный цикл организует логику повторения попыток и считает их количество,
вопрос - должен ли он считать или это обязанность самой функции?
'''
