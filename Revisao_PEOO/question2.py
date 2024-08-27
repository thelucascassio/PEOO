class Ingresso:
    def __init__(self):
        self.__dia = ""
        self.__hora = 0
    def set_dia(self, dia):
        dias_validos = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
        if dia in dias_validos:
            self.__dia = dia
        else: raise ValueError("Digite um dia válido")
    def get_dia(self):
        return self.__dia
    def set_hora(self, hora):
        if 24 >= hora >= 0:
            self.__hora = hora
        else: raise ValueError("Digite uma hora válida")
    def get_hora(self):
        return self.__hora
    def calcIngresso(self):
        if self.__dia == "quinta":
            return 6
        elif self.__dia != "quinta":
            if self.__hora <= 16:
                return 5
            else:
                return 10
class UI:
    @staticmethod
    def main():
        x = Ingresso()
        x.set_dia(input("Digite o dia da sessão: "))
        x.set_hora(int(input("Digite o horário da sessão: ")))
        print(f"O valor do ingresso será de {x.calcIngresso()}R$.")
UI.main()