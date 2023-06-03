# Абстрактный класс (Abstract class).
#from abc import ABCMeta
from abc import ABC
from abc import abstractmethod
"""
Модуль abc определяет мета-класс и набор декораторов.
"""
class Vehicle(ABC):
    """
    абстрактный базовый класс может быть создан простым производным от ABC,
    избегая запутанного использования метакласса
    """
#class Vehicle(metaclass=ABCMeta):
    """
    Для определения абстрактного базового класса:
    - устанавить ABCMeta как мета-класс абстрактного класса
    - пометить декораторами @abstractmethod и @abstractproperty методы и свойства,
    которые должны быть реализованы в неабстрактных потомках
    """

    @abstractmethod
    def change_gear(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def hello(self):
        print("Hello from Basic class")



print(type(ABC)) # тип ABC - ABCMeta <class 'abc.ABCMeta'>

class Car(Vehicle):

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def change_gear(self):
        print("Changing gear")
 
    def start_engine(self):
        print("Changing engine")

    def hello(self):
        """
        можем переопределять метод как в обычном наследовании,
        а вызывать родительский метод при помощи super()
        """
        super().hello()
        print("Enriched functionality")



#veh = Vehicle() # TypeError: Can't instantiate abstract class Vehicle with abstract methods change_gear, start_engine
car = Car("Toyota", "Avensis", "silver")
"""
Абстрактный класс регистрирует подкласс и проверка isinstance
возвращает корректное значение
"""
print(isinstance(car, Vehicle)) # True

car.start_engine()
car.change_gear()
car.hello()
