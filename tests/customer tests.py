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

    def test_validate_email(self):
        """Test walidacji email"""
        klient1 = Customer(3, "Test", "User", "test@example.com", "DEF456")
        klient2 = Customer(4, "Bad", "Email", "bademail", "GHI789")
        self.assertTrue(klient1.validate_email())
        self.assertFalse(klient2.validate_email())


if __name__ == "__main__":
    unittest.main()