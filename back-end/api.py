from fastapi import FastAPI
import funcao

#Roda fastapi = python -m uvicorn api:app --reload

#Testar as rotas do fastapi
#/docs > documentação Swagger
#/redot > Documentação Redoc

app = FastAPI(title = "Gerenciador de Filmes")

#GET > Pegar/Listar
#POST > Enviar/adastrar
#PUT > Atulizar
#DELETE > Deletar

#API sempre retorn dados em JSON (Chave: Valor)
@app.get("/")
def home():
    return {
        "Mensagem": "Bem-vindo ao gerenciador de filmes"
        }