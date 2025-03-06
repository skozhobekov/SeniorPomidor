list = {"bug#1":"medium","bug#2":"high","bug#3":"low","bug#4":"highest","bug#5":"lowest"}
print(list)
def addNewBug(bugName, priority ):
    list[bugName] = priority
    print(list)

bugName = str(input("Введите название бага: "))
priority = str(input("Введите приоритет: "))
addNewBug(bugName, priority)

    # student = {"name": "Ivan", "age": 20}
    #
    # def addElementToDictionary():
    #     student["City"] = "New York"
    #     print(student)
    #
    # addElementToDictionary()