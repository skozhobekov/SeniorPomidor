class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance+= amount
            print(f"успешное пополнение.")

    def showBalance(self):
        print(f"ваш баланс {self.__balance}")

myAccount = Account("Sanjar", 100)
myAccount.deposit(150)
myAccount.showBalance()

class CheckingAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def deposit(self, amount):
        print(f"пополнение расчетного счета прошло успешно")
        print(f"ваш баланс теперь {amount}")

newCheck = CheckingAccount("Sultan", 1120)
newCheck.showBalance()
newCheck.deposit(11213)
