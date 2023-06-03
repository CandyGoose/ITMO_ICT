
class Person:

    # конструктор
    def __init__(self, first_name, last_name):
        self.full_name = (first_name, last_name)       # устанавливаем полное имя


# создание объектов класса
person3 = Person("Петр", "Иванов")

print(*person3.full_name)          
