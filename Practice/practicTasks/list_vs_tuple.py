
number_list = []

for i in range(5):
    number = int(input("введите число: "))
    number_list.append(number)
print(number_list)

number_tuple = tuple(number_list)
print(number_tuple)

number_list[1] = input("введите число для обновления 2 числа: ")
print(number_list)

number_list.append(int(input("введите число: ")))
print("измененный список: ",number_list)
print("кортеж - неизменяемый тип данных")
