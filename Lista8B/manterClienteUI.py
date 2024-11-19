import streamlit as st
import view
import pandas as pd
class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()
    @staticmethod
    def listar():
        clientes = view.Cliente_listar()
        if len(clientes) == 0:
            st.write("Não há clientes cadastrados!")
        else:
            dic = []
            for obj in clientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    @staticmethod
    def inserir():
        nome = st.text_input("Digite seu nome")
        email = st.text_input("Informe o email do cliente")
        fone = st.text_input("Informe o telefone do cliente")
        if st.button("Inserir"):
            view.Cliente_inserir(nome, email, fone)
            st.success("Cliente inserido com sucesso")
            #funciona como o f5, refreshes the web page automatically
    @staticmethod
    def atualizar():
        clientes = view.Cliente_listar()
        if len(clientes) == 0: st.write("Não há clientes cadastrados!")
        else:
            op = st.selectbox("Atualização do cliente", clientes)
            nome = st.text_input("Digite seu nome")
            email = st.text_input("Informe o email do cliente")
            fone = st.text_input("Informe o telefone do cliente")
            if st.button("Atualizar"):
                view.Cliente_atualizar(op.id, nome, email, fone)
                st.success("Cliente atualizado com sucesso")
                st.rerun()
    def excluir():
        clientes = view.Cliente_listar()
        if len(clientes) == 0: st.write("Não há clientes cadastrados!")
        else:
            op = st.selectbox("Exclusão do cliente", clientes)
            if st.button("Atualizar"):
                view.Cliente_excluir(op.id)
                st.success("Cliente atualizado com sucesso")
                st.rerun()