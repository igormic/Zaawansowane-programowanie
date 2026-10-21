class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"Biblioteka w miejscowosci {self.city} na ulicy {self.street} z kodem pocztowym {self.zip_code} otwarta w godzinach {self.open_hours} z telefonem {self.phone}"


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"Pracownik o imieniu {self.first_name} i nazwisku {self.last_name} ztrudniony w dniu {self.hire_date}, pochodzacy z miasta {self.city}, mieszkajacy na ulicy {self.street} z kodem pocztowym {self.zip_code} i numerem telefonu {self.phone}"


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: str,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Ksiazka z biblioteki {self.library} z data publikacji {self.publication_date} autorstwa {self.author_name} {self.author_surname} z iloscia stron {self.number_of_pages}"


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: list[Book], order_date
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f"Zamowienie wykonane przez pracownika {self.employee} dla studenta {self.student} z ksiazkami {self.books} z data zamowienia {self.order_date}"


class Student:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


lib1 = Library("Kraków", "Bogucicka 1", "31-124", "08:00 - 19:00", "12 617 52 00")
lib2 = Library("Warszawa", "Wolnosci 1", "00-950", "09:00 - 20:00", "22 537 41 40")

b1 = Book(lib1, "1954", "J.R.R.", "Tolkien", 423)
b2 = Book(lib1, "1943", "Antoine", "de Saint-Exupéry", 96)
b3 = Book(lib2, "1949", "George", "Orwell", 328)
b4 = Book(lib2, "1866", "Fiodor", "Dostojewski", 671)
b5 = Book(lib2, "1997", "J.K.", "Rowling", 223)

emp1 = Employee(
    "Jan",
    "Kowalski",
    "2020-03-01",
    "1985-05-12",
    "Kraków",
    "Wolnosci 1",
    "31-019",
    "501-111-222",
)
emp2 = Employee(
    "Ewa",
    "Zielińska",
    "2018-09-15",
    "1990-11-23",
    "Warszawa",
    "Wolnosci 1",
    "00-628",
    "502-333-444",
)
emp3 = Employee(
    "Piotr",
    "Wiśniewski",
    "2022-01-10",
    "1995-07-08",
    "Kraków",
    "Wolnosci 1",
    "31-006",
    "503-555-666",
)

s1 = Student("Michał Dominik", [55, 60, 70])
s2 = Student("Karolina Maj", [40, 45, 50])
s3 = Student("Paweł Lis", [80, 85, 90])

order1 = Order(emp1, s1, [b1, b2], "2026-03-10")
order2 = Order(emp2, s3, [b3, b4, b5], "2026-03-11")

print(order1)
print("\n" + "=" * 50 + "\n")
print(order2)
print("\n")