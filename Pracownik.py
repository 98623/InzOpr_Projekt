import unittest

class Pracownik:
    """
    Klasa reprezentuje dane dotyczące pracownika.
    Atrybuty:
        imie (str): Imię pracownika
        nazwisko (str): Nazwisko pracownika
        numer_id (int): Identyfikator pracownika
        staż_pracy (int): Liczba lat pracy
        zarobki (int): Zarobki pracownika
    """
    def __init__(self, imie: str, nazwisko: str, numer_id: int, staż_pracy: int, zarobki: int):
        """
        Inicjalizuje nowego pracownika.
        """
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.numer_id: int = numer_id
        self.staż_pracy: int = staż_pracy
        self.zarobki: int = zarobki

    def __repr__(self):
        """
        Zwraca tekstowy opis pracownika.
        """
        return (f"Pracownik {self.imie} {self.nazwisko} z nr id: {self.numer_id} "
                f"zarabia {self.zarobki} zł, mając staż pracy {self.staż_pracy} lat.")




class TestPracownik(unittest.TestCase):
    """
    Klasa zawierająca testy jednostkowe dla klasy Pracownik.
    """

    def test_utworzenie_pracownika(self):
        """
        Testuje poprawność tworzenia obiektu Pracownik i przypisywania atrybutów.
        """
        p = Pracownik("Adam", "Wielkopolski", 999, 4, 5000)
        self.assertEqual(p.imie, "Adam")
        self.assertEqual(p.nazwisko, "Wielkopolski")
        self.assertEqual(p.numer_id, 999)  # poprawka z 299 -> 999
        self.assertEqual(p.staż_pracy, 4)
        self.assertEqual(p.zarobki, 5000)

    def test_repr_format(self):
        """
        Testuje poprawność działania metody __repr__.
        """
        p = Pracownik("Ewa", "Nowicka", 123, 7, 6700)
        expected = "Pracownik Ewa Nowicka z nr id: 123 zarabia 6700 zł, mając staż pracy 7 lat."
        self.assertEqual(repr(p), expected)

    def test_typy_atrybutow(self):
        """
        Testuje typy danych przypisane do atrybutów obiektu Pracownik.
        """
        p = Pracownik("Eryk", "Mazowiecki", 200, 3, 4200)
        self.assertIsInstance(p.imie, str)
        self.assertIsInstance(p.nazwisko, str)
        self.assertIsInstance(p.numer_id, int)
        self.assertIsInstance(p.staż_pracy, int)
        self.assertIsInstance(p.zarobki, int)


if __name__ == "__main__":
    unittest.main()