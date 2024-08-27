class Cliente:
    def __init__(self, nome, cpf, limite):
        self.__nome = nome
        self.__cpf = cpf
        self.__limite = limite
    def set_nome(self, nome):
        if nome != "": self.__nome = nome
        else: raise ValueError()
    def set_cpf(self, cpf):
        if cpf != "": self.__cpf = cpf
        else: raise ValueError()
    def set_limite(self, limite):
        if limite != "": self.__limite = limite
        else: raise ValueError()
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_limite(self):
        return self.__limite
    def __str__(self):
        return f"Nome do cliente: {self.__cliente} - CPF: {self.__cpf} - Limite: {self.__limite}"

class Empresa:
    def __init__(self, nome):
        self.__nome = ""
        self.__clientes = []
    def Inserir(self, c):
        self.__clientes.append(c)
    def Excluir(self, c):
        self.__clientes.remove(c)
    def Listar(self):
        return self.__clientes[:]
    def __str__(self):
        return f"Nome da"
