class Pracownik:
    """
    Klasa reprezentuje dane dotyczące pracownika.
    Atrybuty:
        imie (str): Imię pracownika
        nazwisko (str): Nazwisko pracownika
        numer_id (str): Identyfikator pracownika
        staż_pracy (int): Liczba lat pracy
        zarobki (int): Zarobki pracownika
    """
    def __init__(self, imie, nazwisko, numer_id, staż_pracy, zarobki):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.numer_id: str = numer_id
        self.staż_pracy: int = staż_pracy
        self.zarobki: int = zarobki

    """
           Funkcja opisuje podstawowe dane o Pracowniku
           """

    def __repr__(self):
        return (f"Pracownik {self.imie} {self.nazwisko} z nr id: {self.numer_id} "
                f"zarabia {self.zarobki} zł, mając staż pracy {self.staż_pracy} lat.")

pracownicy = [
    Pracownik("Jan", "Nowak", 321, 5, 5500),
    Pracownik("Anna", "Kowalska", 322, 8, 7200),
    Pracownik("Piotr", "Poznański", 323, 3, 4800),
    Pracownik("Maria", "Warszawska", 324, 10, 8000),
    Pracownik("Tomasz", "Krakowski", 325, 2, 4100),
    Pracownik("Izabela", "Wrocławska", 326, 6, 6300)
]

for pracownik in pracownicy:
    print(pracownik)