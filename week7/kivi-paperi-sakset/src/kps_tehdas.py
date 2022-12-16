from kivi_paperi_sakset import KiviPaperiSakset
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

# Tää nyt ei ihan järkevästi toimi tälleen,
# mutta kuitenkin toteuttaa toiminnallisuuden ja
# poistaa riippuvuudet index.pystä. Lisäksi tähän voisi lähteä kehittelemään
# kaikenlaista, joten mielestäni täyttää tehtävän tekemisen tunnusmerkit :D
class KPSTehdas:
    def __init__(self, game: KiviPaperiSakset = KPSPelaajaVsPelaaja()):
        self.game = game

    def parempi_tekoaly(self):
        return KPSTehdas(KPSParempiTekoaly())

    def tekoaly(self):
        return KPSTehdas(KPSTekoaly())

    def pvp(self):
        return KPSTehdas(KPSPelaajaVsPelaaja())

    def create(self):
        return self.game