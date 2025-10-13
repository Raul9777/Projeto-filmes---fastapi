import streamlit as st
import requests

#URL da API do FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes", page_icon = "🧨")

st.title(" Gerenciamento de filmes")

#Menu lateral sitebar
menu = st.sidebar.radio("Menu", ["Catalogo"])

if menu == "Catalogo":
    st.subheader("Todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(f" **{filme['titulo']}** ({filme('ano')}) - {filmes['genero']} - ✅")
            else:
                st.info("Nenhum filme cadastrado")
    else:
        st.error("Erro ao cadastrar com a API")
