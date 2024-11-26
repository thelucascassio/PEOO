import json
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self._id = id
        self._data = data
        self._confirmado = False
        self._id_cliente = 0
        self._id_servico = 0

    # Getters
    def get_id(self):
        return self._id

    def get_data(self):
        return self._data

    def get_confirmado(self):
        return self._confirmado

    def get_id_cliente(self):
        return self._id_cliente

    def get_id_servico(self):
        return self._id_servico

    # Setters
    def set_id(self, id):
        self._id = id

    def set_data(self, data):
        self._data = data

    def set_confirmado(self, confirmado):
        self._confirmado = confirmado

    def set_id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    def set_id_servico(self, id_servico):
        self._id_servico = id_servico

    def __str__(self):
        return f"{self.get_id()} - {self.get_data()}"

    def to_json(self):
        return {
            "id": self.get_id(),
            "data": self.get_data().strftime("%d/%m/%Y %H:%M"),
            "confirmado": self.get_confirmado(),
            "id_cliente": self.get_id_cliente(),
            "id_servico": self.get_id_servico()
        }

class Horarios:
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
      c._data = obj._data
      c._confirmado = obj._confirmado
      c._id_cliente = obj._id_cliente
      c._id_servico = obj._id_servico
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
    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Horario.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Horario(obj["_id"], datetime.strptime(obj["_data"], "%d/%m/%Y %H:%M"))
          c._confirmado = obj["_confirmado"]
          c._id_cliente = obj["_id_cliente"]
          c._id_servico = obj["_id_servico"]
          cls.objetos.append(c)
    except FileNotFoundError:
      pass



