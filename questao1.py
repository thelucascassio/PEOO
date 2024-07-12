class Circulo:
  def __init__(self):
    self.__raio = 0
  def set_raio(self, valor):
    if valor >= 0: self.__raio = valor
    else: raise ValueError("Valor do raio não pode ser negativo")
  def get_raio(self, valor):
    return self.__raio
  def calcArea(self):
    return 3.14 * (self.__raio ** 2)
  def calcPerimetro(self):
    return 2 * 3.14 * self.__raio

x = Circulo()
x.set_raio(float(input("Digite o raio do círculo: ")))
print("A área do círculo é de", x.calcArea(), "m2")
print("O perímetro do círculo é de", x.calcPerimetro(), "m")