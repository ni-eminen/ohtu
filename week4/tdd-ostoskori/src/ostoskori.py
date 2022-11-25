from functools import reduce

from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.items = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return len(self.items)

    def hinta(self):
        return reduce(lambda a, b: a+b.hinta(), self.items, 0)

    def lisaa_tuote(self, lisattava: Tuote):
        lisattava_n = lisattava.nimi()
        for i, item in enumerate(self.items):
            if lisattava_n == item.tuotteen_nimi():
                item.muuta_lukumaaraa(1)
                return


        self.items.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        poistettava_n = poistettava.nimi()
        for i, item in enumerate(self.items):
            if poistettava_n == item.tuotteen_nimi() and item.lukumaara() > 1:
                item.muuta_lukumaaraa(-1)
                return
            elif poistettava_n == item.tuotteen_nimi() and item.lukumaara() == 1:
                del self.items[i]


    def tyhjenna(self):
        self.items = []

    def ostokset(self):
        return self.items
