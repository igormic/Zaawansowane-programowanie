from .property import Property

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        poczatek = super().__str__()
        return f"Dzialka {poczatek}, ilosc pieter: {self.floor}"