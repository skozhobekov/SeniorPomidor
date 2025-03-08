error_message = input("Введите строку с ошибкой из лога: ").strip().capitalize()

error_message = error_message.replace("Ошибка", "Ошибка критическая").strip().capitalize()

print("Преобразованная строка:", error_message)

words_list = error_message.split()
print("Список слов:", words_list)