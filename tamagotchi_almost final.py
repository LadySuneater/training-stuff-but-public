import pickle
import random

class Mazlicek:
    def __init__(self, jmeno):  # konstruktor
        self._spokojenost = False
        self._jmeno = jmeno

    def __str__(self):  # vypis mazlicka a jeho stavu
        if self._spokojenost:
            return f"{self._jmeno} je spokojeny"
        else:
            return f"{self._jmeno} je nespokojeny"

    def set_jmeno(self, jmeno):
        self._jmeno = jmeno

    def get_jmeno(self):
        return self._jmeno

    def get_spokojenost(self):
        return self._spokojenost


class Papousek(Mazlicek):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self.__zrni = False
        self.__voda = False
        self.__povidani = False

    def __str__(self):
        return (f"V seznamu je {self.get_jmeno()}, papousek, ktery {'je' if self.get_spokojenost() else 'neni'} " +
                f"spokojeny. Papousek {'ma' if self.get_zrni() else 'nema'} zrni," +
                f" {'ma' if self.get_zrni() else 'nema'} vodu a {'povidal' if self.get_povidani() else 'nepovidal'} si.")

    def set_spokojenost(self):
        self._spokojenost = self.__zrni and self.__voda and self.__povidani

    def set_zrni(self, zrni):
        self.__zrni = zrni
        print("Nasypal jsi papouskovi zrni.")
        self.set_spokojenost()

    def set_voda(self, voda):
        self.__voda = voda
        print("Vymenil jsi papouskovi vodu.")
        self.set_spokojenost()

    def set_povidani(self, povidani):
        self.__povidani = povidani
        print("Povidal sis s papouskem.")
        self.set_spokojenost()

    def get_zrni(self):
        return self.__zrni

    def get_voda(self):
        return self.__voda

    def get_povidani(self):
        return self.__povidani

    def nasypat_zrni(self):
        self.set_zrni(True)
        self.set_spokojenost()

    def vymenit_vodu(self):
        self.set_voda(True)
        self.set_spokojenost()

    def povidat_si(self):
        self.set_povidani(True)
        self.set_spokojenost()

    def pece(self):
        druh_pece = input(
            "Jak chces pecovat o papouska? Muzes nasypat zrni, vymenit vodu nebo si popovidat."
            " Napis 'zrni', 'voda' nebo 'povidani'.")
        if druh_pece.lower() == "zrni":
            self.nasypat_zrni()
        elif druh_pece.lower() == "voda":
            self.vymenit_vodu()
        elif druh_pece.lower() == "povidani":
            slovo = input("Rekni neco papouskovi: ")
            if slovo != "":
                print (f"Papousek: {slovo}")
                self.povidat_si()
        else:
            return f"Neplatny vstup. Takovou peci papousek nepotrebuje."


class Chameleon(Mazlicek):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self._schovavana = False
        self._voda = False
        self._cvrcci = False

    def __str__(self):
        return (f"V seznamu je {self.get_jmeno()}, chameleon, ktery {'je' if self.get_spokojenost() else 'neni'} " +
                f"spokojeny. Chameleon {'ma' if self.get_cvrcci() else 'nema'} cvrcky," +
                f" {'ma' if self.get_voda() else 'nema'} vodu a"
                f" {'hral si na schovavanou' if self.get_schovavana() else 'nehral si na schovavanou'}.")

    def get_schovavana(self):
        return self._schovavana

    def set_schovana(self, schovana):
        self._schovavana = schovana
        self.set_spokojenost()

    def get_voda(self):
        return self._voda

    def set_voda(self, voda):
        self._voda = voda
        print("Vymenil jsi chameleonovi vodu.")
        self.set_spokojenost()

    def get_cvrcci(self):
        return self._cvrcci

    def set_cvrci(self, cvrcci):
        self._cvrcci = cvrcci
        print("Nasypal jsi chameleonovi cvrcky.")
        self.set_spokojenost()

    def set_spokojenost(self):
        self._spokojenost = self._schovavana and self._voda and self._cvrcci

    def hrat_na_schovavanou(self):
        self.set_schovana(True)
        pokusy = 0
        max_pokusy = 3
        mozne_schovky = ['postel', 'knihovna', 'kuchyne', 'pradelni kos', 'policka']
        schovka = mozne_schovky[random.randint(0, len(mozne_schovky) - 1)]
        while pokusy < max_pokusy:
            tip = input(
                "Kam se schoval chameleon? Moznosti jsou 'postel', 'knihovna', 'kuchyne',"
                " 'pradelni kos' a 'policka'. Hledej poradne a odpovez jednim ze slov: ").lower()
            if tip == schovka:
                print("Gratuluji, nasel jsi chameleona a ten je spokojeny!")
                self.set_schovana(True)
                return
            else:
                print("Tady chameleon neni. Zkus to znovu.")
                pokusy += 1
        print(
            "Bohuzel, vycerpal jsi vsechny pokusy na hadani."
            " Chameleon opravdu dobre splynul s okolim, ale neni spokojeny. Byl schovany zde:",
            schovka)
        self.set_schovana(False)
        self.set_spokojenost()

    def vymenit_vodu(self):
        self.set_voda(True)
        self.set_spokojenost()

    def nasypat_cvrcky(self):
        self.set_cvrci(True)
        self.set_spokojenost()

    def pece(self):
        druh_pece = input(
            "Jak chces pecovat o chameleona? Muzes nasypat cvrcky, vymenit vodu nebo si hrat na schovavanou."
            " Napis 'cvrcci', 'voda' nebo 'schovka'.")
        if druh_pece.lower() == "cvrcci":
            self.nasypat_cvrcky()
        elif druh_pece.lower() == "voda":
            self.vymenit_vodu()
        elif druh_pece.lower() == "schovka":
            self.hrat_na_schovavanou()

class Pstros(Mazlicek):
    def __init__(self, jmeno):
        super().__init__(jmeno)
        self.__pisek = False
        self.__trava = False
        self.__hlava = False

    def __str__(self):
        return (f"V seznamu je {self.get_jmeno()}, pstros, ktery {'je' if self.get_spokojenost() else 'neni'} " +
                f"spokojeny. Pstros {'ma' if self.get_pisek() else 'nema'} pisek," +
                f" {'ma' if self.get_trava() else 'nema'} travu a {'ma' if self.get_hlava() else 'nema'} hlavu v pisku.")

    def set_spokojenost(self):
        self._spokojenost = self.__pisek and self.__trava and self.__hlava

    def set_pisek(self, pisek):
        self.__pisek = pisek
        print("Nasypal jsi pstrosovi pisek.")
        self.set_spokojenost()

    def set_trava(self, trava):
        self.__trava = trava
        print("Dal jsi pstrosovi travu.")
        self.set_spokojenost()

    def set_hlava(self, hlava):
        self.__hlava = hlava and self.__pisek
        print("Pstros schoval hlavu do pisku a ma radost.")
        self.set_spokojenost()

    def get_pisek(self):
        return self.__pisek

    def get_trava(self):
        return self.__trava

    def get_hlava(self):
        return self.__hlava

    def nasypat_pisek(self):
        self.set_pisek(True)
        self.set_spokojenost()

    def nasypat_travu(self):
        self.set_trava(True)
        self.set_spokojenost()

    def schovat_hlavu(self):
        self.set_hlava(True)
        self.set_spokojenost()

    def pece(self):
        druh_pece = input(
            "Jak chces pecovat o pstrosa? Muzes nasypat travu nebo pisek a pak ho vybidnout, at schova hlavu do pisku."
            " Napis 'pisek', 'trava' nebo 'hlava'.")
        if druh_pece.lower() == "pisek":
            self.nasypat_pisek()
        elif druh_pece.lower() == "trava":
            self.nasypat_travu()
        elif druh_pece.lower() == "hlava" and not self.__pisek:
            print("Nejprve musis pstrosovi nasypat pisek, aby mel kam schovat hlavu!")
            self.pece()
        elif druh_pece.lower() == "hlava" and self.__pisek:
            self.schovat_hlavu()
        else:
            return f"Neplatny vstup. Takovou peci pstros nepotrebuje."

class Zverinec:
    def __init__(self, soubor):
        self.__soubor = soubor
        try:
            file = open(self.__soubor, 'rb')
            self.__seznam = pickle.load(file)
        except FileNotFoundError:
            self.__seznam = list()

    def ukladani(self):
        with open(self.__soubor, "wb") as file:
            pickle.dump(self.__seznam, file)

    def zvirata_ve_zverinci(self):
        if self.__seznam:
            for zvire in self.__seznam:
                print(zvire)
        else:
            volba = input("V seznamu neni zadne zvire. Chcete pridat zvire do seznamu? 1 - Ano. 2 - Ne.")
            if volba.lower() == "1":
                self.pridej_zvire()
            if volba.lower() == "2":
                print_menu()
            elif volba != "1" and volba != "2":
                print("Neplatny vstup.")

    def celkova_spokojenost(self):
        vysledek = True
        for zvire in self.__seznam:
            vysledek = vysledek and zvire.get_spokojenost()
        return vysledek


    def pridej_zvire(self):
        volba = input("Jake zvire chcete pridat do zverince?\nZde jsou moznosti: chameleon, papousek, pstros. ")
        jmeno = input("Jak se bude zvire jmenovat? ")

        if volba.lower() == "chameleon":
            chamik = Chameleon(jmeno)
            self.__seznam.append(chamik)
            print (f"Chameleon {jmeno} byl pridan do zverince.")
        if volba.lower() == "papousek":
            papik = Papousek(jmeno)
            self.__seznam.append(papik)
            print (f"Papousek {jmeno} byl pridan do zverince.")
            jmena.add(jmeno)
        if volba.lower() == "pstros":
            pstros = Pstros(jmeno)
            self.__seznam.append(pstros)
            print(f"Pstros {jmeno} byl pridan do zverince.")
        if volba.lower() != "chameleon" and volba.lower() != "papousek" and volba.lower() != "pstros":
            print("Neplatny vstup. Nemate ve slovech preklep? Zkuste to znovu.")
            self.pridej_zvire()

    def pece_o_zvire(self):
        print("O ktere zvire se chcete postarat? Moznosti jsou nasledujici: ")
        for index, zvire in enumerate(self.__seznam, start=1):
            print(f"{index}. {zvire}")

        volba = input("Napiste jmeno zvirete, o ktere se chcete postarat: ")
        volba_lower = volba.lower()
        zvire = [obj for obj in self.__seznam if obj.get_jmeno().lower() == volba_lower]

        if zvire and zvire[0]:
            zvire = zvire[0]

            if isinstance(zvire, Papousek):
                zvire.pece()
            elif isinstance(zvire, Chameleon):
                zvire.pece()
            elif isinstance(zvire, Pstros):
                zvire.pece()
            else:
                print("Takove zvire v seznamu neni.")
                self.pece_o_zvire()
        else:
            print("Zvire nenalezeno.")
            self.pece_o_zvire()


def print_menu():
    print("Hlavni menu:")
    print("1 - Pridat zvire")
    print("2 - Zobrazit seznam zvirat")
    print("3 - Postarat se o zvire")
    print("End - Ukoncit program")


def main():
    zver = Zverinec("soubor.dat")
    volba = ""
    print("Vitejte ve Zverinci, jednoduche textove hre, ve ktere muzete do sveho zverince pridat libovolne mnozstvi zvirat,")
    print("a pak se starate o uspokojovani jejich potreb. Bude mit chameleon dost cvrcku? Jak pojmenujete sveho pstrosa?")
    print("A o cem si budete povidat s papouskem? Prijemnou zabavu!")

    while volba != "end":
        print_menu()
        volba = input("Vyberte jedno z cisel: ")
        zver.ukladani()
        if volba.lower() == "end":
            print("Ukoncili jste program.")
        elif volba == "1":
            zver.pridej_zvire()
        elif volba == "2":
            zver.zvirata_ve_zverinci()
        elif volba == "3":
            zver.pece_o_zvire()
        elif volba != "1" and volba != "2" and volba != "3" and volba != "end":
            print("Neplatny vstup.")
            print_menu()

if __name__ == "__main__":
    main()
