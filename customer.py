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



if __name__ == "__main__":
    c = Customer(1, "Jan", "Kowalski", "jan.kowalski@mail.com", "ABC12345")
    print("Id klienta:", c.customer_id)
    print("Imię klienta:", c.first_name)
    print("Nazwisko klienta:", c.last_name)
    print("Email klienta:", c.email)
    print("Numer prawa jazdy:", c.license_number)
