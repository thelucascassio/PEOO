from clientes import Cliente, Clientes, Horario, Horarios, Servico, Servicos
from datetime import datetime, timedelta


def Cliente_inserir(nome, email, fone):
    c = Cliente(0, nome, email, fone)
    Clientes.inserir(c)

def Cliente_listar():
    for c in Clientes.listar():
      print(c)

def Cliente_atualizar(id, nome, email, fone):
   c = Cliente(id, nome, email, fone)
   Clientes.atualizar(c)

def Cliente_excluir(id):
   c = Cliente(id, "", "", "")
   Clientes.excluir(c)

def Horario_inserir(data, confirmado, idCliente, idServico):
    h = Horario(0, data, confirmado, idCliente, idServico)
    Horarios.inserir(h)

def Horario_listar():
    for x in Horarios.listar():
        print(x)

def Horario_atualizar(id, data, confirmado, idCliente, idServico):
    h = Horario(id, data, confirmado, idCliente, idServico)
    Horarios.atualizar(h)

def Horario_excluir(id):
    h = Horario(id, "", "", "", "")
    Horarios.excluir(h)
    

def Servico_inserir(id, descricao, valor, duracao):
    s = Servico(id, descricao, valor, duracao)
    Servicos.inserir(s)

def Servico_listar():
    for x in Servicos.listar():
        print(x)
def Servico_atualizar(id, descricao, valor, duracao):
    s = Servico(id, descricao, valor, duracao)
    Servicos.atualizar(s)

def Servico_excluir(id):
    s = Servico(id, "", "", "")
    Servicos.excluir(s)

def AbrirAgenda(data, hr_inicial, hr_final, minutos):
        i = data + " " + hr_inicial   
        f = data + " " + hr_final      
        d = timedelta(minutes=minutos)
        di = datetime.strptime(i, "%d/%m/%Y %H:%M")
        df = datetime.strptime(f, "%d/%m/%Y %H:%M")
        x = di
        while x <= df:
            Horario_inserir(x, True, None, None)
            x = x + d