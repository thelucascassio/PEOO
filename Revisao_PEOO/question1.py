class Água:
    def __init__(self):
        self.__mes = 0
        self.__ano = 0
        self.__consumo = 0

    def set_mes(self, mes):
        if 12 >= mes >= 1: mes = self.__mes
        else: raise ValueError("Mês inválido")
    def get_mes(self):
        return self.__mes
    def set_ano(self, ano):
        if ano >= 0: ano = self.__ano
        else: raise ValueError("Digite um ano válido")
    def get_ano(self):
        return self.__ano
    def set_consumo(self, consumo):
        if consumo >= 0:  self.__consumo = consumo
        else: raise ValueError("Digite um valor válido")
    def get_consumo(self):
        return self.__consumo
    def calcular_conta(self):
        if self.__consumo <= 10:
            return 38.00
        elif self.__consumo <= 20:
            return 38.00 + (self.__consumo - 10) * 5.00
        else:
            return 38.00 + 10 * 5.00 + (self.__consumo - 20) * 6.00

class UI:
    @staticmethod
    def main():
        x = Água()
        x.set_mes(int(input("Digite o mês da conta de água: ")))
        x.set_ano(int(input("Digite o ano da conta de água: ")))
        x.set_consumo(int(input("Digite o seu consumo nesse período: ")))
        print(f"O valor da conta de água foi de {x.calcular_conta():.2f}R$.")
UI.main()