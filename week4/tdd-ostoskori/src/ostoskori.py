from functools import reduce

from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.items = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return reduce(lambda a, b: a+b.lukumaara(), self.items, 0)

    def hinta(self):
        return reduce(lambda a, b: a+b.hinta(), self.items, 0)

    def lisaa_tuote(self, lisattava: Tuote):
        self.items.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.items
