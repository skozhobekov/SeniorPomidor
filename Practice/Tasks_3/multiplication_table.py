def multiplication_table():
    for i in range(1,11):
        for digit in range(1,11):
            print(f"{i} * {digit} =", i*digit)

multiplication_table()