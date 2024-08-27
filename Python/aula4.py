class Triangulo: #entidade
    def __init__(self): #construtor
        self.__b = 0.00 #atributos
        self.__h = 0.00
        #self.__b - o encapsulamento (__ - modificador de acesso, algo esses modificadores tornam os atributos privados) só permite acessar o atributo dentro da classe Triangulo()
    def set_base(self, valor):
        if valor >= 0: self.__b = valor
        else: raise ValueError ("Valor da altura não pode ser negativo!")
    def get_base(self):
        return self.__b
    def set_altura(self, valor):
        if valor >= 0: self.__h = valor
        else: raise ValueError ("Valor da altura não pode ser negativo!") #comunicar ao sistema para não rodar mais, que deu um erro de valor
    def get_altura(self):
        return self.__h
    def calcArea(self): #métodos (operação) - MÉTODO DE INSTÂNCIA (variável)
        return self.b * self.h /2
class UI: #Interface do usuário
    @staticmethod #prints e inputs nessa classe
    def main(): #operação principal da UI - MÉTODO DE CLASSE
        x = Triangulo()
        #x.__b = float(input("Informe o valor da base: "))
        #x.__h = float(input("Informe o valor da altura: "))
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        print(f"A base do triângulo é de {x.get_base()} m")
        print(f"A altura do triângulo é de {x.get_altura()} m")
        print(f"A área do triângulo é de {x.calcArea()} m²")
UI.main()
#versão sem encapsulamento - acesso direto ao atributo - qualquer valor é armazenado
#versão com encapsulamento - acesso ao atributo indiretamente - precisa-se de operações
#set - guardar, analisar o valor
#get - recuperar/retornar valor