def check_grade():
    while True:
        try:
            score = int(input("Enter your score: "))
            if score < 0:
                raise ValueError("Input a positive number")

            if score >= 90 and score <= 100:
                print("Great")
            elif score >= 75:
                print("Good")
            elif score >= 50:
                print("Not bad")
            else:
                print("Bad")

            break

        except ValueError as e:
            print(f"Error: {e}, try again.")

check_grade()

def isEven():
    number = int (input("input your number: "))
    isEven = "even" if number % 2==0 else "odd"
    return print(f"number is: {isEven}")
isEven()


a = int(input("input first number: "))
b = int(input("input second number: "))

def find_max(a, b):
    try:
        if a == b:
            raise ValueError (f"{a} is equal to {b}")
        result = f"{a} is bigger" if a > b else f"{b} is bigger"
        print(result)
    except ValueError as er:
        print(er)

find_max(a,b)
number = int(input("input your number: "))
def check_number(number):
    try:
        if number<=0:
            raise ValueError (f"your number is 0 or negative")
        if number > 0 and number % 2 == 0:
            response = "Positive and even"
        else:
            response = "Positive and odd"
        return print(f"your number is {response}")
    except ValueError as er:
        print(er)
check_number(number)

string = str(input("input your text: "))
lenght = int(input("input your number: "))
def check_string_length(string, length):
    try:
        if lenght == 0:
            raise ValueError("Число равно нулю")
        lengthOf = len(string)
        if lengthOf > length:
            print("Длина строки достаточная")
        else:
            print("Строка слишком короткая")
    except ValueError as err:
        print(err)
check_string_length(string, lenght)




