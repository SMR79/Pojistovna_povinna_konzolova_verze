from pojistenec import Pojistenec


class Pojistovna:

    def __init__(self, rozhrani, jmeno_pojistovny = "Pojistovna"):
        self.rozhrani = rozhrani
        self._jmeno = jmeno_pojistovny

    def __str__(self):
        jmeno_rozhrani = getattr(self.rozhrani, "_jmeno", "")
        pozice_rozhrani = getattr(self.rozhrani, "_pozice", "")
        return (f"{self._jmeno} - {jmeno_rozhrani} - {pozice_rozhrani}")

    # Přidání nového pojištěnce
    def pridej_pojistence(self):
        jmeno = self.rozhrani.dej_jmeno()
        prijmeni = self.rozhrani.dej_prijmeni()
        datum_narozeni = self.rozhrani.dej_datum_narozeni()
        telefoni_cislo = self.rozhrani.dej_telefon()
        pojistenec = Pojistenec(jmeno, prijmeni, datum_narozeni, telefoni_cislo)
        return pojistenec

    # Vypis všech pojištěnců
    def vypis_vsechny_pojistence(self):
        if not Pojistenec.seznam_pojistencu:
            print("Žádní pojištěnci nejsou evidováni.")
            return
        for jeden_pojistenec in Pojistenec.seznam_pojistencu:
            print(f"{jeden_pojistenec.jmeno} {jeden_pojistenec.prijmeni} - {jeden_pojistenec.datum_narozeni} - {jeden_pojistenec.telefoni_cislo}")
        return

    # Vyhledání pojištěnce podle jména a příjmení
    def vyhledej_pojistence(self, jmeno, prijmeni):
        nalezeny_pojistenec = None
        for pojistenec in Pojistenec.seznam_pojistencu:
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                nalezeny_pojistenec = pojistenec
                return nalezeny_pojistenec
        return nalezeny_pojistenec





