def checkNumberForDiapason(number):
    if number<0 or number > 100:
            print("число выходит из диапазона")
    else:
        print("число в диапазоне")

number = int(input("введите ваше число: "))
checkNumberForDiapason(number)