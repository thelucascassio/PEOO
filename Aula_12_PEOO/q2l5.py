from enum import Enum

class Pagamento(enum.Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, valor):
        self.valor = valor
        self.situacao_pg = Pagamento.EmAberto
    def Pagar(self, valor_pago):
        if self.valor == valor_pago:
            self.situacao_pg = Pagamento.Pago
        else:
            self.situacao_pg = Pagamento.PagoParcial