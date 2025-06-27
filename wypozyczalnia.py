from typing import List, Optional
from customer import Customer
from samochod import Samochod
from wypozyczenie import Wypozyczenie

class Wypozyczalnia:
    """
    Klasa reprezentująca wypożyczalnię samochodów.
    
    Atrybuty:
        nazwa (str): Nazwa wypożyczalni
        samochody (List[Samochod]): Lista samochodów
        klienci (List[Customer]): Lista klientów
        wypozyczenia (List[Wypozyczenie]): Lista wypożyczeń
    """
    
    def __init__(self, nazwa: str) -> None:
        """
        Inicjalizuje wypożyczalnię.
        
        Args:
            nazwa (str): Nazwa wypożyczalni
        """
        self.nazwa = nazwa
        self.samochody: List[Samochod] = []
        self.klienci: List[Customer] = []
        self.wypozyczenia: List[Wypozyczenie] = []
        self.nastepny_numer_wypozyczenia = 1

    def dodaj_samochod(self, samochod: Samochod) -> None:
        """
        Dodaje samochód.
        
        Args:
            samochod (Samochod): Samochód do dodania
        """
        self.samochody.append(samochod)

    def dodaj_klienta(self, klient: Customer) -> None:
        """
        Dodaje klienta do bazy.
        
        Args:
            klient (Customer): Klient do dodania
        """
        self.klienci.append(klient)

    def znajdz_klienta(self, customer_id: int) -> Optional[Customer]:  # ZMIENIONE: Dodany Optional
        """
        Znajduje klienta po ID.

        Args:
            customer_id (int): ID klienta

        Returns:
            Optional[Customer]: Klient o podanym ID lub None jeśli nie znaleziono
        """
        for klient in self.klienci:
            if klient.customer_id == customer_id:
                return klient
        return None

        # Oznacza samochód jako wypożyczony
        samochod.oznacz_jako_wypozyczony(numer_wypozyczenia)  # ZMIENIONE: Poprawiona nazwa zmiennej

        # Dodaje wypożyczenie do listy
        self.wypozyczenia.append(wypozyczenie)

        return numer_wypozyczenia

    def znajdz_samochod(self, numer_rejestracyjny: str) -> Optional[Samochod]:
        """
        Znajduje samochód po numerze rejestracyjnym.
        
        Args:
            numer_rejestracyjny (str): Numer rejestracyjny samochodu
            
        Returns:
            Optional[Samochod]: Samochód o podanym numerze lub None
        """
        for samochod in self.samochody:
            if samochod.numer_rejestracyjny == numer_rejestracyjny:
                return samochod
        return None

    def get_dostepne_samochody(self) -> List[Samochod]:
        """
        Zwraca listę dostępnych samochodów.
        
        Returns:
            List[Samochod]: Lista dostępnych samochodów
        """
        dostepne = []
        for samochod in self.samochody:
            if samochod.czy_dostepny():
                dostepne.append(samochod)
        return dostepne

    def wypozycz_samochod(self, customer_id, numer_rejestracyjny, dni):
        """
        Wypożycza samochód klientowi.
        
        Args:
            customer_id (int): ID klienta
            numer_rejestracyjny (str): Numer rejestracyjny samochodu
            dni (int): Liczba dni wypożyczenia
            
        Returns:
            str: Numer wypożyczenia lub None jeśli nie udało się wypożyczyć
        """
        klient = self.znajdz_klienta(customer_id)
        samochod = self.znajdz_samochod(numer_rejestracyjny)
        
        if not klient:
            print("Nie znaleziono klienta")
            return None
            
        if not samochod:
            print("Nie znaleziono samochodu")
            return None
            
        if not samochod.czy_dostepny():
            print("Samochód nie jest dostępny")
            return None
        
        # Generuje numer wypożyczenia
        numer_wypozyczenia = f"W{self.nastepny_numer_wypozyczenia:03d}"
        self.nastepny_numer_wypozyczenia += 1
        
        # Tworzy wypożyczenie
        wypozyczenie = Wypozyczenie(
            numer_wypozyczenia, 
            customer_id, 
            numer_rejestracyjny, 
            dni, 
            samochod.dzienna_rata_wypozyczenia
        )
        
        # Oznacza samochód jako wypożyczony
        samochod.oznacz_jako_wypozyczony(numer_wypozyczenia)
        
        # Dodaje wypożyczenie do listy
        self.wypozyczenia.append(wypozyczenie)
        
        return numer_wypozyczenia

    def zwroc_samochod(self, numer_wypozyczenia: str) -> bool:
        """
        Zwraca samochód.
        
        Args:
            numer_wypozyczenia (str): Numer wypożyczenia
            
        Returns:
            bool: True jeśli udało się zwrócić samochód
        """
        for wypozyczenie in self.wypozyczenia:
            if wypozyczenie.numer_wypozyczenia == numer_wypozyczenia and wypozyczenie.czy_aktywne():
                wypozyczenie.oznacz_jako_zwrocony()
                samochod = self.znajdz_samochod(wypozyczenie.numer_rejestracyjny)
                if samochod:
                    samochod.oznacz_jako_dostepny()
                return True
        return False

    def get_aktywne_wypozyczenia(self) -> List[Wypozyczenie]:
        """
        Zwraca listę aktywnych wypożyczeń.
        
        Returns:
            List[Wypozyczenie]: Lista aktywnych wypożyczeń
        """
        aktywne = []
        for wypozyczenie in self.wypozyczenia:
            if wypozyczenie.czy_aktywne():
                aktywne.append(wypozyczenie)
        return aktywne

    def __str__(self) -> str:
        """
        Zwraca reprezentację tekstową wypożyczalni.
        
        Returns:
            str: Reprezentacja tekstowa wypożyczalni
        """
        return (f"Wypożyczalnia '{self.nazwa}': "
                f"{len(self.samochody)} samochodów, "
                f"{len(self.klienci)} klientów, "
                f"{len(self.wypozyczenia)} wypożyczeń")


if __name__ == "__main__":
    # Test wypożyczalni
    from samochod import RodzajPaliwa
    
    wypozyczalnia = Wypozyczalnia("AutoRent")