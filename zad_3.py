class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"Dzialka o powierzchni {self.area} z iloscia pokoi o liczbie {self.rooms} w cenie {self.price} o adresie {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        poczatek = super().__str__()
        return f"Dzialka {poczatek}, wielkosc dzialki {self.plot}"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        poczatek = super().__str__()
        return f"Dzialka {poczatek}, ilosc pieter: {self.floor}"

house = House(area=180.5, rooms=6, price=1250000.0, address="Gliwice, ul. Wolnosci", plot=850)
flat = Flat(area=54.2, rooms=2, price=580000.0, address="Wrocław, ul. Wolnosci 2/3", floor=3)

print(house)
print(flat)