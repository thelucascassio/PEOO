import streamlit as st
import pandas as pd
import view

class ManterServicoUI:
    @staticmethod
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterServicoUI.servico_listar()
        with tab2:
            ManterServicoUI.servico_inserir()
        with tab3:
            ManterServicoUI.servico_atualizar()
        with tab4:
            ManterServicoUI.servico_excluir()

    @staticmethod
    def servico_inserir():
        st.header("Inserir Serviço")
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o e-mail")
        duracao = st.text_input("Informe a duração")
        
        if st.button("Inserir"):
            if descricao and valor and duracao:
                view.Servico_inserir(descricao, valor, duracao)
                st.success("Serviço inserido com sucesso!")
            else:
                st.error("Preencha os campos corretamente!")

    @staticmethod
    def servico_listar():
        st.header("Lista de Servicos")
        servicos = view.Servico_listar() 
        if isinstance(servicos, list):
            df = pd.DataFrame(servicos)
        else:
            df = servicos  
        
        if not df.empty:
            st.dataframe(df)  
        else:
            st.write("Nenhum serviço cadastrado.")

    @staticmethod
    def servico_atualizar():
        st.header("Atualizar Serviço")
        servicos = view.Servico_listar()  
        if isinstance(servicos, list):
            df = pd.DataFrame(servicos)
        else:
            df = servicos

        if not df.empty:
            st.dataframe(df) 
            ids = df['id'].tolist()  
            servicos_id = st.selectbox("Selecione o serviço pelo ID", ids)
            
            descricao = st.text_input("Informe a nova descrição", value=df[df['id'] == servicos_id]['descricao'].values[0])
            valor = st.text_input("Informe o novo valor", value=df[df['id'] == servicos_id]['valor'].values[0])
            duracao = st.text_input("Informe a nova duração", value=df[df['id'] == servicos_id]['duracao'].values[0])

            if st.button("Atualizar"):
                view.Servico_atualizar(servicos_id, descricao, valor, duracao)
                st.success("Serviço atualizado com sucesso!")
        else:
            st.write("Nenhum serviço cadastrado para atualizar.")

    @staticmethod
    def servico_excluir():
        st.header("Excluir Serviço")
        servicos = view.Servico_listar()
        if isinstance(servicos, list):
            df = pd.DataFrame(servicos)
        else:
            df = servicos

        if not df.empty:
            st.dataframe(df)
            ids = df['id'].tolist()
            servicos_id = st.selectbox("Selecione o serviço pelo ID para excluir", ids)
            
            if st.button("Excluir"):
                view.Servico_excluir(servicos_id)
                st.success(f"Serviço com ID {servicos_id} excluído com sucesso!")
        else:
            st.write("Nenhum serviço cadastrado para excluir.")