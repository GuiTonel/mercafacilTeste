# mercafacilTeste
Solução desenvolvida em Python 3.9 com a ferramente Flask e SQLAlchemy para o banco de dados

## Para rodar o projeto
`pip install requirements.txt`
`python server.py`

### ou
`docker-compose up --build`

## Rotas Disponives
- /v1/users/:user_id
Para autenticação

- /v1/contacts/
Para cadastro dos contatos, contendo assim no Header Authentication o token obtido na rota acima.

### Necessário cadastrar os 2 usuarios ( Macapa e Varejao ) na tabela "usuario" do banco de dados "mercafacil"
