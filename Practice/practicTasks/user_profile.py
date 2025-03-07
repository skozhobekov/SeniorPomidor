name = str(input("Введите имя: "))
occupation = str(input("Введите профессию: "))
lovelyTool = str(input("Любимый инструмент для тестирования: "))

print({"name":name, "occupation":occupation, "lovelyTool":lovelyTool})


def changeOccupation():
    occupation = str(input("Введите вашу желаемую профессию: "))
    return print({"name":name, "occupation":occupation, "lovelyTool":lovelyTool})

changeOccupation()
