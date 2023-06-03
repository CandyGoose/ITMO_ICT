'''Аннотации являются полностью необязательной информацией метаданных о используемых типах,
Для переменных аннотации типов пишутся не в комментариях или docstring,
а непосредственно в коде.
Аннотация содержит непосредственно ожидаемый тип.
'''
x: int = 10
x = 'str' # можно присвоить  
s: str = 'hello'

print(x * 3)
print(s.startswith('h'))

'''Параметры функции аннотируются так же как переменные,
возвращаемое значение указывается после стрелки -> до завершающего двоеточия
'''
def sum_two_numbers(a: int, b: int) -> int:
   return a + b

def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello", name)
'''До версии 3.9 для явного указания, что структура данных должна состоять
только из эементов определенного типа, нужно было импортировать модуль typing:
from typing import List, Dist
'''

'''переменная может обладать свойствами, охватывающими нескольких типов.
Этого можно достичь при помощи generic-типа Union из модуля typing'''
from typing import Union

def get_room_temperature(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    return a*b  

'''возможно либо значение определенного типа, либо None'''
from typing import Optional, Union

# это одно и то же, но первый вариант проще читается
phone: Optional[str]
phone: Union[str, None]

'''функция может принимать на вход абсолютно что угодно.
Для этих случаев есть специальный объект typing.Any'''
from typing import Any

def func(arg: Any) -> Any:
    return arg



if __name__ == '__main__':
    a: list = [7]
    names: list = ['Вася', 'Петя']
    sum = sum_two_numbers(a, a*2)
    print(sum)
    ''' Аннотации хранятся в атрибуте функции __annotations__ как словарь
    и не влияют ни на какую другую часть функции'''
    print(sum_two_numbers.__annotations__)
    greet_all(names)
