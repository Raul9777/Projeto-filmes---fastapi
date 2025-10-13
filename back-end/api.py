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

@app.get("/filmes")
def catalogo():
    filmes = funcao.listar_movies()
    lista = []
    for filme in filmes:
        lista.append({ "id":filme[0],
                      "titulo":filme[1],
                      "genero":filme[2],
                      "ano":filme[3],
                      "avaliacao":filme[4]
                    })
    return{"filmes": lista}