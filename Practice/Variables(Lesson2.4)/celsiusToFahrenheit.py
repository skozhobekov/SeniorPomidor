def converter(farenheit):
    celsius = (farenheit-32)*5/9
    return round(celsius,2)

farenheit = float(input("Введите кол-во градусов по Фаренгейту: "))
celsius = converter(farenheit)
print(farenheit, "градусов по фаренгейту равны: ", celsius, " градусов по цельсию")




# f= int(input("Введите кол-во градусов по Фаренгейту"))
#
# c = (f-32)*5/9
#
# print(f, " градусов по фаренгейту будет равно: ", round(c,3))
#
