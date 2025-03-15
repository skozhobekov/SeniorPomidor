# Напишите функцию sum_numbers(n), которая принимает число n и возвращает сумму всех чисел от 1 до n.
def sum_numbers(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    print(f"sum is {sum}")

n = int(input("input your number: "))
sum_numbers(n)


# Напишите функцию find_min(numbers), которая принимает список чисел и возвращает минимальное число, используя цикл for.
numbers = [12,32,123,4,3,1]
def find_min(numbers):
    min_numbers = numbers[0]
    for  num in numbers:
        if num < min_numbers:
            min_numbers = num
            return min_numbers
result = find_min(numbers)
print(f"min number is: {result}")

string = str(input("input string: "))
def count_vowels(string):
    wovels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in string:
        if char in wovels:
            count+=1
    print(f"quantity of vowels is: {count}")
count_vowels(string)

def print_diamond(raws):
    for i in range(1, raws +1,  2):
        print(" " * ((raws - i) // 2) + "*" * i)

    for j in range(raws-2, 0, -2):
        print(" " * ((raws - i) // 2) + "*" * i)
raws = int(input("input odd number: "))
if raws %2 == 0:
    print("please, input odd number: ")
else:
    print_diamond(raws)

def countdown():
    number = 0
    for i in range(10, 0, -1):
        print(i)
    print("Start!")

countdown()



