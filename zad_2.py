def lista_mnozona_for(lista):
    wynik = []
    for liczba in lista:
        wynik.append(liczba * 2)
    return wynik

def lista_mnozona_druga(lista):
    return [liczba * 2 for liczba in lista]

liczby = [2, 3, 4, 5, 6]
lista_mnozona_for(liczby)
lista_mnozona_druga(liczby)