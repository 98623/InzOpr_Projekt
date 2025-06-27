import unittest
from wypozyczalnia import Wypozyczalnia
from customer import Customer
from samochod import Samochod, RodzajPaliwa
from wypozyczenie import Wypozyczenie


class TestIntegracjaKoszty(unittest.TestCase):
    """Test integracyjny - obliczanie kosztów"""
    
    def test_obliczanie_kosztow(self):
        """Test prostego obliczania kosztów wypożyczeń"""
        
        # Stwórz wypożyczalnię
        wypozyczalnia = Wypozyczalnia("CostTest")
        
        # Doda 2 samochody
        auto1 = Samochod("Toyota", "Corolla", 2020, "KR001", 100.0)
        auto2 = Samochod("BMW", "X3", 2019, "KR002", 200.0)
        
        wypozyczalnia.dodaj_samochod(auto1)
        wypozyczalnia.dodaj_samochod(auto2)
        
        # Dodaj 2 klientów
        klient1 = Customer(1, "Jan", "Kowalski", "jan@mail.com", "ABC123")
        klient2 = Customer(2, "Anna", "Nowak", "anna@mail.com", "XYZ789")
        
        wypozyczalnia.dodaj_klienta(klient1)
        wypozyczalnia.dodaj_klienta(klient2)
        
        # Wypożycz oba samochody
        numer1 = wypozyczalnia.wypozycz_samochod(1, "KR001", 5)  # 5 dni * 100 = 500 zł
        numer2 = wypozyczalnia.wypozycz_samochod(2, "KR002", 3)  # 3 dni * 200 = 600 zł
        
        # Sprawdź że wypożyczenia się udały
        self.assertEqual(numer1, "W001")
        self.assertEqual(numer2, "W002")
        
        # Sprawdź koszty wypożyczeń
        wypozyczenia = wypozyczalnia.get_aktywne_wypozyczenia()
        self.assertEqual(len(wypozyczenia), 2)
        
        # Znajdź konkretne wypożyczenia i sprawdź koszty
        w1 = next(w for w in wypozyczenia if w.numer_wypozyczenia == "W001")
        w2 = next(w for w in wypozyczenia if w.numer_wypozyczenia == "W002")
        
        self.assertEqual(w1.koszt_calkowity, 500.0)
        self.assertEqual(w2.koszt_calkowity, 600.0)
        
        # Oblicz całkowity przychód
        calkowity_przychod = w1.koszt_calkowity + w2.koszt_calkowity
        self.assertEqual(calkowity_przychod, 1100.0)
        
        # Zwróć jeden samochód
        wypozyczalnia.zwroc_samochod("W001")
        
        # Sprawdź że zostało tylko jedno aktywne wypożyczenie
        aktywne = wypozyczalnia.get_aktywne_wypozyczenia()
        self.assertEqual(len(aktywne), 1)
        self.assertEqual(aktywne[0].koszt_calkowity, 600.0)


if __name__ == "__main__":
    unittest.main()