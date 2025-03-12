# Частотный анализ строки
def char_frequency(s):
    newDit = {}
    for char in s:
        if char in newDit:
            newDit[char] +=1
        else:
            newDit[char] = 1
    return newDit
s = "hello"
print(char_frequency(s))

# Напишите функцию merge_dicts(dict1, dict2), которая принимает два словаря и объединяет их в один.
# Если в обоих словарях есть одинаковые ключи, суммируйте их значения (значения только числа).

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result[key] + value if key in result and isinstance(value, (int, float)) else value
    return result
dict1 = {"a": 10, "b": 20}
dict2 = {"b": 5, "c": 15}
print(merge_dicts(dict1, dict2))

# Напишите функцию dict_to_lists(my_dict), которая принимает словарь и возвращает два списка: один с ключами и другой с соответствующими значениями.
def dict_to_lists(my_dict):
    keys = []
    values = []
    for key, value in my_dict.items():
        keys.append(key)
        values.append(value)
    return keys, values
my_dict = {"a": 10, "b": 20, "c":25, "d":30}
print(dict_to_lists(my_dict))

# Напишите функцию group_by_first_letter(strings), которая принимает список строк и группирует их в словарь,
# где ключами являются первые символы строк, а значением — список строк, начинающихся с этого символа.
def group_by_first_letter(strings):
    dict = {}
    for string in strings:
        first_letter = string[0]
        if first_letter not in dict:
            dict[first_letter] = []
        dict[first_letter].append(string)
    return dict

strings = ["apple", "watermalon", "cucumber", "garlic", "onion", "oakl"]
print(group_by_first_letter(strings))

# Напишите функцию extract_subdict(my_dict, keys), которая принимает словарь и список ключей.
# Функция должна вернуть новый словарь, включающий только те пары, ключи которых содержатся в списке.
def extract_subdict(my_dict, keys):
    return {key: my_dict[key] for key in keys if key in my_dict}

my_dict = {"a": 10, "b": 20, "c": 30, "d": 40}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))