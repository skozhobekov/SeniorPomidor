sum = float(input("Введите сумму покупки: "))
discount = int(input("Введите сумму скидки в процентах: "))
total_sum =  sum * ((100 - discount) * 0.01)
economiedSum = sum - total_sum
print("Сумма с учетом скидки равна: ", round(total_sum,2))
print("Вы сэкономите ", round(economiedSum,2))
