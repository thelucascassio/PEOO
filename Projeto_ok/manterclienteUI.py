import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:    
            #for obj in clientes: st.write(obj)
            dic = []
            for obj in clientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        try:
            nome = st.text_input("Informe o nome do cliente")
            email = st.text_input("Informe o e-mail")
            fone = st.text_input("Informe o fone")
            senha = st.text_input("Informe a senha", type="password")
            if st.button("Inserir"):
                if any(campo == "" for campo in [nome, email, fone, senha]):
                    raise ValueError("Faltam campos a serem preenchidos")
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Cliente inserido com sucesso")
                time.sleep(2)
                st.rerun()
        except ValueError as e:
            print(f"Erro: {e}")

    def atualizar():
        try:
            clientes = View.cliente_listar()
            if len(clientes) == 0: 
                st.write("Nenhum cliente cadastrado")
            else:
                op = st.selectbox("Atualização de cliente", clientes)
                nome = st.text_input("Informe o novo nome do cliente")
                email = st.text_input("Informe o novo e-mail", op._email)
                fone = st.text_input("Informe o novo fone", op._fone)
                senha = st.text_input("Informe a nova senha", op._senha, type="password")
                if st.button("Atualizar"):
                    if any(campo == "" for campo in [nome, email, fone, senha]):
                        raise ValueError("Faltam campos a serem preenchidos")
                    View.cliente_atualizar(op._id, nome, email, fone, senha)
                    st.success("Cliente atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
        except ValueError as e:
            print(f"Erro: {e}")

    def excluir():
        try:
            clientes = View.cliente_listar()
            if len(clientes) == 0:
                st.write("Nenhum cliente cadastrado")
            else:
                op = st.selectbox("Selecione o cliente para exclusão", clientes, format_func=lambda c: c.get_nome())
                if st.button("Excluir"):
                    View.cliente_excluir(op.get_id())
                    st.success("Cliente excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
        except ValueError as e:
            st.error(f"Erro: {e}")

