from enum import Enum

class StatusSamochodu(Enum):
    DOSTEPNY = "Dostępny"
    WYPOZYCZONY = "Wypożyczony"
    NIEDOSTEPNY = "Niedostępny"
    W_NAPRAWIE = "W naprawie"

class RodzajPaliwa(Enum):
    BENZYNA = "Benzyna"
    DIESEL = "Diesel"
    ELEKTRYCZNY = "Elektryczny"
    HYBRYDOWY = "Hybrydowy"

class Samochod:
    def __init__(self, marka, model, rok_produkcji, numer_rejestracyjny, dzienna_rata_wypozyczenia, przebieg = 0, rodzaj_paliwa=RodzajPaliwa.BENZYNA):
        """
        Inicjalizacja obiektu Samochod dla wypożyczalni samochodów

        Argumentyy:
            marka (str): Marka samochodu (np. "Toyota")
            model (str): Model samochodu (np. "Corolla")
            rok_produkcji (int): Rok produkcji samochodu (np. 2020)
            numer_rejestracyjny (str): Numer rejestracyjny samochodu
            dzienna_rata_wypozyczenia (float): Dzienna rata wypożyczenia samochodu w złotówkach
            przebieg (int): Przebieg samochodu w kilometrach (domyślnie 0)
            rodzaj_paliwa (RodzajPaliwa): Rodzaj paliwa samochodu (domyślnie BENZYNA)
        """
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.numer_rejestracyjny = numer_rejestracyjny
        self.dzienna_rata_wypozyczenia = dzienna_rata_wypozyczenia
        self.przebieg = przebieg
        self.status = StatusSamochodu.DOSTEPNY
        self.rodzaj_paliwa = rodzaj_paliwa
        self.aktualny_numer_wypozyczenia = None

    def oznacz_jako_wypozyczony(self, numer_wypozyczenia) -> bool:
        """
        Oznacza samochód jako wypożyczony

        Argumenty:
            numer_wypozyczenia (str): Unikalny numer wypożyczenia

        Zwraca:
            bool: True jeżeli pomyślnie oznaczono samochód jako wypożyczony, False w przeciwnym razie
        """
            
        if self.status == StatusSamochodu.DOSTEPNY:
            self.status = StatusSamochodu.WYPOZYCZONY
            self.aktualny_numer_wypozyczenia = numer_wypozyczenia
            return True
        return False
    
    def oznacz_jako_dostepny(self) -> bool:
        """
        Oznacza samochód jako dostępny

        Zwraca:
            bool: True jeżeli pomyślnie oznaczono samochód jako dostępny
        """
        self.status = StatusSamochodu.DOSTEPNY
        self.aktualny_numer_wypozyczenia = None
        return True

    def oznacz_jako_w_naprawie(self) -> bool:
        """
        Oznacza samochód jako w naprawie

        Zwraca:
            bool: True jeżeli pomyślnie oznaczono samochód jako w naprawie
        """
        self.status = StatusSamochodu.W_NAPRAWIE
        self.aktualny_numer_wypozyczenia = None
        return True

    def oblicz_koszt_wypozyczenia(self, dni) -> float:
        """
        Oblicza koszt wypożyczenia samochodu na określoną liczbę dni

        Argumenty:
            dni (int): Liczba dni wypożyczenia

        Zwraca:
            float: Całkowity koszt wypożyczenia
        """
        return round(self.dzienna_rata_wypozyczenia * dni, 2)
    
    def czy_dostepny(self) -> bool:
        """
        Sprawdza, czy samochód jest dostępny do wypożyczenia

        Zwraca:
            bool: True, jeśli samochód jest dostępny, False w przeciwnym razie
        """
        return self.status == StatusSamochodu.DOSTEPNY
    
    def zaktualizuj_przebieg(self, nowy_przebieg) -> None:
        """
        Aktualizuje przebieg samochodu

        Argumenty:
            nowy_przebieg (int): Nowy przebieg samochodu w kilometrach
        """
        if nowy_przebieg < self.przebieg:
            raise ValueError("Nowy przebieg nie może być mniejszy niż aktualny przebieg.")
        self.przebieg = nowy_przebieg

    def opis(self) -> str:
        """
        Zwraca opis samochodu

        Zwraca:
            str: Opis samochodu
        """
        return (f"Samochód: {self.marka} {self.model}, "
                f"Rok produkcji: {self.rok_produkcji}, "
                f"Numer rejestracyjny: {self.numer_rejestracyjny}, "
                f"Przebieg: {self.przebieg} km, "
                f"Rodzaj paliwa: {self.rodzaj_paliwa.value}, "
                f"Status: {self.status.value}, "
                f"Dzienna rata wypożyczenia: {self.dzienna_rata_wypozyczenia} zł")
    
    def __str__(self) -> str:
        """
        Zwraca reprezentację tekstową obiektu Samochod

        Returns:
            str: Reprezentacja tekstowa obiektu Samochod
        """
        return (f"{self.marka} {self.model} ({self.rok_produkcji}) - {self.numer_rejestracyjny}, "
                f"Status: {self.status.value} - Dzienna rata: {self.dzienna_rata_wypozyczenia} zł")


if __name__ == "__main__":
    auto = Samochod("Toyota", "Corolla", 2020, "KR135", 150.0, 25000, RodzajPaliwa.BENZYNA)
    print(auto)
    print(f"Koszt wypożyczenia na 5 dni: {auto.oblicz_koszt_wypozyczenia(5)} zł")
