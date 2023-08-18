import requests

# GET Avaliacoes
headers = {"Authorization": "Token f9b7a4f4608837a7007cecef8d3c9793df0188fa"}
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/cursos/',headers=headers)

# Acessando o código de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json())

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando proxima pagina
# print(avaliacoes.json()['next'])

### manipulação básica de variáveis de coleção aninhada