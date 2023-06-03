# Упаковка
# При упаковке аргументов все переданные позиционные аргументы
# будут собраны в кортеж 'order', а ключевые - в словарь 'info'

def print_order(*order, **info):
    print("Ваш заказ\n")

    # Словарь 'infos' должен содержать ключи 'author' и 'day'
    for key, value in sorted(info.items()):
        print(key, ":", value)

    # Кортеж 'order' содержит все наименования товара
    print("Вы выбрали:")
    for item in order:
        print("  -", item)

    print("\nПриходите еще!")



# вызов функции и передача аргументов в "упаковку"

print_order("Кресло", "Диван", "Стол", "Шкаф", "Стул",
            manager = "Иванов И.И.", day = "07/05/2020")


# Распаковка
abc = [3, 5, 4]
params = dict(print_error=True, units="кв.м.")
# При распаковке аргументов список 'abc' будет распакован в позиционные аргументы
# словарь 'params' - в именованные (ключевые)


# Площадь треугольника по формуле Герона
# функция возвращает строку

def heron_area_str(a, b, c, units="сантиметры", print_error=False):
    if a + b <= c or a + c <= b or b + c <= a:
        if print_error:
            return "Проверьте введенные стороны треугольника!"
        return

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return "\n{} {}".format(s, units)

# вызов функции и передача аргументов на распаковку

print(heron_area_str(*abc, **params))
