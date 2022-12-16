from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _onko_ok_siirto(self, siirto):
        return siirto in ("k", "p", "s")

    def _toisen_siirto(self, siirto):
        self.tekoaly.aseta_siirto(siirto)
        return self.tekoaly.anna_siirto()