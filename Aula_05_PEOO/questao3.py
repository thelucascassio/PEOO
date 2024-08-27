class Conta:
  def __init__(self):
    self.__titular = ""
    self.__numero = ""
    self.__saldo = 0.00
  def depositar(self, valor):
    if valor > 0:
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else: raise ValueError("O valor do depósito deve ser positivo.")

  def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else: raise ValueError("O saldo é insuficiente ou valor de saque inválido.")

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
  def get_saldo(self):
        return self.__saldo
    
class UI:
    @staticmethod
    def menu():
        print("1 - Depósito, 2 - Saque, 3 - Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        x = Conta()
        x.set_titular(input("Digite o nome do titular: ").upper())
        x.set_numero(int(input("Digite o número da conta: ")))
        print(f"Titular: {x.get_titular()} \nNúmero da conta: {x.get_numero()} \nSaldo: {x.get_saldo()}R$")
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: 
                x.depositar(int(input("Digite o valor do depósito: ")))
            elif op == 2: 
                x.sacar(int(input("Digite o valor do saque: ")))
            print(f"O saldo atual é de R${x.get_saldo()}")
UI.main()