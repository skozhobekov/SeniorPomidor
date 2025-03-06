name = str(input("Введите имя: "))
occupation = str(input("Введите профессию: "))
ifKnowValue = str(input("Любимый инструмент для тестирования: "))

print({"name":name, "occupation":occupation, "ifKnowValue":ifKnowValue})


def changeOccupation():
    occupation = str(input("Введите вашу новую профессию: "))
    return print({"name":name, "occupation":occupation, "ifKnowValue":ifKnowValue})

changeOccupation()
