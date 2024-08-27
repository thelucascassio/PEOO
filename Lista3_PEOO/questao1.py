class Retangulo:
    def __init__(self, b, h):
        self.__b = 0.00
        self.__h = 0.00
        self.SetBase(b)
        self.SetAltura(h)
    def SetBase(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError("A base tem que ser positiva")
    def SetAltura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError("A altura tem que ser positiva")
    def GetBase(self):
        return self.__b
    def GetAltura(self):
        return self.__h
    def CalcArea(self):
        return self.__b * self.__h / 2
    def CalcDiagonal(self):
        return ((self.__b ** 2) + (self.__h ** 2)) ** (1/2)
    def __str__(self):
        return f"Base: {self.__b} - Altura: {self.__h} - Área: {self.CalcArea()} - Diagonal: {self.CalcDiagonal()}"
class UI:
    @staticmethod
    def main():
        b = (float(input("Informe a base do retângulo: ")))
        h = (float(input("Informe a altura do retângulo: ")))
        x = Retangulo(b,h)
        print(x)
UI.main()