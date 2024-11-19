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
