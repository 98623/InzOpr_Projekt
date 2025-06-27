class Customer:
    """
    Klasa reprezentująca klienta wypożyczalni samochodów.

    Atrybuty:
        customer_id (int): Unikalny identyfikator klienta.
        first_name (str): Imię klienta.
        last_name (str): Nazwisko klienta.
        email (str): Adres e-mail klienta.
        license_number (str): Numer prawa jazdy klienta.
    """

    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, license_number: str):
        """
        Inicjalizuje nowego klienta z podanymi danymi.

        Args:
            customer_id (int): Unikalny identyfikator klienta.
            first_name (str): Imię klienta.
            last_name (str): Nazwisko klienta.
            email (str): Adres e-mail klienta.
            license_number (str): Numer prawa jazdy klienta.
        """
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.license_number = license_number

    def get_full_name(self) -> str:
        """
        Zwraca pełne imię i nazwisko klienta.

        Returns:
            str: Pełne imię i nazwisko klienta.
        """
        return f"{self.first_name} {self.last_name}"


def validate_email(self):
    """
    Sprawdza czy email jest poprawny.

    Returns:
        bool: True jeśli email jest poprawny, False w przeciwnym razie.
    """
    return "@" in self.email


def __str__(self) -> str:
    """
    Zwraca reprezentację tekstową klienta.

    Returns:
        str: Reprezentacja tekstowa klienta.
    """
    return f"Klient: {self.get_full_name()} (ID: {self.customer_id}, Email: {self.email})"


if __name__ == "__main__":
    klient = Customer(1, "Jan", "Kowalski", "jan.kowalski@gmail.com", "CW123")
    print(klient)
    print(f"Pełne imię: {klient.get_full_name()}")
    print(f"Email poprawny: {klient.validate_email()}")