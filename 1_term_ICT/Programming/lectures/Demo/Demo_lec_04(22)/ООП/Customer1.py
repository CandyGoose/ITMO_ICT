class Customer:
    """Клиент телефонной компании."""

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance

    def __str__(self):
        return "Клиент \"{}\". Баланс: {} руб.".format(self.name, self.balance)

    @property
    def balance(self):
        """Вернуть баланс клиента.
        Свойство 'balance' доступно только для чтения:
        """
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
            - minutes (float): количество минут разговора.
        """
        if call_type == "Г":
            self._balance -= minutes * 5
        elif call_type == "М":
            self._balance -= minutes * 1


if __name__ == "__main__":

    ivan = Customer("Иван Петров")
    elena = Customer("Елена Миронова", 100)

    ivan.record_call("Г", 20)
    ivan.record_call("М", 5)
    elena.record_call("М", 10)

    ivan.record_payment(155)    # Пополнили телефон на 155 руб.

    print(ivan)                 # Клиент "Иван Петров". Баланс: 50 руб.
    print(elena)                # Клиент "Елена Миронова". Баланс: 90 руб.
