class Viagem():
  def __init__(self):
    self.__distancia = 0.00 #km
    self.__horas = 0
    self.__minutos = 0
  def set_distancia(self, valor):
    if valor >= 0: self.__distancia = valor
    else: raise ValueError("Não existe valor de distância negativa")
  def get_distancia(self):
    return self.__distancia
  def set_horas(self, valor):
      if valor>=0: self.__horas = valor
      else: raise ValueError("Não existe valor de horas negativas")
  def get_horas(self):
      return self.__horas
  def set_minutos(self, valor):
      if valor >= 0: self.__minutos = valor
      else: raise ValueError("Não existe valor de minutos negativos")
  def get_minutos(self):
      return self.__minutos
  def calcVelocidade(self):
    return self.__distancia / (self.__horas + (self.__minutos / 60))
x = Viagem()
x.set_distancia(float(input("Digite a distância percorrida: ")))
x.set_horas(int(input("Digite a quantidade de horas fechadas gastas na viagem: ")))
x.set_minutos(int(input("Digite agora os minutos que faltam para completar o tempo total de viagem: ")))
print("A velocidade média foi de", x.calcVelocidade(), "km/h")