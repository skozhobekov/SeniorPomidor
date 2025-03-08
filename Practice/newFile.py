account_actions = {"initialValue":100, "withdraw1": -32, "deposit2":50}

def safe_withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError ("недостаточно средств")
        balance -= amount
        print(f"Списание прошло успешно, остаток на балансе {balance}")
    except ValueError as error:
        print(error)
safe_withdraw(1000,5000)



def print_actions(account_action):
    for action, value in account_actions.items():
        print(f"action is {action}, value is {value}")


print_actions(account_actions)
def reach_min_balance(initialB, minB):
    while initialB<minB:
        print(f"текущий баланс {initialB} меньше минмального. Добавляем депозит 50")
        initialB +=50
    print(f"Достигнут минимальный баланс {minB}")
reach_min_balance(-100, 100)

def createAcc(name, *transactions):
    print(f"создан счет для {name}")
    for transactions in transactions:
        print(f"Транзакция {transactions}")



createAcc("sanjar", 1000, 121,232,4343,34)


transaction = [1,23,13,-12,33]
def applyTrans(transactions):
    balance = 0
    for transaction in transactions:
        if transaction>0:
            print(f"пополнение на сумму {transaction}")
        else:
            print(f"снятие на суму {transaction}")
        balance += transaction
    print(f"финальный баланс {balance}")

applyTrans(transaction)