# композиция - Расчет полезной площади

class WinDoor:
    """
класс-часть - окна и двери являются частями комнаты,
поэтому они входят в состав объекта-помещения
    """
    def __init__(self, x, y):
          self.square = x * y


class Room:
    """
Класс "комната" – это класс-контейнер для окон и дверей.
Он должен содержать вызовы класса "окно_дверь"
    """
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []      # список окон-дверей

    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))   # заполняется список окон-дверей

    """
Функция расчитывает площадь рабочей поверхности:
площадь комнаты - площадь дверей и окон
    """
    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square



 
r1 = Room(6, 3, 3) 
print(r1.square)        # выведет 54
r1.addWD(1, 1) 
r1.addWD(1, 1)
r1.addWD(1, 2)
print(r1.workSurface()) # выведет 50
