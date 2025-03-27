# У вас есть целочисленный массив nums, состоящий из 2 * n элементов.
#
# Вам нужно разделить nums на n пар так, чтобы:
#
# Каждый элемент принадлежал ровно одной паре.
# Элементы в каждой паре были равны.
# Верните True, если nums можно разделить на n пар, иначе верните False.
from collections import Counter


def divideArray (nums):
    count = Counter(nums)
    for value in count.values():
        if value %2!=0:
            return False
    return True
print(divideArray([1,1,2,2,3]))

# Модная строка — это строка, в которой нет трёх подряд одинаковых символов.
#
# Дано строка s, необходимо удалить минимальное количество символов из s, чтобы строка стала модной.
#
# Верните финальную строку после удаления. Можно доказать, что ответ всегда будет уникальным.

def fancyStringEdit(s):
    lst = list(s)
    i = 0
    while i < len(lst)-2:
        if lst[i] == lst[i+1]==lst[i+2]:
            del lst[i+1]
        else:
            i+=1
    return "".join(lst)


print(fancyStringEdit("leeeetcode"))


def isPalindrom(s):
    for i in range(len(s)//2):
        left = i
        right = len(s) - i-1
        if s[left] != s[right]:
            return False
        left+=1
        right -=1
    return True


print(isPalindrom("kotok"))








