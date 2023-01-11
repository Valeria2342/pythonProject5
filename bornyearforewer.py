year_guess = int(input("В каком году родился А.С. Пушкин? "))

while year_guess != 1799:
    year_guess = int(input("В каком году родился А.С. Пушкин? "))
    if year_guess == 1799:
        print('Верно')