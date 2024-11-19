import streamlit as st
from manterUI import ManterClienteUI
from manterHorarioUI import ManterHorarioUI, AbrirAgendaUI
from manterServicoUI import ManterServicoUI
class IndexUI:
    def main():
        st.title("Bem-vindo ao sistema de agendamentos!")
        st.button("Começar cadastro")
        menu = st.sidebar.selectbox("Menu", ("Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia"))
        if menu == "Cadastro de Clientes": ManterClienteUI.main()
        if menu == "Cadastro de Horários": ManterHorarioUI.main()
        if menu == "Cadastro de Serviços": ManterServicoUI.main()
        if menu == "Abrir Agenda do Dia": AbrirAgendaUI.main()
IndexUI.main()
