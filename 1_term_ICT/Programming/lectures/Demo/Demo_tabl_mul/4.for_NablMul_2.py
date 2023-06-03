from random import randint

""" 2. Реализация опроса с проверкой результата """
total = 10
for it in range(total):
    a = randint(1,10)
    b = randint(1,10)
    print(a, '*', b, '=')
    c = int(input())
    if a*b != c:
        print("Ошибка! Правильно будет", a*b)

        
"""
Следующий шаг:
    реализовать подсчет ошибочных ответов
"""




