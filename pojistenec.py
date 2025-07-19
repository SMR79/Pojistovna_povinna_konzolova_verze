from validace import Validace_vstupu as Va

class Pojistenec:
    pojistencu_celkem = 0
    seznam_pojistencu = []

    def __init__(self, jmeno, prijmeni, datum_narozeni, telefoni_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.datum_narozeni = datum_narozeni
        self.telefoni_cislo = telefoni_cislo
        Pojistenec.pojistencu_celkem += 1
        self._cislo_pojistence = Pojistenec.pojistencu_celkem
        Pojistenec.seznam_pojistencu.append(self)

    def __str__(self):
        return f"Pojištěnec č.{self._cislo_pojistence} - {self.jmeno} {self.prijmeni} - {self.datum_narozeni} - {self.telefoni_cislo}"

    # Gettery a Settery pro atributy jmeno, prijmeni, datum_narozeni, telefoni_cislo a cislo_pojistence

    @property
    def cislo_pojistence(self):
        return self._cislo_pojistence

    @property
    def jmeno(self):
        return self._jmeno

    @jmeno.setter
    def jmeno(self, jmeno):
        if Va.validace_jmena(jmeno):
            self._jmeno = jmeno
        else:
            raise ValueError("Vstup musí obsahovat pouze znaky abecedy a být delší než dvě písmena!")

    @property
    def prijmeni(self):
        return self._prijmeni

    @prijmeni.setter
    def prijmeni(self, prijmeni):
        if Va.validace_jmena(prijmeni):
            self._prijmeni = prijmeni
        else:
            raise ValueError("Vstup musí obsahovat pouze znaky abecedy a být delší než dvě písmena!")

    @property
    def datum_narozeni(self):
        return self._datum_narozeni

    @datum_narozeni.setter
    def datum_narozeni(self, datum_narozeni):
        if Va.validace_datum(datum_narozeni):
            self._datum_narozeni = datum_narozeni
        else:
            raise ValueError("Neplatný formát data! Zadejte ve formátu DD.MM.RRRR")

    @property
    def telefoni_cislo(self):
        return self._telefoni_cislo
    @telefoni_cislo.setter
    def telefoni_cislo(self, telefoni_cislo):
        if Va.validace_telefon(telefoni_cislo):
            self._telefoni_cislo = telefoni_cislo
        else:
            raise ValueError("Telefonní číslo musí obsahovat pouze číslice a mít délku 9 znaků!")

