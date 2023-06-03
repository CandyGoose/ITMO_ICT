"""
Демонстрация того, что функция может быть определена внутри другой функции и
может быть передана как параметр.
"""
  
# Добавляет приветственное сообщение в строку

def messageWithWelcome(str):

    # Вложенная функция
    def addWelcome():
        return "Welcome to "
    # Возвращаем конкатенацию 
    return  addWelcome() + str

  
# Применение: получить имя, к которому добавлено приветствие

def site(site_name):
    return site_name

strm = messageWithWelcome(site("ITMO"))

print(strm)         # Welcome to ITMO

