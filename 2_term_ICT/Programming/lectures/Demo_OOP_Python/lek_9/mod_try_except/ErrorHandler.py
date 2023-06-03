a = 10

try:
    b = int(input("Введите знаменатель: "))
    c = a/b
    print(c)
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Error - деление на нуль")
except:
    print("Error")

