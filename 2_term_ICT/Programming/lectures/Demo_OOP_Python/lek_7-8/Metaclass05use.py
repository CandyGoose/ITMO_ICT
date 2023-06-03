"""
Требуется: объявить класс (использующий метакласс), который не позволит классам от него наследоваться
"""

# финальный метакласс - унаследоваться от класса, имеющего своим метаклассом Final не получится
class Final(type):  
    def __new__(cls, name, bases, attr):
        # от финального класса нельзя унаследоваться
        # проверим, что класс Final не выступает в качестве базового
        # если так, укажем об ошибке, иначе создадим новый класс с атрибутами Final
        type_arr = [type(x) for x in bases]
        for i in type_arr:
            if i is Final:
                raise RuntimeError("You cannot subclass a Final class")
        return super(Final, cls).__new__(cls, name, bases, attr)


# Тест: применим метакласс, чтобы создать финальный класс Copa

class Copa(metaclass=Final):  
    def exit():
        print("Exiting...")
        quit()

# Попытка создать класс Copa, в идеале следует возбудить исключение!
class FakeCopa(Copa):  
    def scam():
        print("This is a hold up!")

cop1 = Copa()  
fakecop1 = FakeCopa()

# другой класс Final
class Goat(metaclass=Final):  
    location = "Goatland"

# Унаследоваться от финального класса не получится
class BillyGoat(Goat):  
    location = "Billyland"
