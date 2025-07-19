from validace import Validace_vstupu as Va
from os import system


class UzivatelskeRozhrani:

    # Inicializace uživatelského rozhraní
    def __init__(self, jmeno, pozice):
        self._jmeno = jmeno
        self._pozice = pozice

    def __str__(self):
        return (f"{self._jmeno} - {self._pozice}")

    # Metoda pro vymazání obrazovky
    @staticmethod
    def cistic_obrazovky():
        system("cls")
        print(r"""
 _____           _       _                              
|  ___|         (_)     | |                             
| |__   __   __  _    __| |   ___   _ __     ___    ___ 
|  __|  \ \ / / | |  / _` |  / _ \ | '_ \   / __|  / _ \
| |___   \ V /  | | | (_| | |  __/ | | | | | (__  |  __/
\____/    \_/   |_|  \__,_|  \___| |_| |_|  \___|  \___|   

                             _ _     _             _ 
                            (_|_)   | |           (_)
                 _ __   ___  _ _ ___| |_ ___ _ __  _ 
                | '_ \ / _ \| | / __| __/ _ \ '_ \| |
                | |_) | (_) | | \__ \ ||  __/ | | | |
                | .__/ \___/| |_|___/\__\___|_| |_|_|
                | |        _/ |                      
                |_|       |__/                             
                """)

    # Metoda pro vyčkání na stisk klávesy
    @staticmethod
    def cekej_na_stisk():
        input("Stiskněte Enter pro pokračování...")

    # vypsáni hlavního uživatelského menu
    @staticmethod
    def vypis_menu():
        UzivatelskeRozhrani.cistic_obrazovky()
        print("\n")
        print("Vyberte akci:")
        print("1 - Přidat nového pojištěnce")
        print("2 - Vypsat všechny pojistné")
        print("3 - Vyhledat pojistného")
        print("4 - Konec")

    # Metoda pro zobrazení menu a validaci uživatelského vstupu
    @staticmethod
    def dej_volbu():
        UzivatelskeRozhrani.vypis_menu()
        while True:
            volba = input("Volba pojistné operace: ")
            if Va.validace_volby(volba):
                break
        return volba

    # Metoda zadavání jména
    @staticmethod
    def dej_jmeno():
       while True:
           UzivatelskeRozhrani.cistic_obrazovky()
           volba = input("Zadejte jméno: ")
           if Va.validace_jmena(volba):
               break
           UzivatelskeRozhrani.cekej_na_stisk()
       return volba

    # Metoda zadavání příjmení
    @staticmethod
    def dej_prijmeni():
        while True:
            UzivatelskeRozhrani.cistic_obrazovky()
            volba = input("Zadejte příjmení: ")
            if Va.validace_jmena(volba):
                break
            UzivatelskeRozhrani.cekej_na_stisk()
        return volba

    # Metoda zadavání telefonního čísla
    @staticmethod
    def dej_telefon():
        while True:
            UzivatelskeRozhrani.cistic_obrazovky()
            volba = input("Zadejte telefonní číslo: ")
            if Va.validace_telefon(volba):
                break
            UzivatelskeRozhrani.cekej_na_stisk()
        return volba

    # Metoda zadavání datum narození
    @staticmethod
    def dej_datum_narozeni():
        while True:
            UzivatelskeRozhrani.cistic_obrazovky()
            volba = input("Zadejte datum narození (DD.MM.RRRR): ")
            if Va.validace_datum(volba):
                break
            UzivatelskeRozhrani.cekej_na_stisk()
        return volba


