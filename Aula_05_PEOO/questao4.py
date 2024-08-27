class Cinema:
    def __init__(self):
        self.__dia = ""
        self.__horario = ""

    def get_valor_base(self):
        if self.__dia in ["segunda", "terça", "quinta"]:
            return 16.0
        elif self.__dia == "quarta":
            return 8.0
        elif self.__dia in ["sexta", "sábado", "domingo"]:
            return 20.0
        else:
            raise ValueError("Dia inválido")

    def is_acrescimo(self):
        horario = int(self.__horario.split(':')[0])
        if (24 > horario > 17) and self.__dia != "quarta":
            return True
        if self.__dia == "quarta":
            return False 
    
    def calcInteira(self):
        valor_base = self.get_valor_base()
        if self.is_acrescimo() == True:
            valor_base = valor_base * 1.5
        return valor_base
    def calcMeia(self):
        valor_meia = (self.get_valor_base()) / 2
        if self.__dia == "quarta":
            valor_meia = self.get_valor_base()
        elif self.is_acrescimo() == True:
            valor_meia = valor_meia * 1.5
        return valor_meia

    def set_dia(self, dia):
        self.__dia = dia

    def get_dia(self):
        return self.__dia
    
    def set_horario(self, horario):
        self.__horario = horario

    def get_horario(self):
        return self.__horario


# Programa para testar a classe
class UI:
    @staticmethod
    def main():
        x = Cinema()
        x.set_dia(input("Digite o dia da sessão: ").lower())
        x.set_horario(input("Digite o horário da sessão: "))
        print(f"Dia: {x.get_dia()}")
        print(f"Horário: {x.get_horario()}h")
        print(f"Valor entrada inteira: R${x.calcInteira():.2f}")
        print(f"Valor meia-entrada: R${x.calcMeia():.2f}")
UI.main()