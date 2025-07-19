from ur import UzivatelskeRozhrani as Ur
from pojistovna import Pojistovna

uzivatelske_rozhrani = Ur("Slavomír", "specialista pojištění")
pojistovna = Pojistovna(uzivatelske_rozhrani)

def main():
    while True:
        volba = uzivatelske_rozhrani.dej_volbu()
        uzivatelske_rozhrani.cistic_obrazovky()
        if volba == "1":
            print(f"Vybraná volba: {volba} - Přidání nového pojistného")
            novy_pojistenec = pojistovna.pridej_pojistence()
            print(f"Zadaný pojištěnec číslo {novy_pojistenec._cislo_pojistence}:\n{novy_pojistenec._jmeno} {novy_pojistenec._prijmeni}")
            continue
        elif volba == "2":
            print(f"Vybraná volba: {volba} - Vypsání všech pojistných")
            print(f"Seznam pojištěnců:")
            pojistovna.vypis_vsechny_pojistence()
        elif volba == "3":
            print(f"Vybraná volba: {volba} - Vyhledání pojistného")
            jmeno = Ur.dej_jmeno()
            prijmeni = Ur.dej_prijmeni()
            hledany_pojistenec = pojistovna.vyhledej_pojistence(jmeno, prijmeni)
            if hledany_pojistenec is not None:
                print(f"Pojištěnec {hledany_pojistenec} byl nalezen.")
            else:
                print("Pojištěnec nebyl nalezen.")
        elif volba == "4":
            print(f"Vybraná volba: {volba} - Konec programu.\nNA SHLEDANOU {uzivatelské_rozhraní._jmeno}!!!")
            break
        uzivatelske_rozhrani.cekej_na_stisk()



main()



