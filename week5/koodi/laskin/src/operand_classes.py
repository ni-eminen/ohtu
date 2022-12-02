from sovelluslogiikka import Sovelluslogiikka


class Summa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, reader):
        self.sovelluslogiikka = sovelluslogiikka
        self.reader = reader

    def suorita(self):
        return self.sovelluslogiikka.plus(int(self.reader()))


class Erotus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, reader):
        self.sovelluslogiikka = sovelluslogiikka
        self.reader = reader

    def suorita(self):
        return self.sovelluslogiikka.miinus(int(self.reader()))


class Nollaus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, reader):
        self.sovelluslogiikka = sovelluslogiikka
        self.reader = reader

    def suorita(self):
        return self.sovelluslogiikka.nollaa()


class Kumoa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, reader):
        self.sovelluslogiikka = sovelluslogiikka
        self.reader = reader

    def suorita(self):
        return self.sovelluslogiikka.kumoa()

