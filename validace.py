class Validace_vstupu:

    # Metoda pro validaci uživatelského vstupu volby
    @staticmethod
    def validace_volby(hodnota):
        if not hodnota:
            print("Neplatná volba - zadejte znovu!")
            return False
        else:
            if 0 < int(hodnota) < 7:
                return True
        return False

    # Metoda pro validaci textového vstupu
    @staticmethod
    def validace_textu(text):
        if isinstance(text, str) and len(text) > 4:
            return True
        return False

    # Metoda pro validaci jména nebo příjmení
    @staticmethod
    def validace_jmena(novy_nazev):
        if novy_nazev.isalpha() and len(novy_nazev)>2:
            return True
        return False

    # Metoda pro validaci telefonního čísla
    @staticmethod
    def validace_telefon(cislo):
        if cislo.isdigit() and len(cislo) == 9:
            return True
        return False

    # Metoda pro validaci data narození
    @staticmethod
    def validace_datum(datum):
        try:
            den, mesic, rok = map(int, datum.split('.'))
            if 1 <= den <= 31 and 1 <= mesic <= 12 and 1900 <= rok <= 2025:
                return True
        except ValueError:
            pass
        return False


