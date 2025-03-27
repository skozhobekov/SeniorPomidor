# Задача: "Наибольший общий префикс (приставка)"
# Условие:
# Напишите функцию, которая находит наибольший общий префикс среди массива строк.
#
# Если общего префикса нет, верните пустую строку "".
#
# Пример 1:
# Вход: strs = ["flower", "flow", "flight"]
# Выход: "fl"
# Объяснение: Наибольший общий префикс для всех строк — это "fl".
from os import remove

words = ["flower", "flow", "flight"]
def func(words):
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    return prefix


print(func(words))