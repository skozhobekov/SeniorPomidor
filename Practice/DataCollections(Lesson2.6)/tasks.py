list = ["kotok", "am", "tashak"]

def addElementToList(str):
    list.append(str)
    return print(list)
addElementToList(str(input("Введите ваше слово: ")))

def deleteElementFromList(int):
    list.remove(list[int])
    return print(list)
deleteElementFromList(1)

cities = ["Moscow", "Saint-Petersburg", "New York", "Tokyo"]

def pickCityByIndex(int):
    return print(cities[int])
pickCityByIndex(1)

numbers = [0,1,2,3,4,5,6,7,8,9]

def accessToElementBySlice(int, int2):
    return print("the slice is: ", numbers[int:int2])

accessToElementBySlice(int(input("Введите первый индекс: ")),int(input("Введите второй индекс: ")))

