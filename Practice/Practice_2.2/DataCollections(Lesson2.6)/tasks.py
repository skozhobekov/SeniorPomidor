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


colors = ["red", "blue", "pink", "black"]
def changeElement(int):
    colors[int] = "yellow"
    return print("new colors are: ", colors)
changeElement(1)

animals = ["cat", "dog", "pigWhichIsHaram", "shark"]
def lenghtOfList():
    print("Длина списка равняется: ", len(animals))
lenghtOfList()

student = {"name":"Ivan", "age":20}
def addElementToDictionary():
    student["City"] = "New York"
    print(student)
addElementToDictionary()

def changeElementInDictionary():
    student["age"] = 39
    student["City"] = "Moscow"
    print(student)
changeElementInDictionary()

def deleteElementFromDictionary():
    del student["City"]
    print(student)
deleteElementFromDictionary()

def accessToElementByKey():
    print("Ivan's age is: ", student["age"])
accessToElementByKey()

student1= {"name":"Ivan", "age":20}
def checkKeyisExist():
    print("name" in student1)
checkKeyisExist()

student2 = {"name":"Sanjar", "address":{"city":"Moscow", "street":"Lenina"}}
def changeKeyInDictionary():
    student2["address"]["city"] = "Bishkek"
    print(student2)
changeKeyInDictionary()

student3 = {"name":"Sanjar", "grades":[11,2,3]}
def changeElementInListInDict():
    student3["grades"][0] = 7
    print(student3)
changeElementInListInDict()
student4 = [{"name":"sanjar", "age":"28", "grade":"senior"}, {"name":"sultan", "age":"20", "grade":"junior"}]

def changeElementInDictInList():
    student4[0]["name"] = "SuperSanjar"
    print(student4)
changeElementInDictInList()

colors = ("red", "black", "cock", "yellow")
def checkElementAndLenght():
    lenght = len(colors)
    print("Lenght is: ", lenght)
    if "black" in colors:
        print("yes, is here")
checkElementAndLenght()