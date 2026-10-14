from typing import Optional
import requests


class Brewery:

    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: Optional[str] = None,
        address_2: Optional[str] = None,
        address_3: Optional[str] = None,
        city: Optional[str] = None,
        state_province: Optional[str] = None,
        postal_code: Optional[str] = None,
        country: Optional[str] = None,
        longitude: Optional[str] = None,
        latitude: Optional[str] = None,
        phone: Optional[str] = None,
        website_url: Optional[str] = None,
        state: Optional[str] = None,
        street: Optional[str] = None,
    ) -> None:
        self.id: str = id
        self.name: str = name
        self.brewery_type: str = brewery_type
        self.address_1: Optional[str] = address_1
        self.address_2: Optional[str] = address_2
        self.address_3: Optional[str] = address_3
        self.city: Optional[str] = city
        self.state_province: Optional[str] = state_province
        self.postal_code: Optional[str] = postal_code
        self.country: Optional[str] = country
        self.longitude: Optional[str] = longitude
        self.latitude: Optional[str] = latitude
        self.phone: Optional[str] = phone
        self.website_url: Optional[str] = website_url
        self.state: Optional[str] = state
        self.street: Optional[str] = street

    def __str__(self) -> str:
        return (
            f"Browar: {self.name} (Typ: {self.brewery_type})\n"
            f"  Lokalizacja: {self.city or 'Brak miasta'}, {self.country or 'Brak kraju'}\n"
            f"  Strona WWW: {self.website_url or 'Brak'}\n"
        )


def pobierz_browary(limit: int = 20) -> list[Brewery]:
    url = f"https://api.openbrewerydb.org/v1/breweries?per_page={limit}"
    odpowiedz = requests.get(url)
    odpowiedz.raise_for_status()

    dane_json: list[dict] = odpowiedz.json()

    # Tworzymy instancję klasy Brewery dla każdego słownika z JSON-a
    lista_browarow: list[Brewery] = [
        Brewery(**dane_browaru) for dane_browaru in dane_json
    ]
    return lista_browarow


if __name__ == "__main__":
    browary: list[Brewery] = pobierz_browary(20)

    for browar in browary:
        print(browar)