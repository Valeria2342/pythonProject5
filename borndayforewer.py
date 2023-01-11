year_guess = int(input("В каком году родился А.С. Пушкин? "))

while year_guess != 1799:
    year_guess = int(input("В каком году родился А.С. Пушкин? "))
    if year_guess == 1799:
        day_guess = int(input("В какой день родился А.С. Пушкин? "))
        while day_guess != 6:
            day_guess = int(input("В какой день родился А.С. Пушкин? "))
            if day_guess == 6:
                print('Верно')