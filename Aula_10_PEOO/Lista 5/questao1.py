from datetime import datetime
class Paciente:
    def __init__(self, n, c, t, nasc):
        self.__nome = n
        self.__cpf = c
        self.__telefone = t
        self.__nascimento = nasc
    def set_CPF(self, c):
        if c != "": self.__nome = c
        else: raise ValueError()
    def get_CPF(self):
        return self.__cpf
    
    def set_telefone(self, t):
        if t != "": self.__telefone = t
        else: raise ValueError()
    def get_telefone(self):
        return self.__telefone
    
    def set_nome(self, n):
        if n != "": self.__nome = n
        else: raise ValueError()
    def get_nome(self):
        return self.__nome
    
    def set_nascimento(self, nasc):
        if nasc != "": self.__nascimento = nasc
        else: raise ValueError()
    def get_nascimento(self):
        return self.__nascimento
    def Idade(self):
        hoje = datetime.now()
        tempo = hoje - datetime.strptime(self.__nascimento,"%d/%m/%Y") #time.delta()
        dias = tempo.days
        anos = dias // 365
        resto = anos % 365
        meses = resto / 30
        return f"{anos} ano(s) e {meses} meses"

    def __str__(self):
        return f"Nome: {self.get_nome()}, CPF: {self.get_CPF()}, Telefone: {self.get_telefone()}, Nascimento: {self.get_nascimento()}, Idade: {self.Idade()}"
    
class UI:
    @staticmethod
    def main():
        n = input("Digite o nome: ")
        c = input("Digite o CPF: ")
        t = input("Digite o telefone: ")
        nasc = input("Digite o nascimento: ")
        p = Paciente(n, c, t, nasc)
        print(p)

UI.main()
