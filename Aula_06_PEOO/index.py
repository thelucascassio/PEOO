class Pais:
    def __init__(self, nome: str, população: int, area: float):
        self.__nome = nome
        self.__população = população
        self.__area = area
        if nome == "": raise ValueError
        if população <= 0: raise ValueError
        if area < 0: raise ValueError
    def __str__(self): #def to string
        return {self.__nome} - {self.__população} - {self.__area}
class UI:
    @staticmethod
    def main():
        nome = input()
        população = int(input())
        area = float(input())
        p = Pais(nome, população, area)
        print(p)