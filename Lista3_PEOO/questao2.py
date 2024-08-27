class Frete:
    def __init__(self, distancia, peso):
        self.__distancia = 0.00
        self.__peso = 0.00
        self.SetDistancia(distancia)
        self.SetPeso(peso)
    def SetDistancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()
    def SetPeso(self, p):
        if p >= 0: self.__peso = p
        else: raise ValueError()
    def GetDistancia(self):
        return self.__distancia
    def GetPeso(self):
        return self.__peso
    def CalcFrete(self):
        return 0.01 * self.__peso * self.__distancia
    def __str__(self):
        return f"Distancia: {self.__distancia}- Peso: {self.__peso} - Frete: {self.CalcFrete()}R$"

class UI:
    @staticmethod
    def main():
        distancia = float(input())
        peso = float(input())
        x = Frete(distancia, peso)
        print(x)
UI.main()