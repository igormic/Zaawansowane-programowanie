def listy(lista1: list[int], lista2: list[int]) -> list[int]:

    unikalne = set(lista1 + lista2)

    return [x**3 for x in unikalne]

l1 = [1, 2, 3]
l2 = [2, 3, 4]

wynik = listy(l1, l2)
print(wynik)