# Анаграмма
def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):

        return print("Yes it is")
    else:
        print("it is not anagrams")

s1 = str(input("input first word: "))
s2 = str(input("input second word: "))
is_anagram(s1,s2)

# Палиндром
def isPalindrom(string):
    string1 = string[::-1]
    if string1 == string:
        return print("Yes it is Palindrom")
    else:
        print("it is NOT")
string = str(input("input your string: "))
isPalindrom(string)

# Самое длинное слово
stroke = "In the middle of a vast desert, an extraordinary adventure awaits"
def longest_word(s):
    newStroke = stroke.split()
    longest = ""
    for word in newStroke:
        if len(word) > len(longest):
           longest = word
    print(longest)
longest_word(stroke)

# Напишите функцию format_phone_number(digits), которая принимает строку из 10 цифр и возвращает её в формате (XXX) XXX-XXXX.
numbers = str(input("input phone number: "))
def format_phone_number(numbers):
    if len(numbers) != 9 or not numbers.isdigit():
        return print("Error")
    return print(f"({numbers[:3]})-{numbers[3:6]}-{numbers[6:]}")
format_phone_number(numbers)

# Напишите функцию remove_duplicates(s), которая принимает строку и возвращает новую строку,
# из которой удалены все повторяющиеся символы, оставляя только первое вхождение каждого символа.
s3 = str(input("input string: "))

def remove_duplicates(s3):
    result = ""
    for i in s3:
        if i not in result:
            result += i
    return print(result)
remove_duplicates(s3)

s4 = str(input("input String: "))
def isUnique(s4):
    return len(s4)== len(set(s4))
if isUnique(s4):
    print("YES")
else:
    print("NO")

isUnique(s4)
