# birthdate = int(input("your date of birth: ").strip())

# def countAge(birthdate):
#     age = 2025 - birthdate
#     print(f"your age is {age}")
#     if age < 18:
#         print("Вы еще молоды, учеба — ваш путь!")
#     elif age > 18 and age < 65:
#         print("Отличный возраст для карьерного роста!")
#     elif age > 65:
#         print("Пора наслаждаться заслуженным отдыхом!")
#
# countAge(birthdate)
#
# Напишите программу, которая выводит числа от 1 до n (включительно), но:
#
# Если число делится на 3, вместо числа выведите "Fizz".
# Если число делится на 5, вместо числа выведите "Buzz".
# Если число делится и на 3, и на 5, выведите "FizzBuzz".
# В остальных случаях выведите само число.
#
#
# Пример входных данных:
n = int(input("input number: "))

for i in range(1, n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i % 5 ==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)