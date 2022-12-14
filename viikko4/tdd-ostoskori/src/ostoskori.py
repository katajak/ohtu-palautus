from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        total = 0
        for ostos in self.ostoskori:
            total += ostos.lukumaara()
        return total
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        total = 0
        for ostos in self.ostoskori:
            total += ostos.hinta()
        return total
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if self.ostoskori:
            for ostos in self.ostoskori:
                if lisattava.nimi() == ostos.tuotteen_nimi() and lisattava.hinta() == ostos.hinta()/ostos.lukumaara():
                    ostos.muuta_lukumaaraa(1)
                    return
        self.ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self.ostoskori:
            if poistettava.nimi() == ostos.tuotteen_nimi() and poistettava.hinta() == ostos.hinta()/ostos.lukumaara():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.ostoskori.remove(ostos)

    def tyhjenna(self):
        self.ostoskori = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
