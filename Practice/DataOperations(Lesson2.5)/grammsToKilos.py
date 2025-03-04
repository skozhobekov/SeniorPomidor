def grammsToKillos(gramm):
    kilo = gramm/1000
    return round(kilo,1)

try:
    gramm = int(input("Введите количество грамм: "))
    if gramm <=0:
        raise ValueError("Введите положительное число!")
except ValueError as e:
    print(e)

else:
    kilo = grammsToKillos(gramm)
    print(gramm, "грамм это -", kilo, "килограмм")


