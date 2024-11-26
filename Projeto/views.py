from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from datetime import datetime, timedelta

class View:
    def cliente_admin():
        for c in View.cliente_listar():
            if c._email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
        try:
            c = Cliente(0, nome, email, fone, senha)
            for x in View.cliente_listar():
                if x._email == c._email:
                    raise ValueError("Já existe um cliente com esse e-mail!")
            Clientes.inserir(c)

        except ValueError as e:
            print(f"Erro: {e}")

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha):
        try:
            c = Cliente(id, nome, email, fone, senha)
            for x in View.cliente_listar():
                if x._email != c._email:
                    Clientes.atualizar(c)
                else: raise ValueError("Já existe um cliente com esse e-mail!")
        except ValueError as e:
            print(f"Erro: {e}")

    def cliente_excluir(id):
        try:
            for h in View.horario_listar():
                if h.get_id_cliente() == id:
                    raise ValueError("Não foi possível excluir o cliente com esse id porque ele possui horários marcados.")
            c = Cliente(id, "", "", "", "")
            Clientes.excluir(c)
        except ValueError as e:
            print(f"Erro: {e}")    

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c._email == email and c._senha == senha:
                return {"id" : c._id, "nome" : c._nome }
        return None

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        try:
            if id_cliente < 0 or id_servico < 0:
                raise ValueError("O id cliente e o id serviço devem ser diferentes de 0. Corrija ambos se necessário.")
            c = Horario(0, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            for x in View.horario_listar():
                if x.get_id_cliente() == c.get_id_cliente() and x.get_id_servico() == c.get_id_servico():
                    raise ValueError("Já existe um horário para esse cliente e serviço!")
            Horarios.inserir(c)
        except ValueError as e:
            print(f"Erro {e}")

    def horario_listar():
        return Horarios.listar()

    def horario_listar_id(id):
        return Horarios.listar_id(id)    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h._data >= datetime.now() and h._id_cliente == None: disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        try:
            # Verifica se os IDs de cliente e serviço são válidos
            if id_cliente <= 0 or id_servico <= 0:
                raise ValueError("O id cliente e o id serviço devem ser diferentes de zero. Corrija ambos caso necessário.")
            
            c = Horario(id, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            
            # Verifica se já existe um horário com o mesmo cliente e serviço
            for x in View.horario_listar():
                if x.get_id_cliente() == c.get_id_cliente() and x.get_id_servico() == c.get_id_servico() and x.get_id() != c.get_id():
                    raise ValueError("Já existe um horário para esse cliente e serviço!")

            # Se não houver duplicação, atualiza o horário
            Horarios.atualizar(c)
        
        except ValueError as e:
            print(f"Erro: {e}")


    def horario_excluir(id):
        try:
            horario = View.horario_listar_id(id)
            if horario and horario.get_confirmado():
                raise ValueError(f"Não é possível excluir o horário com ID {id}, pois ele está confirmado para um cliente.")
            c = Horario(id, None)
            Horarios.excluir(c)
        except ValueError as e:
            print(f"Erro: {e}")    

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        try:
            i = data + " " + hora_inicio   # "05/11/2024 08:00"
            f = data + " " + hora_fim      # "05/11/2024 12:00"
            di = datetime.strptime(i, "%d/%m/%Y %H:%M")
            df = datetime.strptime(f, "%d/%m/%Y %H:%M")
            if di >= df:
                raise ValueError("O horário inicial deve ser menor que o horário final.")
            if intervalo <= 0:
                raise ValueError("O intervalo deve ser diferente e maior que zero.")
            d = timedelta(minutes=intervalo)
            x = di
            while x <= df:
                #cadastrar o horário x
                View.horario_inserir(x, False, None, None)
                #passar para o próximo horário
                x = x + d
        except ValueError as e:
            print(f"Erro: {e}")

    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        try:
            for h in View.horario_listar():
                if h.get_id_servico() == id: raise ValueError("Não foi possível excluir o serviço com esse id.")
            c = Servico(id, "", 0, 0)
            Servicos.excluir(c)
        except ValueError as e:
            print(f"Erro: {e}")
