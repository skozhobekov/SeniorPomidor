from dataclasses import dataclass

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0


    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"your balance after deposit is: {self._balance}")
            return True
        else:
            print(f"amount must be positive")
            return False

    def withdraw(self, amount):
        try:
            if amount > self._balance:
                raise ValueError ("not enough money for withdraw")
            else:
                self._balance -=amount
                print(f"your new balance after withdraw is: {self._balance}")
                return self._balance
        except ValueError as err:
            print(err)

    def get_balance(self):
        return self._balance


# Ba = BankAccount("Sanjar")
# Ba.deposit(150)
# Ba.withdraw(70)
# Ba.withdraw(70)
# Ba.get_balance()

class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate


    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return self._balance

class CheckingAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance


savingAcc = SavingsAccount("Sanjar baike", 0.2)
checkingAcc = CheckingAccount(savingAcc)
print(savingAcc.deposit(500))
print(savingAcc.withdraw(10000))
print(savingAcc.apply_interest())
print(checkingAcc.deposit(500))
print(checkingAcc.withdraw(10000))


#перепиши по ТЗ withdraw в BankAccount и CheckingAccount