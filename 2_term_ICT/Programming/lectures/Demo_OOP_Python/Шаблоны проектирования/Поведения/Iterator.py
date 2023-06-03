# Итератор (Iterator)
# Поведенческий паттерн проектирования, созданный для обхода коллекций и упрощения классов
# хранения данных, вынося реализацию (или разные реализации) обхода в другие классы.
 
class IteratorBase():
    """Базовый класс итератора"""
    def first(self):
        """Возвращает первый элемент коллекции.
        Если элемента не существует возбуждается исключение IndexError."""
        raise NotImplementedError()
 
    def last(self):
        """Возвращает последний элемент коллекции.
        Если элемента не существует возбуждается исключение IndexError."""
        raise NotImplementedError()
 
    def next(self):
        """Возвращает следующий элемент коллекции"""
        raise NotImplementedError()
 
    def prev(self):
        """Возвращает предыдущий элемент коллекции"""
        raise NotImplementedError()
 
    def current_item(self):
        """Возвращает текущий элемент коллекции"""
        raise NotImplementedError()
 
    def is_done(self, index):
        """Возвращает истину если элемент с указанным индексом существует, иначе ложь"""
        raise NotImplementedError()
 
    def get_item(self, index):
        """Возвращает элемент коллекции с указанным индексом, иначе выбрасывает исключение IndexError"""
        raise NotImplementedError()
 
 
class Iterator(IteratorBase):
    def __init__(self, list_=None):
        self._list = list_ or []
        self._current = 0
 
    def first(self):
        return self._list[0]
 
    def last(self):
        return self._list[-1]
 
    def current_item(self):
        return self._list[self._current]
 
    def is_done(self, index):
        last_index = len(self._list) - 1
        return 0 <= index <= last_index
 
    def next(self):
        self._current += 1
        if not self.is_done(self._current):
            self._current = 0
        return self.current_item()
 
    def prev(self):
        self._current -= 1
        if not self.is_done(self._current):
            self._current = len(self._list) - 1
        return self.current_item()
 
    def get_item(self, index):
        if not self.is_done(index):
            raise IndexError('Нет элемента с индексом: %d' % index)
        return self._list[index]
 
 
it = Iterator(['one', 'two', 'three', 'four', 'five'])

li = [it.prev() for i in range(5)]
print(li)           # ['five', 'four', 'three', 'two', 'one']
li = [it.next() for i in range(5)]
print(li)           # ['two', 'three', 'four', 'five', 'one']
