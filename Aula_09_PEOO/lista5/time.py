from jogador import Jogador
class Time():
    def __init__(self):
        self.__nome = ""
        self.__estado = ""
        self.__jogadores = []
    def Inserir(self, j):
        self.__jogadores.append(j)
    def Listar(self):
        for x in self.__jogadores:
            return (self.__jogadores[x])
    def Artilheiro(self):
        return max(self.__jogadores, key= lambda x:x.get_gols())
class UI:
    @staticmethod
    def main():
        op = 1
        while op == 1:
            nome_jogador = input("Digite o nome do jogador!")
            camisa = int(input("Digite o nº da camisa"))
            gols = int(input("Digite o número de gols"))
            j = Jogador(nome_jogador, camisa, gols)
            x = Time()
            x. Inserir(j)
            op = int(input("Deseja continuar? 1- Sim, 2- Não"))
        print(x.Artilheiro())
UI.main()