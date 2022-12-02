class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.last_one = 0

    def miinus(self, arvo):
        self.last_one = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.last_one = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.last_one = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.last_one = self.tulos
        self.tulos = arvo

    def kumoa(self):
        self.tulos = self.last_one