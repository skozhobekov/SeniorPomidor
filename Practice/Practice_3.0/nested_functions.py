def calc():
    a = int(input("first number: "))
    b = int(input("second number: "))
    operation = input("choose operation (-, +, *, /): ")

    def plus(a,b):
        return print("result is: ",a+b)
    def minus(a,b):
        return print("result is: ", a-b)
    def multiply(a,b):
        return print("result is: ", a*b)
    def divide(a,b):
        try:
            if b == 0:
                raise ValueError ("На ноль делить нельзя")
            return print("result is: ",a/b)
        except ValueError as error:
            print(error)

    if operation =="+":
        plus(a,b)
    elif operation == "-":
        minus(a,b)
    elif operation =="*":
        multiply(a,b)
    elif operation == "/":
        divide(a,b)

calc()