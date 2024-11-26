import json

# Modelo
class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        if id < 0 and id != -1:  # Permite -1 como ID temporário
            raise ValueError("O id precisa ser maior ou igual a 0.")
        self._id = id
        if not nome:
            raise ValueError("O nome precisa possuir algum valor.")
        self._nome = nome
        if not email:
            raise ValueError("O e-mail precisa possuir algum valor.")
        self._email = email
        if not fone:
            raise ValueError("O telefone precisa possuir algum valor.")
        self._fone = fone
        if not senha:
            raise ValueError("A senha precisa possuir algum valor.")
        self._senha = senha

    #Sets
    def set_id(self, id):
       if id < 0:
          raise ValueError("O id precisa possuir valor maior ou igual a 0.")
       self._id = id
       
    def set_nome(self, nome):
        if not nome:
            raise ValueError("O nome precisa possuir algum valor.")
        self._nome = nome

    def set_email(self, email):
        if not email:
            raise ValueError("O e-mail precisa possuir algum valor.")
        self._email = email

    def set_fone(self, fone):
        if not fone:
            raise ValueError("O telefone precisa possuir algum valor.")
        self._fone = fone

    def set_senha(self, senha):
        if not senha:
            raise ValueError("A senha precisa possuir algum valor.")
        self._senha = senha
    # Gets
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_fone(self):
        return self._fone

    def get_senha(self):
        return self._senha
    
    #STR
    def __str__(self):
        return f"{self.get_nome()} - {self.get_email()} - {self.get_fone()}"

# Persistência
class Clientes:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c._id > m: m = c._id
    obj.set_id(m + 1)
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
      c._nome = obj._nome
      c._email = obj._email
      c._fone = obj._fone
      c._senha = obj._senha
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    cls.objetos.sort(key=lambda cliente: cliente._nome)
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
      json.dump([vars(c) for c in cls.objetos], arquivo)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          try:
              c = Cliente(obj["_id"], obj["_nome"], obj["_email"], obj["_fone"], obj["_senha"])
              cls.objetos.append(c)
          except ValueError as e:
              print(f"Erro ao carregar cliente: {e}")
    except FileNotFoundError:
      pass

