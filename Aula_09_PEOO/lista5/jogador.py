class Jogador:
    def __init__(self, nome_jogador, camisa, gols):
        self.__nome = ""
        self.__camisa = 0
        self.__gols = 0
    def set_nome(self, n):
        if n != "": self.__nome = n
        else: raise ValueError("Nome inválido")
    def set_camisa(self, n):
        if n >= 0: self.__camisa = n
        else: raise ValueError("Número inválido")
    def set_gols(self, n):
        if n >= 0: self.__gols = n
        else: raise ValueError("Número inválido")
    def get_nome(self):
        return self.__nome
    def get_camisa(self):
        return self.__camisa
    def get_gols(self):
        return self.__gols
    def __lt__(self, other):
        return self.__gols < other.__gols
    def __str__(self):
        return f"Nome do jogador: {self.__nome}\nNúmero da camisa: {self.__camisa}\nNúmero de gols: {self.__gols}"