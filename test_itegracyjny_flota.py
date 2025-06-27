import unittest
from wypozyczalnia import Wypozyczalnia
from customer import Customer
from samochod import Samochod, StatusSamochodu, RodzajPaliwa
from pracownik import Pracownik


class TestIntegracjaFlota(unittest.TestCase):
    """Test integracyjnyy - zarządzanie flotą"""
    
    def test_zarządzanie_flota(self):
        """Test prostego zarządzania flotą samochodów"""
        
        # Stwórz wypożyczalnię
        wypozyczalnia = Wypozyczalnia("FleetTest")
        
        # Dodaj 3 samochody
        auto1 = Samochod("Toyota", "Corolla", 2020, "KR001", 150.0)
        auto2 = Samochod("BMW", "X3", 2019, "KR002", 300.0)
        auto3 = Samochod("Audi", "A4", 2021, "KR003", 250.0)
        
        wypozyczalnia.dodaj_samochod(auto1)
        wypozyczalnia.dodaj_samochod(auto2)
        wypozyczalnia.dodaj_samochod(auto3)
        
        # Sprawdź że wszystkie są dostępne
        self.assertEqual(len(wypozyczalnia.get_dostepne_samochody()), 3)
        
        # Jeden samochód idzie do naprawy
        auto2.oznacz_jako_w_naprawie()
        self.assertEqual(len(wypozyczalnia.get_dostepne_samochody()), 2)
        
        # Pracownik kończy naprawę
        pracownik = Pracownik("Anna", "Mechanik", 100, 5, 4000)
        auto2.oznacz_jako_dostepny()
        
        # Sprawdź że znów wszystkie są dostępne
        self.assertEqual(len(wypozyczalnia.get_dostepne_samochody()), 3)
        
        # Test kosztów różnych aut
        koszt1 = auto1.oblicz_koszt_wypozyczenia(5)  # Toyota
        koszt2 = auto2.oblicz_koszt_wypozyczenia(5)  # BMW
        koszt3 = auto3.oblicz_koszt_wypozyczenia(5)  # Audi
        
        self.assertEqual(koszt1, 750.0)   # 150 * 5
        self.assertEqual(koszt2, 1500.0)  # 300 * 5
        self.assertEqual(koszt3, 1250.0)  # 250 * 5


if __name__ == "__main__":
    unittest.main()