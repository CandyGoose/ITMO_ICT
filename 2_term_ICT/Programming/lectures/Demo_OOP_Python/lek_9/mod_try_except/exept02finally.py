

def fun(obj, index):
    return obj[index]

x = "ABBA"
print(fun(x,3))
# print(fun(x,4)) # IndexError: string index out of range

while True:
    try:
        k = int(input("Введите индекс: "))
        f = fun(x,k)
        break
    except ValueError as er:
        print('Внимание! ', type(er), er)
    except IndexError: # Перехватывает и обрабатывает исключение
        print('\nИндекс вне диапазона')
    finally:
        print('Отключите питание')
    print('End loop')

print(f)

    
