import requests
import jsonpath

# GET Avaliacoes
headers = {"Authorization": "Token f9b7a4f4608837a7007cecef8d3c9793df0188fa"}
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/cursos/',headers=headers)

resultados = jsonpath.jsonpath(avaliacoes.json(),'results')
resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacoes')