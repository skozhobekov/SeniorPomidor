# def rectangle_area(a,b):
#     s = a * b
#     return print(f"Площадь прямоугольника с длиной {a} и шириной {b} равна {s}")
#
# rectangle_area(3,5)
#
# def convert_seconds(seconds):
#     hours = seconds //360
#     minutes = (seconds % 3600) // 60  # Оставшиеся минуты
#     return hours, minutes
#
# seconds = int(input("Введите количество секунд: "))
# hours, minutes = convert_seconds(seconds)
# print(f"В {seconds} секундах содержится {hours} часов и {minutes} минут.")
#
# def power_of(number, exponent):
#     s = number ** exponent
#     return print(f"число {number} в степени {exponent} будет равна {s}")
#
# power_of(3,2)

# def count_items(*args):
#     quantity = 0
#     for i in args:
#         quantity +=1
#     print(f"quantity is: {quantity}")
#
# args = (1,2,3,4,5,6,4,4,4,4)
# count_items(*args)