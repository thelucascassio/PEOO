import random
class Bingo:
    def __init__(self):
        self.__numBolas = 10 #o atributo colocado no init é visto nos outros métodos também.
        self.__sorteados = []
    def iniciar(self, numBolas): #set_numBolas
        if numBolas > 0: self.__numBolas = numBolas
        else: raise ValueError("Número de bolas tem que ser positivo")
        self.__sorteados.clear()
    def proximo(self): #sorteia uma bola
        if len(self.__sorteados) == self.__numBolas: return "Fim de jogo"
        n = random.randint(1, self.__numBolas)
        #print("Dentro do método", n)
        while n in self.__sorteados:
            n = random.randint(1, self.__numBolas)
        self.__sorteados.append(n)
        return n
    def sorteados(self):
        return sorted(self.__sorteados)
    def __str__(self):
        return f"Foram sorteadas {len(self.__sorteados)} bolas"

class UI:
    @staticmethod
    def menu():
        print("1- Iniciar jogo, 2-Próximo, 3-Sorteados, 4-Info, 5-Fim")
        return int(input("Escolha uma opção!"))
    @staticmethod
    def main():
        b = Bingo()
        print("Bem-vindo ao IF Bingo!")
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.iniciar_jogo(b)
            if op == 2: UI.proximo(b)
            if op == 3: UI.sorteados(b)
            if op == 4: UI.info(b)
        print("Bye, guys!")
    @staticmethod
    def iniciar_jogo(b):
        n = int(input("Informe o número de bolas"))
        b.iniciar(n)
    @staticmethod
    def proximo(b):
        print(b.proximo())
    @staticmethod
    def sorteados(b):
        print(b.sorteados())
    @staticmethod
    def info(b):
        print(b)


UI.main()