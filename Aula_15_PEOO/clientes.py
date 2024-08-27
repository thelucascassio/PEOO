# CRUD de clientes - cadastro de clientes - lista
# C - Create - insere um cliente no cadastro
# R - Read - lê os clientes cadastrados
# U - Update - atualiza os dados de um cliente
# D - Delete - remove um cliente do cadastro
from dataclasses import dataclass
from datetime import datetime
import json

# Modelo
class Cliente:
  def __init__(self, id, nome, email, fone):
    self.id = id
    self.nome = nome
    self.email = email
    self.fone = fone
  def __str__(self):
    return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Horario:
    def __init__(self, id, data, confirmado, idCliente, idServico):
        self.id = id
        self.data = data
        self.confirmado = confirmado
        self.idCliente = idCliente
        self.idServico = idServico
    def __str__(self):
        return f"{self.id} - {self.data} - {self.confirmado} - {self.idCliente} - {self.idServico}"

class Servico:
    def __init__(self, id, descricao, valor, duracao):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.duracao = duracao
    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.valor} - {self.duracao}"

# Persistência
class Clientes:
  objetos = []  # atributo estático
  @classmethod #usa-se porque não é uma classe estática - classmethod não cria os objetos
  def inserir(cls, obj): #cls - atributo da classe, acessa o atributo objetos, funciona como o self
    cls.abrir()
    m = 0                     # cálculo do maior id utilizado - começa com 0
    for c in cls.objetos:     # percorre a lista de clientes - c é cada cliente
      if c.id > m: m = c.id   # compara o id de c com m (maior)
    obj.id = m + 1  
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None 
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
       c.nome = obj.nome
       c.email = obj.email
       c.fone = obj.fone
    cls.salvar()   
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None: 
      cls.objetos.remove(c)
      cls.salvar()   
  @classmethod
  def salvar(cls):  
    with open("clientes.json", mode = "w") as arquivo:   # write
        json.dump(cls.objetos, arquivo, default = vars) 
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
      with open("clientes.json", mode = "r") as arquivo:   # read
        texto = json.load(arquivo)
        for obj in texto:
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])                     # dicionário
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

class Horarios:
  objetos = []  # atributo estático
  @classmethod #usa-se porque não é uma classe estática - classmethod não cria os objetos
  def inserir(cls, obj): #cls - atributo da classe, acessa o atributo objetos, funciona como o self
    cls.abrir()
    m = 0                     # cálculo do maior id utilizado - começa com 0
    for h in cls.objetos:     # percorre a lista de clientes - c é cada cliente
      if h.id > m: m = h.id   # compara o id de c com m (maior)
    obj.id = m + 1  
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for h in cls.objetos:
      if h.id == id: return h
    return None 
  @classmethod
  def atualizar(cls, obj):
    h = cls.listar_id(obj.id)
    if h != None:
       h.data = obj.data
       h.confirmado = obj.confirmado
       h.idCliente = obj.idCliente
       h.idServico = obj.idServico
    cls.salvar()   
  @classmethod
  def excluir(cls, obj):
    h = cls.listar_id(obj.id)
    if h != None: 
      cls.objetos.remove(h)
      cls.salvar()   
  @classmethod
  def salvar(cls):  
    with open("horarios.json", mode = "w") as arquivo:   # write
        json.dump(cls.objetos, arquivo, default = vars) 
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
      with open("horarios.json", mode = "r") as arquivo:   # read
        texto = json.load(arquivo)
        for obj in texto:
          h = Horario(obj["id"], obj["data"], obj["confirmado"], obj["idCliente"], obj["idServico"])                     # dicionário
          cls.objetos.append(h)
    except FileNotFoundError:
      pass

class Servicos:
  objetos = []  # atributo estático
  @classmethod #usa-se porque não é uma classe estática - classmethod não cria os objetos
  def inserir(cls, obj): #cls - atributo da classe, acessa o atributo objetos, funciona como o self
    cls.abrir()
    m = 0                     # cálculo do maior id utilizado - começa com 0
    for s in cls.objetos:     # percorre a lista de clientes - c é cada cliente
      if s.id > m: m = s.id   # compara o id de c com m (maior)
    obj.id = m + 1  
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for s in cls.objetos:
      if s.id == id: return s
    return None 
  @classmethod
  def atualizar(cls, obj):
    s = cls.listar_id(obj.id)
    if s != None:
       s.data = obj.data
       s.confirmado = obj.confirmado
       s.idCliente = obj.idCliente
       s.idServico = obj.idServico
    cls.salvar()   
  @classmethod
  def excluir(cls, obj):
    s = cls.listar_id(obj.id)
    if s != None: 
      cls.objetos.remove(s)
      cls.salvar()   
  @classmethod
  def salvar(cls):  
    with open("servicos.json", mode = "w") as arquivo:   # write
        json.dump(cls.objetos, arquivo, default = vars) 
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
      with open("servicos.json", mode = "r") as arquivo:   # read
        texto = json.load(arquivo)
        for obj in texto:
          s = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])# dicionário
          cls.objetos.append(s)
    except FileNotFoundError:
      pass


# Visão
class UI:
  @staticmethod
  def menu():
    print("1 - Inserir cliente, 2 - listar clientes, 3 - atualizar cliente, 4 - excluir cliente \n5 - Inserir horário, 6 - listar horários, 7 - atualizar horário, 8 - excluir horário \n9 - Inserir serviço, 10 - listar serviços, 11 - atualizar serviço, 12 - excluir serviço \n13- fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 13: 
      op = UI.menu()
      if op == 1: UI.cliente_inserir()
      if op == 2: UI.cliente_listar()
      if op == 3: UI.cliente_atualizar()
      if op == 4: UI.cliente_excluir()

      if op == 5: UI.horario_inserir()
      if op == 6: UI.horario_listar()
      if op == 7: UI.horario_atualizar()
      if op == 8: UI.horario_excluir()

      if op == 9: UI.servico_inserir()
      if op == 10: UI.servico_listar()
      if op == 11: UI.servico_atualizar()
      if op == 12: UI.servico_excluir()
      
#clientes
  @staticmethod
  def cliente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o fone: ")
    c = Cliente(0, nome, email, fone)
    Clientes.inserir(c)

  @staticmethod
  def cliente_listar():
    for c in Clientes.listar():
      print(c)

  @staticmethod
  def cliente_atualizar():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo fone: ")
    c = Cliente(id, nome, email, fone)
    Clientes.atualizar(c)

  @staticmethod
  def cliente_excluir():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    c = Cliente(id, "", "", "")
    Clientes.excluir(c)

#horarios
  @staticmethod
  def horario_inserir():
    data = input("Informe a data: ")
    confirmado = bool(input("Informe se confirmado (True/False): "))  # Ou use uma lógica para converter
    idCliente = int(input("Informe o id do cliente: "))
    idServico = int(input("Informe o id do serviço: "))
    h = Horario(0, data, confirmado, idCliente, idServico)
    Horarios.inserir(h)

  @staticmethod
  def horario_listar():
    for h in Horarios.listar():
      print(h)

  @staticmethod
  def horario_atualizar():
    UI.horario_listar()
    id = int(input("Informe o id do horario a ser atualizado: "))
    data = input("Informe o nome: ")
    confirmado = input("Informe o e-mail: ")
    c = Cliente()
    idCliente = c.id
    s = Servico()
    idServico = s.id
    h = Horario(id, data, confirmado, idCliente, idServico)
    Horarios.atualizar(h)

  @staticmethod
  def horario_excluir():
    UI.horario_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    h = Horario(id, "", "", "", "")
    Horarios.excluir(h)

#serviços
  @staticmethod
  def servico_inserir():
    #id = int(input("Informe o id: "))
    descricao = input("Informe a descrição do serviço: ")
    valor = input("Informe o valor: ")
    duracao = input("Informe a duração: ")
    s = Servico(0, descricao, valor, duracao)
    Servicos.inserir(s)

  @staticmethod
  def servico_listar():
    for s in Servicos.listar():
      print(s)

  @staticmethod
  def servico_atualizar():
    UI.servico_listar()
    id = int(input("Informe o id do serviço a ser atualizado: "))
    descricao = input("Informe a nova descrição: ")
    valor = input("Informe o novo valor: ")
    duracao = input("Informe a nova duracao: ")
    s = Servico(id, descricao, valor, duracao)
    Servicos.atualizar(s)

  @staticmethod
  def servico_excluir():
    UI.servico_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    s = Servico(id, "", "", "")
    Servicos.excluir(s)

UI.main()