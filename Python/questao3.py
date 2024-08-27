class Conta:
  def __init__(self):
    self.__titular = ""
    self.__numero = ""
    self.__saldo = 0.00
    self.__op = 0
  def set_titular(self, nome):
      if nome != "": self.__titular = nome
      else: raise ValueError("Nome do titular inválido")
  def get_titular(self):
      return self.__titular
  def set_numero(self, numero):
      if numero >= 0: self.__numero = numero
      else: raise ValueError("Digite um número válido")
  def get_numero(self):
      return self.__numero
  def operacao(self):
    self.__op = int(input("Digite a operação desejada: \n 1 - Depósito \n 2 - Saque \n"))
    if self.__op == 1:
      self.__saldo = self.__saldo + float(input("Digite o valor do depósito: "))
    elif self.__op == 2:
      self.__saldo = self.__saldo - float(input("Digite o valor do saque: "))
    return self.__saldo

x = Conta()
x.titular = input("Digite o nome do titular: ").upper()
x.numero = input("Digite o número da conta: ")
print("Titular: ", x.titular, "\n"
      "Número da conta: ", x.numero, "\n"
      "Saldo: ", x.saldo, "R$")
running = True
while running:
  x.operacao()
  print("O saldo da conta é de:", x.saldo, "R$")
  running = input("Deseja continuar? (S/N)").upper()
  if running == "N":
    running = False


x.set_titular(input("Digite o nome do titular: ").upper())
x.set_numero(int(input("Digite o número da sua conta: ")))