
class Person:

    # конструктор
    def __init__(self, name):
        self.name = name        # устанавливаем имя

    # деструктор
    """
    функция __del__будет вызываться либо в результате вызова оператора del,
    либо при автоматическом удалении объекта
    """
    def __del__(self):
        print(self.name,"удален из памяти")
       
    def display_info(self):
        print("Имя: {0}, Возраст: {1}".format(self.name, self.age))





