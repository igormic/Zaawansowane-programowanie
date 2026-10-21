def lista_imion(lista):

    if len(lista) != 5:
        print("nieprawidlowa ilosc imion")
        return

    for imie in lista:
        print(imie)


imiona = ["Kacper", "Adam", "Anna", "Dominik", "Grzegorz"]
lista_imion(imiona)
