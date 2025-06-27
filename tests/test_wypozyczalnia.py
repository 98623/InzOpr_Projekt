import unittest
from wypozyczalnia import Wypozyczalnia
from customer import Customer
from samochod import Samochod, RodzajPaliwa


class TestWypozyczalnia(unittest.TestCase):
    """Testy jednostkowe dla klasy Wypozyczalnia"""
    
    def test_utworzenie_wypozyczalni(self):
        """Test tworzenia nowej wypożyczalni"""
        wypozyczalnia = Wypozyczalnia("AutoRent")
        self.assertEqual(wypozyczalnia.nazwa, "AutoRent")
        self.assertEqual(len(wypozyczalnia.samochody), 0)
        self.assertEqual(len(wypozyczalnia.klienci), 0)
        self.assertEqual(len(wypozyczalnia.wypozyczenia), 0)
        self.assertEqual(wypozyczalnia.nastepny_numer_wypozyczenia, 1)
    
    def test_dodaj_samochod_i_klienta(self):
        """Test dodawania samochodu i klienta"""
        wypozyczalnia = Wypozyczalnia("TestRent")
        auto = Samochod("Toyota", "Corolla", 2020, "KR12345", 150.0)
        klient = Customer(1, "Jan", "Kowalski", "jan@mail.com", "ABC123")
        
        wypozyczalnia.dodaj_samochod(auto)
        wypozyczalnia.dodaj_klienta(klient)
        
        self.assertEqual(len(wypozyczalnia.samochody), 1)
        self.assertEqual(len(wypozyczalnia.klienci), 1)
        self.assertIn(auto, wypozyczalnia.samochody)
        self.assertIn(klient, wypozyczalnia.klienci)
    
    def test_znajdz_klienta_i_samochod(self):
        """Test znajdowania klienta i samochodu"""
        wypozyczalnia = Wypozyczalnia("FindTest")
        auto = Samochod("BMW", "X3", 2019, "KR67890", 200.0)
        klient = Customer(5, "Anna", "Nowak", "anna@mail.com", "XYZ789")
        
        wypozyczalnia.dodaj_samochod(auto)
        wypozyczalnia.dodaj_klienta(klient)
        
        # Test znajdowania istniejących obiektów
        znaleziony_klient = wypozyczalnia.znajdz_klienta(5)
        znaleziony_auto = wypozyczalnia.znajdz_samochod("KR67890")
        
        self.assertIsNotNone(znaleziony_klient)
        self.assertIsNotNone(znaleziony_auto)
        self.assertEqual(znaleziony_klient.first_name, "Anna")
        self.assertEqual(znaleziony_auto.marka, "BMW")
        
        # Test nie znajdowania nieistniejących obiektów
        nieistniejacy_klient = wypozyczalnia.znajdz_klienta(999)
        nieistniejacy_auto = wypozyczalnia.znajdz_samochod("NIEISTNIEJE")
        
        self.assertIsNone(nieistniejacy_klient)
        self.assertIsNone(nieistniejacy_auto)


if __name__ == "__main__":
    unittest.main()