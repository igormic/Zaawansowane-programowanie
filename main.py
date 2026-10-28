from classes.house import House
from classes.flat import Flat


if __name__ == "__main__":
    dom = House(area=150.0, rooms=5, price=850000.0, address="Polna 12, Warszawa", plot=600)
    mieszkanie = Flat(area=48.5, rooms=2, price=450000.0, address="Lipowa 3/14, Kraków", floor=3)

    print(dom)
    print(mieszkanie)