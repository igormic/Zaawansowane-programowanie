from . import utils
from .Product import Product


class Order:
    def __init__(self, products: list[Product]):
        self.products = products

    def get_total(self) -> float:
        return sum(p.price for p in self.products)

    def __str__(self) -> str:
        total = utils.format_price(self.get_total())
        return f"Zamówienie (liczba pozycji: {len(self.products)}), suma: {total}"