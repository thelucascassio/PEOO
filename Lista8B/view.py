from cliente import Cliente, Clientes

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