import streamlit as st
import requests

#URL da API do FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes", page_icon = "🧨")

st.title(" Gerenciamento de filmes")

#Menu lateral sitebar
menu = st.sidebar.radio("Menu", ["Catalogo", "Adicionar Filme", "Atualizar Filme"])

if menu == "Catalogo":
    st.subheader("Todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(f" **{filme['titulo']}** ({filme['ano']}) - {filme['genero']}")
        else:
                st.info("Nenhum filme cadastrado")
    else:
        st.error("Erro ao cadastrar com a API")
elif menu == "Adicionar Filme":
     st.subheader("Adicionar Filme")
     titulo = st.text_input("Título do Filme")
     genero = st.text_input("Gênero do Filme")
     Ano = st.number_input("Ano de Lançamento", min_value=1900, max_value=2100, step=1)
     Avaliacao = st.number_input("Avaliação de (0 a 10)",min_value=0, max_value=10, step=1)

     if st.button("Salvar Filme"):
          params = {"titulo":titulo, "genero":genero, "ano":Ano, "avaliacao": Avaliacao}
          response = requests.post(f"{API_URL}/filmes", params=params)
          if response.status_code == 200:
               st.success("Filme adicionado com sucesso")
          else:
               st.error("Erro ao adicionar o filme")
elif menu == "Atualizar Filme":
    st.subheader("Atualizar Filme")

    titulo_original = st.text_input("Título Original do Filme (que será atualizado)")

    novo_titulo = st.text_input("Novo Título do Filme")
    genero = st.text_input("Novo Gênero do Filme")
    ano = st.number_input("Novo Ano de Lançamento", min_value=1900, max_value=2100, step=1)
    avaliacao = st.number_input("Nova Avaliação de (0 a 10)", min_value=0, max_value=10, step=1)

    if st.button("Atualizar Filme"):
        params = {
            "titulo": novo_titulo,
            "genero": genero,
            "ano": ano,
            "avaliacao": avaliacao
        }

        response = requests.put(f"{API_URL}/filmes/{titulo_original}", params=params)
        if response.status_code == 200:
            st.success("Filme atualizado com sucesso")
        else:
             st.error("Erro ao atuliazar o filme")
            

