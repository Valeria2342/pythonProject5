year_guess = int(input("В каком году родился А.С. Пушкин? "))

if year_guess == 1799:
    day_guess = int(input("В какой день родился А.С. Пушкин? "))
    if day_guess == 6:
        print("Вы ответили верно!")
    else:
        print("Неверный день рождения")
else:
    print('Вы ответили неверно!')