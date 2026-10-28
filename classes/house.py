from .property import Property

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        poczatek = super().__str__()
        return f"Dzialka {poczatek}, wielkosc dzialki {self.plot}"