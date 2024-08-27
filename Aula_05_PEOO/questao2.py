class Viagem():
  def __init__(self):
    self.__distancia = 0.00 #km
    self.__horas = 0
    self.__minutos = 0
  def set_distancia(self, d):
    if d >= 0: self.__distancia = d
    else: raise ValueError("Não existe valor de distância negativa")
  def get_distancia(self):
    return self.__distancia
  def set_tempo(self, t): # formato "h:m" 1:30
        t = t.split(":")
        self.__horas = int(t[0])
        self.__minutos = int(t[1])
  def velocidade_media(self):
    return self.__distancia / (self.__horas + (self.__minutos / 60))
  
class UI:
  @staticmethod
  def main():
    x = Viagem()
    x.set_distancia(float(input("Digite a distância percorrida: ")))
    x.set_tempo(input("Digite o tempo de viagem percorrido, no formato horas:minutos"))
    print(f"A velocidade média foi de {x.velocidade_media()} km/h")
    
UI.main()