#Напишите функцию remove_duplicates(lst), которая удаляет все повторяющиеся элементы из списка, оставляя только уникальные значения.
lst=[1,2,3,4,5,5,4,3]
def remove_duplicates(lst):
    return print(set(lst))

remove_duplicates(lst)


#Напишите функцию generate_squares(n), которая генерирует список квадратов чисел от 1 до n.
n = int(input("input n: "))
def generate_squares(n):
    for i in range(1,n+1):
        result = i ** 2
    return print(f"square of {i} is {result}")
generate_squares(n)

#Напишите функцию merge_lists(list1, list2), которая объединяет два списка, удаляя дубликаты.
list3 = list(str(input("input list1: ")))
list4 = list(str(input("input list2: ")))

def merge_lists(list1, list2):
    newList = list1 + list2
    newSet = set(newList)
    finalList = list(newSet)
    return print(finalList)

merge_lists(list3, list4)


IfSortedList = [1,2,3,4,5,1,2,3,5]
# Проверка на отсортированность
def isSorted(list):

    if list == sorted(list):
        print("yes, it is sorted")
    else:
        print("NO")

isSorted(IfSortedList)

listNO1 = [1,2,3]
listNO2 = [4,5,6]

#Слияние списков
def merge_lists(listNO1, listNO2):
    merged_list = []
    for a,b in zip(listNO1,listNO2):
        merged_list.append(a+b)
    return print(merged_list)

merge_lists(listNO1,listNO2)


