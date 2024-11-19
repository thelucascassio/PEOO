import streamlit as st
from manterClienteUI import ManterClienteUI
class IndexUI:
    def main():
        st.title("Bem-vindo ao cadastro de clientes!")
        if st.button("Começar cadastro"):
            ManterClienteUI.main()
IndexUI.main()
