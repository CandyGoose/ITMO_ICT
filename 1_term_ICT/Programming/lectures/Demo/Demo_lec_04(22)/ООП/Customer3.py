"""
Требуется:
Расширить возможности компании, добавив наличие у клиента тарифного плана,
в каждом из которых есть тип звонка («городской» и «мобильный»):
 - Повременный: «городской» (5 руб./мин.) и «мобильный» (1 руб./мин.);
 - После10МинутВ2РазаДешевле: после 10 минут звонка на городской номер каждая вторая минута бесплатно; в остальном как Повременный;
 - ПлатиМеньшеДо5Минут: до 5 минут разговора в 2 раза дешевле тарифа Повременный, после - в 2 раза дороже.

Решение:
    Использование принципов наследования и полиморфизма: 
       унаследовав класс Customer, можно изменить только метод расчета стоимости звонка
       (за счёт полиморфизма - переопределить работу метода), а далее использовать новый класс,
       если клиент использует новый тарифный план 
"""

class Customer:
    """Клиент телефонной компании.
    Расходы данного клиента ведутся на повременной основе."""

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance

    def __str__(self):
        return "Клиент \"{}\". Баланс: {} руб.".format(self.name, self.balance)

    @property
    def balance(self):
        """Вернуть баланс клиента.
        Свойство 'balance' доступно только для чтения:
        давать доступ на изменение его напрямую было бы неправильно."""
        return self._balance

    def record_payment(self, amount_paid):
        """Пополнить баланс клиента на 'amount_paid' руб."""
        assert amount_paid > 0, "Сумма пополнения должна быть > 0!"
        self._balance += amount_paid

    def record_call(self, call_type, minutes):
        """Списать стоимость звонка с баланса клиента.
        Параметры:
            - call_type (str): тип звонка:
                "Г": городской;
                "М": мобильный;
            - minutes (int): количество минут разговора.
        """
        if call_type == "Г":
            self._balance -= minutes * 5
        elif call_type == "М":
            self._balance -= minutes * 1


class CustomerFree2ndMinuteAfter10(Customer):
    """Клиент телефонной компании (потомок Customer).
    После 10 минут звонка на городской номер каждая вторая минута бесплатно;
    в остальном как "Повременный".
    Все атрибуты, что предоставляет Customer, доступны и здесь, достаточно
    изменить только те, которые должны работать по-другому."""

    def record_call(self, call_type, minutes):
        # Данный метод переопределяет соответствующий метод родителя
        # Определяем количество бесплатных минут
        if call_type == "Г" and minutes > 10:
            bonus_minutes = (minutes - 10) // 2
        else:
            bonus_minutes = 0
        # Вызываем родительский метод расчета
        super().record_call(call_type, minutes - bonus_minutes)


class CustomerTwiceCheaperFirst5Minutes(Customer):
    """Клиент телефонной компании (потомок Customer).
    До 5 минут разговора в 2 раза дешевле тарифа "Повременный",
    после - в 2 раза дороже.
    Все атрибуты, что предоставляет Customer, доступны и здесь, достаточно
    изменить только те, которые должны работать по-другому."""

    def record_call(self, call_type, minutes):
        # Данный метод переопределяет соответствующий метод родителя
        LIMIT_CHEAP = 5
        if minutes > LIMIT_CHEAP:
            cheap_minutes = LIMIT_CHEAP
            expensive_minutes = minutes - LIMIT_CHEAP
        else:
            cheap_minutes = minutes
            expensive_minutes = 0
        # Вызываем родительский метод расчета
        super().record_call(call_type, cheap_minutes / 2 +
                                       expensive_minutes * 2)


if __name__ == "__main__":

    ivan = Customer("Иван Петров", 100)
    # Елена, Екатерина и Сергей будут экземпляры других классов
    elena = CustomerFree2ndMinuteAfter10("Елена Миронова", 100)
    ekaterina = CustomerFree2ndMinuteAfter10("Екатерина Ефимова", 100)
    sergey = CustomerTwiceCheaperFirst5Minutes("Сергей Васильев", 100)

    ivan.record_call("Г", 20)
    elena.record_call("Г", 20)
    ekaterina.record_call("М", 20)
    sergey.record_call("Г", 20)

    print(ivan)       # "Иван Петров".       Баланс: 0 руб.      Тариф: "Повременный"
    print(elena)      # "Елена Миронова".    Баланс: 50 руб.     Тариф: "После10В2РазаДешевле"
    print(ekaterina)  # "Екатерина Ефимова". Баланс: 80 руб.     Тариф: "После10В2РазаДешевле"
    print(sergey)     # "Сергей Васильев".   Баланс: -62.5 руб.  Тариф: "ПлатиМеньшеДо5Минут"

