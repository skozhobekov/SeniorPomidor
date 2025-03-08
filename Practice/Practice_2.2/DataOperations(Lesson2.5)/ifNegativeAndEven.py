def checkIfNegativeAndEven(number):
    if number %2==0 and number<0:
        print("number is even and negative")
    else:
        print("number doesn't match your expectations")

number = int(input("Type your number: "))
checkIfNegativeAndEven(number)