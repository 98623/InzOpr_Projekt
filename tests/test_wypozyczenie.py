import unittest
from wypozyczenie import Wypozyczenie


class TestWypozyczenie(unittest.TestCase):
    """Testy jednostkowe dla klasy Wypozyczenie"""
    
    def test_utworzenie_wypozyczenia(self):
        """Test tworzenia nowego wypożyczenia"""
        wypozyczenie = Wypozyczenie("W001", 1, "KR12345", 7, 150.0)
        self.assertEqual(wypozyczenie.numer_wypozyczenia, "W001")
        self.assertEqual(wypozyczenie.customer_id, 1)
        self.assertEqual(wypozyczenie.numer_rejestracyjny, "KR12345")
        self.assertEqual(wypozyczenie.dni_wypozyczenia, 7)
        self.assertEqual(wypozyczenie.koszt_calkowity, 1050.0)
        self.assertFalse(wypozyczenie.zwrocony)
    
    def test_oznacz_jako_zwrocony(self):
        """Test oznaczania wypożyczenia jako zwrócone"""
        wypozyczenie = Wypozyczenie("W002", 2, "KR67890", 5, 200.0)
        self.assertFalse(wypozyczenie.zwrocony)
        wypozyczenie.oznacz_jako_zwrocony()
        self.assertTrue(wypozyczenie.zwrocony)
    
    def test_czy_aktywne(self):
        """Test sprawdzania czy wypożyczenie jest aktywne"""
        wypozyczenie = Wypozyczenie("W003", 3, "KR11111", 3, 180.0)
        self.assertTrue(wypozyczenie.czy_aktywne())
        
        wypozyczenie.oznacz_jako_zwrocony()
        self.assertFalse(wypozyczenie.czy_aktywne())


if __name__ == "__main__":
    unittest.main()