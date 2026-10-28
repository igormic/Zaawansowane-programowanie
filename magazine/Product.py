from . import utils


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Produkt: {self.name}, Cena: {utils.format_price(self.price)}"