import streamlit as st
import pandas as pd
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    def inserir():
        try:
            nome = st.text_input("Informe o nome")
            email = st.text_input("Informe o e-mail")
            fone = st.text_input("Informe o fone")
            senha = st.text_input("Informe a senha", type="password")
            if st.button("Inserir"):
                if nome or email or fone or senha == "": 
                    raise ValueError("Faltam campos a serem preenchidos")
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Conta criada com sucesso")
                time.sleep(2)
                st.rerun()
        except ValueError as e:
            print(f"Erro: {e}")
