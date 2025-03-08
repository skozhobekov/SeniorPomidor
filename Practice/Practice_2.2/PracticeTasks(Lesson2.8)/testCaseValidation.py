def casesQuantityReceive():
        while True:
            try:
                test_cases = int(input("Введите количество тест-кейсов: "))
                if test_cases>=0:
                    break
                print("Ошибка! Введите положительное целое число.")
            except ValueError:
                print("Введите положительное число")
        if test_cases < 10:
            print("попробуйте поработать больше")
        else:
            print("Хорошая работа")
casesQuantityReceive()
