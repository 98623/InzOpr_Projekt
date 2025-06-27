from datetime import datetime, timedelta

class Wypozyczenie:
    """
    Klasa reprezentująca wypożyczenie samochodu.
    
    Atrybuty:
        numer_wypozyczenia (str): Unikalny numer wypożyczenia
        customer_id (int): ID klienta
        numer_rejestracyjny (str): Numer rejestracyjny samochodu
        data_wypozyczenia (datetime): Data rozpoczęcia wypożyczenia
        data_zwrotu (datetime): Planowana data zwrotu
        koszt_calkowity (float): Całkowity koszt wypożyczenia
        zwrocony (bool): Czy samochód został zwrócony
    """
    
    def __init__(self, numer_wypozyczenia: str, customer_id: int, numer_rejestracyjny: str, 
                 dni_wypozyczenia: int, koszt_dzienny: float) -> None:
        """
        Inicjalizuje nowe wypożyczenie.
        
        Args:
            numer_wypozyczenia (str): Unikalny numer wypożyczenia
            customer_id (int): ID klienta
            numer_rejestracyjny (str): Numer rejestracyjny samochodu
            dni_wypozyczenia (int): Liczba dni wypożyczenia
            koszt_dzienny (float): Koszt dzienny wypożyczenia
        """
        self.numer_wypozyczenia = numer_wypozyczenia
        self.customer_id = customer_id
        self.numer_rejestracyjny = numer_rejestracyjny
        self.data_wypozyczenia = datetime.now()
        self.data_zwrotu = self.data_wypozyczenia + timedelta(days=dni_wypozyczenia)
        self.koszt_calkowity = koszt_dzienny * dni_wypozyczenia
        self.zwrocony = False
        self.dni_wypozyczenia = dni_wypozyczenia

    def oznacz_jako_zwrocony(self):
        """
        Oznacza wypożyczenie jako zwrócone.
        """
        self.zwrocony = True

    def oblicz_opoznienie(self):
        """
        Oblicza liczbę dni opóźnienia w zwrocie.
        
        Returns:
            int: Liczba dni opóźnienia (0 jeśli nie ma opóźnienia)
        """
        if not self.zwrocony:
            dzisiaj = datetime.now()
            if dzisiaj > self.data_zwrotu:
                opoznienie = dzisiaj - self.data_zwrotu
                return opoznienie.days
        return 0

    def oblicz_kare_za_opoznienie(self, kara_dzienna=50.0):
        """
        Oblicza karę za opóźnienie w zwrocie.
        
        Args:
            kara_dzienna (float): Kara za jeden dzień opóźnienia
            
        Returns:
            float: Wysokość kary
        """
        dni_opoznienia = self.oblicz_opoznienie()
        return dni_opoznienia * kara_dzienna

    def czy_aktywne(self) -> bool:
        """
        Sprawdza czy wypożyczenie jest aktywne.
        
        Returns:
            bool: True jeśli wypożyczenie jest aktywne
        """
        return not self.zwrocony

    def get_info(self):
        """
        Zwraca informacje o wypożyczeniu.
        
        Returns:
            str: Informacje o wypożyczeniu
        """
        status = "Zwrócony" if self.zwrocony else "Aktywny"
        return (f"Wypożyczenie {self.numer_wypozyczenia}: "
                f"Klient ID: {self.customer_id}, "
                f"Samochód: {self.numer_rejestracyjny}, "
                f"Data wypożyczenia: {self.data_wypozyczenia.strftime('%Y-%m-%d')}, "
                f"Data zwrotu: {self.data_zwrotu.strftime('%Y-%m-%d')}, "
                f"Koszt: {self.koszt_calkowity} zł, "
                f"Status: {status}")

    def __str__(self) -> str:
        """
        Zwraca reprezentację tekstową wypożyczenia.
        
        Returns:
            str: Reprezentacja tekstowa wypożyczenia
        """
        return f"Wypożyczenie {self.numer_wypozyczenia} - Klient: {self.customer_id}, Auto: {self.numer_rejestracyjny}"


if __name__ == "__main__":
    wypozyczenie = Wypozyczenie("W001", 1, "KR12345", 7, 150.0)
    print(wypozyczenie.get_info())
    print(f"Czy aktywne: {wypozyczenie.czy_aktywne()}")
    print(f"Opóźnienie: {wypozyczenie.oblicz_opoznienie()} dni")
    print(f"Kara: {wypozyczenie.oblicz_kare_za_opoznienie()} zł")