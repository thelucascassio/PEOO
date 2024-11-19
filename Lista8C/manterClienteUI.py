import streamlit as st
import pandas as pd
import view

class ManterClienteUI:
    @staticmethod
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        
        # Abas para cada função
        with tab1:
            ManterClienteUI.cliente_listar()
        with tab2:
            ManterClienteUI.cliente_inserir()
        with tab3:
            ManterClienteUI.cliente_atualizar()
        with tab4:
            ManterClienteUI.cliente_excluir()

    @staticmethod
    def cliente_inserir():
        st.header("Inserir Cliente")
        # Campos de entrada de texto com st.text_input
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        
        if st.button("Inserir"):
            if nome and email and fone:
                view.Cliente_inserir(nome, email, fone)
                st.success("Cliente inserido com sucesso!")
            else:
                st.error("Todos os campos precisam ser preenchidos!")

    @staticmethod
    def cliente_listar():
        st.header("Lista de Clientes")
        clientes = view.Cliente_listar()  
        # Se for uma lista de dicionários, podemos transformá-la em um DataFrame
        if isinstance(clientes, list):
            df = pd.DataFrame(clientes)
        else:
            df = clientes  # Se view.Cliente_listar já retornar um DataFrame
        
        if not df.empty:
            st.dataframe(df)  # Exibir DataFrame no Streamlit
        else:
            st.write("Nenhum cliente cadastrado.")

    @staticmethod
    def cliente_atualizar():
        st.header("Atualizar Cliente")
        # Obter lista de clientes
        clientes = view.Cliente_listar()  # Deve retornar uma lista de dicionários ou DataFrame
        if isinstance(clientes, list):
            df = pd.DataFrame(clientes)
        else:
            df = clientes

        # Exibir lista e selecionar cliente por ID
        if not df.empty:
            st.dataframe(df)  # Exibir lista de clientes
            ids = df['id'].tolist()  # Pegando todos os IDs dos clientes
            cliente_id = st.selectbox("Selecione o cliente pelo ID", ids)
            
            nome = st.text_input("Informe o novo nome", value=df[df['id'] == cliente_id]['nome'].values[0])
            email = st.text_input("Informe o novo e-mail", value=df[df['id'] == cliente_id]['email'].values[0])
            fone = st.text_input("Informe o novo fone", value=df[df['id'] == cliente_id]['fone'].values[0])

            if st.button("Atualizar"):
                view.Cliente_atualizar(cliente_id, nome, email, fone)
                st.success("Cliente atualizado com sucesso!")
        else:
            st.write("Nenhum cliente cadastrado para atualizar.")

    @staticmethod
    def cliente_excluir():
        st.header("Excluir Cliente")
        # Obter lista de clientes
        clientes = view.Cliente_listar()
        if isinstance(clientes, list):
            df = pd.DataFrame(clientes)
        else:
            df = clientes

        # Exibir lista e selecionar cliente por ID para exclusão
        if not df.empty:
            st.dataframe(df)
            ids = df['id'].tolist()
            cliente_id = st.selectbox("Selecione o cliente pelo ID para excluir", ids)
            
            if st.button("Excluir"):
                view.Cliente_excluir(cliente_id)
                st.success(f"Cliente com ID {cliente_id} excluído com sucesso!")
        else:
            st.write("Nenhum cliente cadastrado para excluir.")
