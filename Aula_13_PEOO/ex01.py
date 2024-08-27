import json
x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
print(x)
print(type(x))

x["AM"] = "Manaus"
x["RN"] = ["Natal", "Parnamirim"]

print(*x) #mostra todas as chaves

#tupla

z = (1, 2) #é imutável

for item in x.items(): #método
    print(item) #retorna uma tupla
#método x.keys() - pega as chaves dos dicionários
#método x.values() - pega os valores
#o método copy copiará a variável, assim não permitindo que a original seja alterada
    


class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
a = Cliente(1, "Douglas Crockford") #json
b = Cliente(2, "Jon Bosak") #xml
lista = [a, b]
print(a)
print(b)
print(a.__dict__) #{'id': 1, 'nome': 'Douglas Crockford'}
#transformará os atributos/ em chaves de dicionário
print(vars(b)) #serialização


with open("clientes.json", mode="w") as arquivo: #arquivo, modo de escrever. Cria um arquivo no HD do computador e esse arquivo vem para mim com a possibilidade de eu escrever nele
    json.dump(lista, arquivo, default = vars)
#JSON é um dicionário em que todas as suas chaves são strings
#há o módulo json