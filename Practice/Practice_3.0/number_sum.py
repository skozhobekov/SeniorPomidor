number = int(input("Введите ваше число: "))
sum = 0
for number in range(1, number + 1):
    print("ваше число: ", number,  end=" ")
    sum +=number
print(f"Сумма составляет: {sum} ")
