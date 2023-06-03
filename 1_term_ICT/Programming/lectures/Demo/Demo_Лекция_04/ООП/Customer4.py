"""
Требуется:
Расширить возможности компании, добавив наличие у клиента тарифного плана,
в каждом из которых есть тип звонка («городской» и «мобильный»):
 - Повременный: «городской» (5 руб./мин.) и «мобильный» (1 руб./мин.);
 - После10МинутВ2РазаДешевле: после 10 минут звонка на городской номер каждая вторая минута бесплатно; в остальном как Повременный;
 - ПлатиМеньшеДо5Минут: до 5 минут разговора в 2 раза дешевле тарифа Повременный, после - в 2 раза дороже.

Решение:
    Реализация тарификации по модели «включения/делегации».
    Добавить новый класс CallPlan (Тариф):
      - поле name: наименование тарифа (чтение/запись);
      -	метод record_call(): выполняет обработку звонка клиента в зависимости от:
         -- типа звонка: «городской» (5 руб./мин.) и «мобильный» (1 руб./мин.);
         -- количества минут разговора.
    Наследники классаCallPlan (прочие тарифы) будут иметь изменять необходимые атрибуты.

"""
class CallPlan:
    """Абстрактный класс для всех тарифных планов."""

    def __init__(self):
        self.name = "Абстрактный тариф"

    def record_call(self, call_type, minutes):
        """Списать стоимость звонка с баланса клиента.
        Параметры:
            - call_type (str): тип звонка:
                "Г": городской;
                "М": мобильный;

            - minutes (float): количество минут разговора.
        """
        # Делегируем расчет стоимости отдельному методу
        # Так, наследнику достаточно будет переопределить каждый из них,
        # не меняя общую логику ниже
        if call_type == "Г":
            return self.record_call_g(minutes)
        elif call_type == "М":
            return self.record_call_m(minutes)
        else:
            return 0

    def record_call_g(self, minutes):
        """Вернуть стоимость звонка на городской номер для 'minutes' минут."""
        raise NotImplementedError       # Должны реализовать дочерние классы

    def record_call_m(self, minutes):
        """Вернуть стоимость звонка на мобильный номер для 'minutes' минут."""
        raise NotImplementedError       # Должны реализовать дочерние классы


class CallPlanSimple(CallPlan):

    def __init__(self):
        self.name = "Повременный"

    def record_call_g(self, minutes):
        return minutes * 5

    def record_call_m(self, minutes):
        return minutes * 1


class CallPlanFree2ndMinuteAfter10(CallPlanSimple):

    def __init__(self):
        self.name = "После10В2РазаДешевле"

    def record_call_g(self, minutes):
        if minutes > 10:
            bonus_minutes = (minutes - 10) // 2
        else:
            bonus_minutes = 0

        # Вызываем родительский метод расчета
        return super().record_call_g(minutes - bonus_minutes)


class CallPlanTwiceCheaperFirst5Minutes(CallPlanSimple):

    def __init__(self):
        self.name = "ПлатиМеньшеДо5Минут"

    def record_call(self, call_type, minutes):
        LIMIT_CHEAP = 5
        if minutes > LIMIT_CHEAP:
            cheap_minutes = LIMIT_CHEAP
            expensive_minutes = minutes - LIMIT_CHEAP
        else:
            cheap_minutes = minutes
            expensive_minutes = 0

        # Вызываем родительский метод расчета
        return super().record_call(call_type, cheap_minutes / 2 +
                                   expensive_minutes * 2)


"""
Алгоритм подсчета стоимости звонка для класса Customer изменится:
- расчет стоимости делегируется объекту call_plan
- результат (стоимость звонка по тарифу) вычитается из баланса клиента
"""

class Customer:
    """Клиент телефонной компании."""

    def __init__(self, name, balance=0, call_plan=None):
        self.name = name
        self._balance = balance
        self.call_plan = call_plan
        # Если тарифный план не был указан, используем CallPlanSimple()
        if self.call_plan is None:
            self.call_plan = CallPlanSimple()

    def __str__(self):
        return "Клиент \"{}\". Баланс: {} руб. Тариф: \"{}\"". \
            format(self.name, self.balance, self.call_plan.name)

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
        # Делегируем определение стоимости звонка классу call_plan
        costs = self.call_plan.record_call(call_type, minutes)
        self._balance -= costs




if __name__ == "__main__":

    ivan = Customer("Иван Петров", 100)

    # 1. Используется тариф по умолчанию
    ivan.record_call("Г", 20)
    print(ivan)                 # Клиент "Иван Петров". Баланс: 0 руб. Тариф: "Повременный"

    ivan.record_payment(100 - ivan.balance)  # Пополнили телефон до 100 руб.

    # 2. Меняем тариф на CallPlanFree2ndMinuteAfter10
    ivan.call_plan = CallPlanFree2ndMinuteAfter10()
    ivan.record_call("Г", 20)
    print(ivan)                 # Клиент "Иван Петров". Баланс: 25 руб. Тариф: "После10В2РазаДешевле"

    ivan.record_payment(100 - ivan.balance)  # Пополнили телефон до 100 руб.

    # 3. Меняем тариф на CallPlanTwiceCheaperFirst5Minutes
    ivan.call_plan = CallPlanTwiceCheaperFirst5Minutes()
    ivan.record_call("Г", 20)
    print(ivan)                 # Клиент


    """ Сравнение затрат по тарифам """

    call_plans = (CallPlanSimple(),
                  CallPlanFree2ndMinuteAfter10(),
                  CallPlanTwiceCheaperFirst5Minutes())

    minutes = tuple(range(0, 26, 5))  # 0, 5, 10, 15, 20, 25 мин.

    # Сравним стоимости звонков для тарифов
    for call_type in ("Г", "М"):
        print("{:20}".format(call_type), end="")
        # Заголовок - минуты
        for minute in minutes:
            print("{:>8d} мин.".format(minute), end="")
        print()

        # Подсчет стоимости
        for call_plan in call_plans:
            print("{:20}".format(call_plan.name), end="")
            for minute in minutes:
                print("{:>8.2f} руб.".format(call_plan.record_call(call_type, minute)), end="")
            print()

        print()

