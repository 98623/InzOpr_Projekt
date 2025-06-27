import unittest
from samochod import Samochod, StatusSamochodu, RodzajPaliwa


class TestSamochod(unittest.TestCase):
    """Testy jednostkowe dla klasy Samochood"""
    
    def test_utworzenie_samochodu(self):
        """Test tworzenia nowego samochoduu"""
        auto = Samochod("Toyota", "Corolla", 2020, "KR12345", 150.0, 25000, RodzajPaliwa.BENZYNA)
        self.assertEqual(auto.marka, "Toyota")
        self.assertEqual(auto.model, "Corolla")
        self.assertEqual(auto.rok_produkcji, 2020)
        self.assertEqual(auto.numer_rejestracyjny, "KR12345")
        self.assertEqual(auto.dzienna_rata_wypozyczenia, 150.0)
        self.assertEqual(auto.status, StatusSamochodu.DOSTEPNY)
        self.assertEqual(auto.rodzaj_paliwa, RodzajPaliwa.BENZYNA)
    
    def test_oblicz_koszt_wypozyczenia(self):
        """Test obliczania kosztu wypożyczenia"""
        auto = Samochod("BMW", "X3", 2019, "KR67890", 200.0)
        self.assertEqual(auto.oblicz_koszt_wypozyczenia(5), 1000.0)
        self.assertEqual(auto.oblicz_koszt_wypozyczenia(0), 0.0)  
        self.assertEqual(auto.oblicz_koszt_wypozyczenia(3), 600.0)
    
    def test_oznacz_jako_wypozyczony(self):
        """Test oznaczania samochodu jako wypożyczony"""
        auto = Samochod("Audi", "A4", 2021, "KR11111", 180.0)
        result = auto.oznacz_jako_wypozyczony("W001")
        self.assertTrue(result)
        self.assertEqual(auto.status, StatusSamochodu.WYPOZYCZONY)
        self.assertEqual(auto.aktualny_numer_wypozyczenia, "W001")
        
        # Test próby wypożyczenia już wypożyczonego samochodu
        result2 = auto.oznacz_jako_wypozyczony("W002")
        self.assertFalse(result2)


if __name__ == "__main__":
    unittest.main()