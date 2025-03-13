# Напишите функцию get_unique_elements(lst), которая принимает список чисел или строк и возвращает новый список, содержащий только уникальные элементы из исходного
def get_unique_element(lst):
    list_to_set = set(lst)
    return list_to_set

lst = [1,2,5,6,7,89,654,2,5,1]
print(get_unique_element(lst))

#Напишите функцию is_unique_list(lst), которая принимает список и возвращает True, если все элементы списка уникальны, и False, если есть повторения.
def is_unique_list(lst1):
    if len(lst1) == len(set(lst1)):
        return "true"
    else:
        return "false"

print(is_unique_list([1, 2, 3, 4]))
print(is_unique_list([1, 2, 2, 3]))

# Создайте функцию get_unique_vowels(s), которая принимает строку и возвращает набор уникальных гласных, содержащихся в строке (игнорируя регистр).
vowels = ["a", "e", "i", "o", "u"]
def get_unique_vowels(s):
    turnTolist = list(s)
    vowelsList = []
    for letter in turnTolist:
        if letter in vowels:
            vowelsList.append(letter)
    return set(vowelsList)

print(get_unique_vowels("SANJAREIO".capitalize()))
