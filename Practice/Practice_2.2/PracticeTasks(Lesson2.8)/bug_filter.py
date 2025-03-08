bug_reports = [
    "Ошибка 1 – High",
    "Ошибка 2 – Medium",
    "Ошибка 3 – Low",
    "Ошибка 4 – High",
    "Ошибка 5 – Medium",
    "Ошибка 6 – Low",
    "Ошибка 7 – High"
]

priority = input("Введите приоритет (High, Medium, Low): ").strip().capitalize()

filteredBugs = [bug for bug in bug_reports
                if f"{priority}" in bug]

if filteredBugs:
    print("Баг-репорты с приоритетом", priority, ":")
    for bug in filteredBugs:
        print(bug)
else:
    print("Баг-репортов с таким приоритетом нет.")