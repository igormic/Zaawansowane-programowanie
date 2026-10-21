def parzyste(lista):

    if len(lista) != 10:
        print("nieprawidlowa liczba")
        return

    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)


liczby = list(range(1, 11))

parzyste(liczby)
