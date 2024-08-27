#CRUD de clientes - cadastro de clientes
#C - Create - insere um cliente no cadastro
#R - Read - lÊ os clientes cadastrados
#U - Update - atualiza os dados de um cliente
#D - Delete - remove um cliente do cadastro
import json
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
class Clientes: #que faz o CRUD
    objetos = [] #atributo estático
    @classmethod
    def __init__(self):
        self.objetos = []
    def inserir(self, obj):
        self.objetos.append(obj)
    def listar(self):
        return self.objetos
    def salvar(self):
        with open("clientes.json", mode="w") as arquivo: #arquivo, modo de escrever. Cria um arquivo no HD do computador e esse arquivo vem para mim com a possibilidade de eu escrever nele
            json.dump(self.objetos, arquivo, default = vars)
    def abrir(self):
        self.objetos = []
        with open("clientes.json", mode="r") as arquivo: #arquivo, modo de escrever. Cria um arquivo no HD do computador e esse arquivo vem para mim com a possibilidade de eu escrever nele
            texto = json.load(arquivo) #o load retorna um texto
        for obj in texto:
            c = Clientes(obj["id"], obj["nome"], obj["email"], obj["fone"])
            self.objetos.append(c)
a = Cliente(1, "Douglas Crockford", "d@gmail.com", "1234") #json
b = Cliente(2, "Jon Bosak", "j@gmail.com", "4321") #xml
crud = Clientes()
crud.inserir(a)
crud.inserir(b)
for c in crud.listar(): #pega a lista, retornada pela def listar e faz a listagem
    print(c)