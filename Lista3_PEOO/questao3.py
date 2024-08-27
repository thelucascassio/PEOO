import math
class Bhaskara:
    def __init__(self, a, b, c):
        self.__a = 0.00
        self.__b = 0.00
        self.__c = 0.00
        self.SetA(a)
        self.SetB(b)
        self.SetC(c)
    def SetA(self, v):
        if v != 0: self.__a = v
        else: raise ValueError("O valor de a tem que ser diferente de zero!")
    def GetA(self):
        return self.__a
    def SetB(self, v):
        self.__b = v
    def GetB(self):
        return self.__b
    def SetC(self, v):
        self.__c = v
    def GetC(self):
        return self.__c
    def Delta(self):
        return (self.__b**2 - (4 * self.__a * self.__c))
    def TemRaizesReais(self):
        return (self.Delta() >= 0)
    def Raiz1(self):
        if self.TemRaizesReais(): return (-(self.__b) + math.sqrt(self.Delta())) / (2 * self.__a)
        else: print("Não há raízes reais")
    def Raiz2(self):
        if self.TemRaizesReais(): return (-(self.__b) - math.sqrt(self.Delta())) / (2 * self.__a)
        else: print("Não há raízes reais")
    def __str__(self):
        return f"Equação: {self.__a}x^2 + {self.__b}x + {self.__c}"
class UI:
    @staticmethod
    def main():
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        x = Bhaskara(a, b, c)
        print(x)
        print(f"Delta: {x.Delta()}")
        print(f"Tem raízes reais: {x.TemRaizesReais()}")
        print(f"Raiz 1: {x.Raiz1()}")
        print(f"Raiz 2: {x.Raiz2()}")
UI.main()