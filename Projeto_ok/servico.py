import json

# Modelo
class Servico:
    def __init__(self, id, descricao, valor, duracao):
        if id < 0:
           raise ValueError("O id deve ser maior ou igual a 0.")
        self._id = id
        if not descricao:
            raise ValueError("A descrição deve possuir algum valor.")
        self._descricao = descricao
        if valor < 0:
            raise ValueError("O valor deve ser maior que 0.")
        self._valor = valor
        if duracao < 0:
            raise ValueError("A duração deve possuir algum valor.")
        self._duracao = duracao

    # Sets
    def set_id(self, id):
       if id < 0:
          raise ValueError("O id precisa possuir valor maior ou igual a 0.")
       self._id = id
       
    def set_descricao(self, descricao):
        if not descricao:
            raise ValueError("A descrição deve possuir algum valor.")
        self._descricao = descricao

    def set_valor(self, valor):
        if valor < 0:
            raise ValueError("O valor deve ser maior que 0.")
        self._valor = valor

    def set_duracao(self, duracao):
        if duracao < 0:
            raise ValueError("A duração deve possuir algum valor.")
        self._duracao = duracao
        
    # Gets
    def get_id(self):
        return self._id

    def get_descricao(self):
        return self._descricao

    def get_valor(self):
        return self._valor

    def get_duracao(self):
        return self._duracao

    def __str__(self):
        return f"{self.get_id()} - {self.get_descricao()} - R$ {self.get_valor():.2f} - {self.get_duracao()} min"

# Persistência
class Servicos:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c._id > m: m = c._id
    obj._id = m + 1
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c._id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj._id)
    if c != None:
      c._descricao = obj._descricao
      c._valor = obj._valor
      c._duracao = obj._duracao
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj._id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("servicos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("servicos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

