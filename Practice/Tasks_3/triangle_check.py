a = int(input("введите первое число: "))
b = int(input("введите второе число: "))
c = int(input("введите третье число: "))



def check_triangle(a, b, c):
    # Проверяем условие существования треугольника
    if a + b > c and a + c > b and b + c > a:

        if a == b == c:
            return print("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            return print("Треугольник равнобедренный")
        else:
            return print("Треугольник разносторонний")
    else:
        return print("Треугольник построить нельзя")

check_triangle(a,b,c)