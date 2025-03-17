# #Функция принимает на вход список имен людей, которым понравился предмет, необходимо вернуть сообщение с именами этих людей по определенному шаблону.
# def names_list(names):
#     # for name in names:
#         if not names:
#             return "no one likes this"
#         elif  len(names) == 1:
#             return  f"{names[0]} likes this"
#         elif len(names) ==2:
#             return f"{names[0]} and {names[1]} like this"
#         elif len(names) ==3:
#             return f"{names[0]}, {names[1]},{names[2]} are like this"
#         else:
#             return f"{names[0]}, {names[1]}, and {len(names) -2} others are like this"
#
#
# print(names_list([]))
# print(names_list(["Peter"]))
# print(names_list(["Jacob", "Alex"]))
# print(names_list(["Max", "John", "Mark"]))
# print(names_list(["Alex", "Jacob", "Mark", "Max"]))
#
#
# Вернуть средний символ слова.
# Условия:
# Если длина слова нечетная, вернуть средний символ.
# Если длина слова четная, вернуть 2 средних символа.
import math


def middleSymbol(word):
    symbolsList = list(word)
    lenght = len(symbolsList)
    if lenght%2==0:
        return symbolsList[(lenght//2)-1], symbolsList[(lenght//2)]
    else:
        return symbolsList[math.ceil(lenght//2)]

print(middleSymbol("123456"))

# Преобразуйте положительное число в перевернутый массив цифр - вывести цифры числа в обратном порядке.
# #35231 => [1,3,2,5,3]
# #0 => [0]
# #23582357 => [7,5,3,2,8,5,3,2]


def turnAroundNumber(num):
    numString = str(num)
    num_massive = list(numString)
    num_massive.reverse()
    return num_massive

print(turnAroundNumber(12345))
