user_input = input("Введите список чисел через запятую: ")

numbers = [float(num.strip()) for num in user_input.split(",")]


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

bubble_sort(numbers)

print("Отсортированный список:", numbers)

# user_input = input("Введите список чисел через запятую: ")
# numbers = [num.strip() for num in user_input.split(",") ]
# print(numbers.sort())
#
# def bubble_sort(numbers):
#     numbers = [num.strip() for num in user_input.split(",") ]
#     return print(f"ваш список отсортирован по возрастанию: {numbers.sort()}")
#
# bubble_sort(user_input)