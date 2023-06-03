
def fun(obj, index):
    return obj[index]


x = "ABBA"
print(fun(x,3))
# print(fun(x,4)) # IndexError: string index out of range

try:
    k = int(input("Введите индекс: "))
    f = fun(x,k)
except ValueError as er:
    print('Внимание! ', type(er), er)
except IndexError: # Перехватывает и обрабатывает исключение
    print('\nИндекс вне диапазона')
else:
    print("\nВвод успешный, элемент: ", f)

"""
Проверьте при правильном вводе и вводе ошибки
В случае ошибки ввода - NameError: name 'f' is not defined
Почему?
"""
print("\nЭлемент: ", f)
