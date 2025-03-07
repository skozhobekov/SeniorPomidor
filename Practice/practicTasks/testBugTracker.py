bugs_found = {
    "Алексей": 5,
    "Марина": 3,
    "Санжар": 7,
    "Ольга": 2,
    "Екатерина": 4
}

your_name = str(input("Введите имя тестировщика: ").strip()).capitalize()

if your_name in bugs_found:
    bugs_found[your_name] +=1
    print("теперь у тестировщика ", your_name, bugs_found[your_name], " багов")
else:
    print("Тестировщик не найден в списке.Он будет добавлен в список")
    bugs_found[your_name] = 1
    print(bugs_found)