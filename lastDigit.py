def findLastDigit(digit):
    digitStr = str(digit)
    lastDigit = digitStr[-1]
    print("Последняя цифра - ",lastDigit)


digit = int(input("Введите ваше число: "))
lastDigit = findLastDigit(digit)

