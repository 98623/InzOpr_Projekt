import unittest
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Testy jednostkowe dla klasy Customer"""

    def test_utworzenie_klienta(self):
        """Test tworzenia nowego klienta"""
        klient = Customer(1, "Jan", "Kowalski", "jan@mail.com", "ABC123")
        self.assertEqual(klient.customer_id, 1)
        self.assertEqual(klient.first_name, "Jan")
        self.assertEqual(klient.last_name, "Kowalski")
        self.assertEqual(klient.email, "jan@mail.com")
        self.assertEqual(klient.license_number, "ABC123")

    def test_get_full_name(self):
        """Test metody get_full_name()"""
        klient = Customer(2, "Anna", "Nowak", "anna@mail.com", "XYZ789")
        self.assertEqual(klient.get_full_name(), "Anna Nowak")

    def validate_email(self) -> bool:
        """
        Sprawdza czy email jest poprawny.

        Returns:
            bool: True jeśli email jest poprawny, False w przeciwnym razie.
        """
        return "@" in self.email and "." in self.email.split("@")[1]


if __name__ == "__main__":
    unittest.main()