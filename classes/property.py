class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"Dzialka o powierzchni {self.area} z iloscia pokoi o liczbie {self.rooms} w cenie {self.price} o adresie {self.address}"