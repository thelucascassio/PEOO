class Playlist:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []
        if nome == "": raise ValueError("O nome não pode ser vazio")
    def inserir(self, m): #insere um objeto música em um objeto playlist
        self.__musicas.append(m)
    def listar(self):
        return self.__musicas[:] #fazer cópia de uma lista
    def __str__(self):
        return f"Playlist {self.__nome} - {self.__descricao} tem {len(self.__musicas)} músicas"