import unittest
from wypozyczalnia import Wypozyczalnia
from customer import Customer
from samochod import Samochod, StatusSamochodu, RodzajPaliwa


class TestIntegracjaWypozyczenie(unittest.TestCase):
    """Test integracyjny - prosty proces wypożyczenia"""
    
    def test_podstawowy_proces_wypozyczenia(self):
        """Test podstawowego wypożyczenia i zwrotu samochodu"""
        
        # Stwórz wypożyczalnię
        wypozyczalnia = Wypozyczalnia("TestRent")
        
        # Dodaj samochód i klienta
        auto = Samochod("Toyota", "Corolla", 2020, "KR123", 150.0)
        klient = Customer(1, "Jan", "Kowalski", "jan@mail.com", "ABC123")
        
        wypozyczalnia.dodaj_samochod(auto)
        wypozyczalnia.dodaj_klienta(klient)
        
        # Sprawdź początkowy stan
        self.assertEqual(len(wypozyczalnia.get_dostepne_samochody()), 1)
        self.assertTrue(auto.czy_dostepny())
        
        # Wypożycz samochód
        numer = wypozyczalnia.wypozycz_samochod(1, "KR123", 5)
        self.assertEqual(numer, "W001")
        
        # Sprawdź stan po wypożyczeniu
        self.assertEqual(len(wypozyczalnia.get_dostepne_samochody()), 0)
        self.assertEqual(auto.status, StatusSamochodu.WYPOZYCZONY)
        
        # Zwróć samochód
        zwrot = wypozyczalnia.zwroc_samochod("W001")
        self.assertTrue(zwrot)
        
        # Sprawdź stan po zwrocie
        self.assertEqual(len(wypozyczalnia.get_dostepne_samochody()), 1)
        self.assertTrue(auto.czy_dostepny())


if __name__ == "__main__":
    unittest.main()