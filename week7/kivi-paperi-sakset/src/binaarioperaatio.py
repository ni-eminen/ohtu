class BinaariOperaatio:
    def __init__(self, io):
        self.io = io
        self.luku1 = 0
        self.luku2 = 0

    def suorita(self):
        self.luku1 = int(self.io.lue("Luku 1:"))
        self.luku2 = int(self.io.lue("Luku 2:"))

        self.io.kirjoita(f"Vastaus: {self.laske()}")

    def laske(self):
        return 0
