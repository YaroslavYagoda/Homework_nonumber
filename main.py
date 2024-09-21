"""
Создайте класс BankAccount с приватным атрибутом balance. Реализуйте методы для депозита, снятия и проверки баланса.
Используйте методы доступа для работы с приватным атрибутом.
Подсказка:
Для выполнения этой задачи используйте принципы инкапсуляции.
deposit money
withdraw money
check the balance
"""


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit_money(self, money: float):
        if money <= 0:
            print('Недопустимая операция')
        else:
            self.__balance += money

    def withdraw_money(self, money: float):
        if money > self.__balance:
            print('Недостаточно средств!')
        elif money <= 0:
            print('Недопустимая операция')
        else:
            self.__balance -= money

    def print_balance(self):
        return self.__balance

    balance = property(print_balance, deposit_money, withdraw_money, 'Разрешения для счета')


cash_account = BankAccount()
cash_account.print_balance()
cash_account.deposit_money(100)
cash_account.withdraw_money(10.1)
print(cash_account.print_balance())
cash_account.balance = 20
print(cash_account.balance)
cash_account.balance = -10
print(cash_account.balance)
