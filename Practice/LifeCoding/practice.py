# Даны две строки s и t. Нужно определить, является ли s подпоследовательностью t.
#
# Подпоследовательность — это строка, которая может быть получена из t путем удаления некоторых (возможно, нуля)
# символов без изменения порядка оставшихся символов.
#
# Примеры:
# s = "abc"
# t = "ahbgdc"
# Вывод: True
# Объяснение: Символы "abc" встречаются в "ahbgdc" в том же порядке.
#
# s = "axc"
# t = "ahbgdc"
# Вывод: False
# Объяснение: Символ "x" отсутствует в "ahbgdc", поэтому s не является подпоследовательностью.

s="abc"
t="ahbgdc"

def fun(s,t):
    new = [i for i in list(t) if i in list(s)]
    if new==list(s):
        return True
    else:
        return False

    #print(new3)
    # for i in new2:
    #     if i not in new1:
    #         del i
    #     else:
    #         new3.append(i)
    # print(new3, new1)
    # if new1 == new3:
    #     return True
    # else:
    #     return False
print(fun(s,t))
