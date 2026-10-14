def czy_wieksza(liczba: int, liczba2: int, liczba3: int) -> bool:
    suma = liczba + liczba2

    if suma >= liczba3:
        return True
    else:
        return False

wynik: bool = czy_wieksza(4, 5, 6)