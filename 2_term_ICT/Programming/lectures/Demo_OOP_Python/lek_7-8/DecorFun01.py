"""
Демонстрация того, что функция может быть определена внутри другой функции и
может быть передана как параметр.
"""
  
# Добавляет приветственное сообщение в строку

def messageWithWelcome(fstr):
    """
    Декоратор — это функция, которая принимает функцию в качестве
    единственного параметра и возвращает функцию
    """
    # Вложенная функция
    def addWelcome(str_name):
        return "Welcome to " + fstr(str_name)
    # Возвращаем функцию 
    return  addWelcome

# используем @func_name, чтобы указать декоратор, который будет применен к другой функции
@messageWithWelcome
def site(site_name):
    return site_name

strm = site("ITMO")

print(strm)         # Welcome to ITMO

# Пример продемонстрировать, что
# декораторы могут быть полезны прикрепить данные
  
# Функция декоратора для прикрепления данных для функции

def attach_data(func):
    func.data = 0.13
    return func


@attach_data
def mul (x, y):
    return x * y

  
cost = mul(20, 3) * mul.data
print(cost)
