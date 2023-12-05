
class Irasas:
    def __init__(self, suma):
        self.suma = abs(suma)


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma} ({self.siuntejas}, {self.info})"

    def __repr__(self):
        return f"Pajamos: {self.suma} ({self.siuntejas}, {self.info})"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, budas, isigyta, info):
        super().__init__(suma)
        self.budas = budas
        self.isigyta = isigyta
        self.info = info

    def __str__(self):
        return f"Išlaidos: {self.suma} ({self.budas}, {self.isigyta}, {self.info})"

    def __repr__(self):
        return f"Išlaidos: {self.suma} ({self.budas}, {self.isigyta}, {self.info})"