import pickle

from models import PajamuIrasas, IslaiduIrasas

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