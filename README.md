# mercafacilTeste
Solução desenvolvida em Python 3.9 com a ferramente Flask e SQLAlchemy para o banco de dados

## Para rodar o projeto
`pip install requirements.txt`
`python server.py`

## Rotas Disponives
- /v1/users/:user_id
Para autenticação

- /v1/contacts/
Para cadastro dos contatos, contendo assim no Header Authentication o token obtido na rota acima.
