"""
Требуется:
Расширить возможности компании, добавив наличие у клиента тарифного плана,
в каждом из которых есть тип звонка («городской» и «мобильный»):
 - Повременный: «городской» (5 руб./мин.) и «мобильный» (1 руб./мин.);
 - После10МинутВ2РазаДешевле: после 10 минут звонка на городской номер каждая вторая минута бесплатно; в остальном как Повременный;
 - ПлатиМеньшеДо5Минут: до 5 минут разговора в 2 раза дешевле тарифа Повременный, после - в 2 раза дороже.

Решение:
    Добавление строкового поля call_plan и расширение существующего условия списывания средств в методе record_call()
"""

class Customer:
    """Клиент телефонной компании."""
 
#    def __init__(self, name, balance=0):
    def __init__(self, name, balance=0, call_plan="Повременный"): # "Повременный" по умолчанию
        self.name = name
        self._balance = balance
        self.call_plan = call_plan             
 
    def __str__(self):
#        return "Клиент \"{}\". Баланс: {} руб.".format(self.name, self.balance)
       return "Клиент \"{}\". Баланс: {} руб. Тариф: \"{}\"". \
            format(self.name, self.balance, self.call_plan)
 
    @property
    def balance(self):
       """Вернуть баланс клиента.
        Свойство 'balance' доступно только для чтения:
        давать доступ на изменение его напрямую было бы неправильно."""
       return self._balance

    def record_payment(self, amount_paid):
        """ Пополнить баланс клиента на 'amount_paid' руб."""
        assert amount_paid > 0, "Сумма пополнения должна быть > 0!"
        self._balance += amount_paid

    def record_call(self, call_type, minutes):
        """Списать стоимость звонка с баланса клиента.

        Параметры:
            - call_type (str): тип звонка:
                "Г": городской;
                "М": мобильный;
             - minutes (float): количество минут разговора.
        """
##        if call_type == "Г":
##            self._balance -= minutes * 5
##        elif call_type == "М":
##            self._balance -= minutes * 1
        if self.call_plan == "Повременный":
             # Фиксированная стоимость минуты в зависимости от типа звонка
            if call_type == "Г":
                 self._balance -= minutes * 5
            elif call_type == "М":
                 self._balance -= minutes * 1
        elif self.call_plan == "После10В2РазаДешевле":
             # После 10 минут звонка на городской номер
             # каждая вторая минута бесплатно
            if call_type == "Г":
                if minutes > 10:
                    bonus_minutes = (minutes - 10) // 2
                else:
                    bonus_minutes = 0
                self._balance -= (minutes - bonus_minutes) * 5
            elif call_type == "М":
                 self._balance -= minutes * 1

        elif self.call_plan == "ПлатиМеньшеДо5Минут":
             # До 5 минут разговора в 2 раза дешевле тарифа 'Повременный',
             # после - в 2 раза дороже
            LIMIT_CHEAP = 5
            if minutes > LIMIT_CHEAP:
                cheap_minutes = LIMIT_CHEAP
                expensive_minutes = minutes - LIMIT_CHEAP
            else:
                cheap_minutes = minutes
                expensive_minutes = 0

            if call_type == "Г":
                self._balance -= cheap_minutes * 2.5 + expensive_minutes * 10
            elif call_type == "М":
                self._balance -= cheap_minutes * 0.5 + expensive_minutes * 2
 
if __name__ == "__main__":
 
#    elena = Customer("Елена Миронова", 100)
    ivan = Customer("Иван Петров", 100)
    elena = Customer("Елена Миронова", 100, call_plan="После10В2РазаДешевле")
    ekaterina = Customer("Екатерина Ефимова", 100, call_plan="После10В2РазаДешевле")
    sergey = Customer("Сергей Васильев", 100, call_plan="ПлатиМеньшеДо5Минут")
 
    ivan.record_call("Г", 20)
    ivan.record_call("М", 5)
    elena.record_call("М", 10)
    elena.record_call("Г", 20)
    ekaterina.record_call("М", 20)
    sergey.record_call("Г", 20)
 
    ivan.record_payment(155)  # Пополнили телефон на 155 руб.

#    print(ivan)  # Клиент "Иван Петров". Баланс: 50 руб.
#    print(elena)  # Клиент "Елена Миронова". Баланс: 90 руб.
    print(ivan)       # "Иван Петров".       Баланс: 150 руб.      Тариф: "Повременный"
    print(elena)      # "Елена Миронова".    Баланс: 15 руб.     Тариф: "После10В2РазаДешевле"
    print(ekaterina)  # "Екатерина Ефимова". Баланс: 80 руб.     Тариф: "После10В2РазаДешевле"
    print(sergey)     # "Сергей Васильев".   Баланс: -62.5 руб.  Тариф: "ПлатиМеньшеДо5Минут"
