import streamlit as st
import pandas as pd
import view
import time

class ManterHorarioUI:
    @staticmethod
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        
        # Abas para cada função
        with tab1:
            ManterHorarioUI.horario_listar()
        with tab2:
            ManterHorarioUI.horario_inserir()
        with tab3:
            ManterHorarioUI.horario_atualizar()
        with tab4:
            ManterHorarioUI.horario_excluir()

    @staticmethod
    def horario_inserir():
        st.header("Inserir Horário")
        # Campos de entrada de texto com st.text_input
        data = st.text_input("Informe a data (dd/mm/aaaa)")
        confirmado = True
        idCliente = st.text_input("Informe o id do Cliente")
        idServico = st.text_input("Informe o id do Servico")
        
        if st.button("Inserir"):
            if data and confirmado:
                view.Horario_inserir(data, confirmado, idCliente, idServico)
                st.success("Horário inserido com sucesso!")
            else:
                st.error("Preencha os campos corretamente!")

    @staticmethod
    def horario_listar():
        st.header("Lista de Horarios")
        horarios = view.Horario_listar()  
        if isinstance(horarios, list):
            df = pd.DataFrame(horarios)
        else:
            df = horarios  
        
        if not df.empty:
            st.dataframe(df) 
        else:
            st.write("Nenhum horário cadastrado.")

    @staticmethod
    def horario_atualizar():
        st.header("Atualizar Horário")
        horario = view.Horario_listar()  
        if isinstance(horario, list):
            df = pd.DataFrame(horario)
        else:
            df = horario

        if not df.empty:
            st.dataframe(df)  
            ids = df['id'].tolist()  
            horarios_id = st.selectbox("Selecione o horário pelo ID", ids)
            
            data = st.text_input("Informe a nova data", value=df[df['id'] == horarios_id]['data'].values[0])
            confirmado = True
            idCliente = st.text_input("Informe o novo id do Cliente", value=df[df['id'] == horarios_id]['idCliente'].values[0])
            idServico = st.text_input("Informe o novo id do Serviço", value=df[df['id'] == horarios_id]['idServico'].values[0])

            if st.button("Atualizar"):
                view.Horario_atualizar(horarios_id, data, confirmado, idCliente, idServico)
                st.success("Horário atualizado com sucesso!")
        else:
            st.write("Nenhum horário cadastrado para atualizar.")

    @staticmethod
    def horario_excluir():
        st.header("Excluir Horário")
        horarios = view.Horario_listar()
        if isinstance(horarios, list):
            df = pd.DataFrame(horarios)
        else:
            df = horarios

        if not df.empty:
            st.dataframe(df)
            ids = df['id'].tolist()
            horarios_id = st.selectbox("Selecione o horário pelo ID para excluir", ids)
            
            if st.button("Excluir"):
                view.Horario_excluir(horarios_id)
                st.success(f"Horário com ID {horarios_id} excluído com sucesso!")
        else:
            st.write("Nenhum horário cadastrado para excluir.")


class AbrirAgendaUI:
    @staticmethod
    def main():
        st.header("Abertura a Agenda do dia")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        hr_inicial = st.text_input("Informe o horário de início no formato HH:MM")
        hr_final = st.text_input("Informe o horário de fim no formato HH:MM")
        minutos = st.text_input("Informe o intervalo de tempo entre os horários (min)")
        if st.button("Inserir Horários"):
            view.AbrirAgenda(data, hr_inicial, hr_final, int(minutos))
            st.success("Horários inseridos com sucesso!")
            time.sleep(2)
            st.rerun()