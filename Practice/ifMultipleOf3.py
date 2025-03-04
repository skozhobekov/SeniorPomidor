def checkIfMultipleOfThree(number):
    if number % 3 ==0:
        print("Число кратно трём")
    else:
        print("Число некратно трём")

number = int(input("Введите ваше число: "))
checkIfMultipleOfThree(number)