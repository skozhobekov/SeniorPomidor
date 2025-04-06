# Даны две строки s и t, состоящие из строчных букв.
# Строка t получается путем случайного перемешивания строки s с добавлением одного дополнительного символа в случайную позицию.
#
# Найти этот дополнительный символ.
#
# Примеры:
# Вход: s = "abcd", t = "abcde"
# Выход: "e"
#
# Вход: s = "aabbc", t = "aabbdc"
# Выход: "d"


def func(s,t):
    word1= sorted(list(s))
    word2 = sorted(list(t))
    new = []
    for i in word2:
        if i not in word1:
            new.append(i)
    return "".join(new)


print(func("sanjar", "rajnase"))
