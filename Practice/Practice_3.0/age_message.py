birthdate = int(input("your date of birth: ").strip())

def countAge(birthdate):
    age = 2025 - birthdate
    print(f"your age is {age}")
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    elif age > 18 and age < 65:
        print("Отличный возраст для карьерного роста!")
    elif age > 65:
        print("Пора наслаждаться заслуженным отдыхом!")

countAge(birthdate)