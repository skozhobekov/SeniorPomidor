week_days = ["Понедельник", "Вторник", "Среду", "Четверг", "Пятницу"]
test_cases = []

for day in week_days:
    while True:
        try:
            count = int(input(f"Введите количество тест-кейсов за {day}: "))
            if count < 0:
                raise ValueError("Количество тестов не может быть отрицательным.")
            test_cases.append(count)
            break
        except ValueError:
            print("Ошибка! Введите корректное положительное число.")

# Вычисляем общее и среднее количество тестов за неделю
total_tests = sum(test_cases)
average_tests = total_tests / 5

# Выводим результаты
print(f"\nОбщее количество тестов за неделю: {total_tests}")
print(f"Среднее количество тестов в день: {average_tests:.2f}")

# Выводим сообщение в зависимости от результата
if average_tests > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")
