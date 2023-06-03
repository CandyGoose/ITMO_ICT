"""
Функции являются объектами и их можно передавать в качестве аргументов другим функциям.
Функции, которые в качестве аргументов могут принимать другие функции
называются функциями высокого порядка - higher-order functions

определены две функции, изменяющее поведение
"""

def whisper(text):
    '''переводит в нижний регистр - тихо'''
    return text.lower()

def yell(text):
    '''переводит в верхний регистр'''
    return text.upper()

def greet(func, txt):
    greeting = func(txt)
    return greeting


print("тихо:", greet(whisper, 'Привет! Я — программа Python'))
print("громко:", greet(yell, 'Привет! Я — программа Python'))

