import pickle


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


class Biudzetas:
    def __init__(self):
        self.zurnalas = self.nuskaityti_is_failo()

    def nuskaityti_is_failo(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def irasyti_i_faila(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamu_irasa(self):
        suma = float(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        info = input("Papildoma informacija: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_i_faila()

    def prideti_islaidu_irasa(self):
        suma = float(input("Suma: "))
        budas = input("Mokėjimo būdas: ")
        isigyta = input("Įsigyta prekė/paslauga: ")
        info = input("Papildoma informacija: ")
        irasas = IslaiduIrasas(suma, budas, isigyta, info)
        self.zurnalas.append(irasas)
        self.irasyti_i_faila()

    def gauti_ataskaita(self):
        print("-------------------")
        print("Ataskaita:")
        for irasas in self.zurnalas:
            print(irasas)
        print("-------------------")

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                balansas += irasas.suma
            if type(irasas) is IslaiduIrasas:
                balansas -= irasas.suma
        print("Balansas:", balansas)


biudzetas = Biudzetas()

while True:
    veiksmas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - ataskaita\n4 - balansas\n0 - išeiti\n"))
    match veiksmas:
        case 1:
            biudzetas.prideti_pajamu_irasa()
        case 2:
            biudzetas.prideti_islaidu_irasa()
        case 3:
            biudzetas.gauti_ataskaita()
        case 4:
            biudzetas.gauti_balansa()
        case 0:
            break
        case _:
            print("Nera tokio pasirinkimo")
