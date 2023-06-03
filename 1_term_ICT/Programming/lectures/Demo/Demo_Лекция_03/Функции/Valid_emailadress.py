""" Программа для проверки электронной почты
Получив строку, требуется проверить, является ли строка действительным адресом
электронной почты
Электронная почта — строка (подмножество символов ASCII), разделенная на две части
символом @, «personal_info» и доменом, то есть, personal_info@domain
"""

import re
""" модуль re обеспечивает поддержку для регулярных выражений """

# регулярное выражение для проверки электронной почты

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check(email): 
    """       
    Функция для для проверки электронной почты
    """
    if(re.search(regex,email)): 
        return True 
    else: 
        return False 

      


if __name__ == '__main__' : 
    
    email = "qwerty@mail.ru"
    print(check(email))
  
    email = "my.own@mail.org"
    print(check(email))

    email = "qwerty.com"
    print(check(email))
