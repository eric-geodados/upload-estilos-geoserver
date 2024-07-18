import requests
from requests.auth import HTTPBasicAuth
from config import GEOSERVER_URL
import json


def listar_workspaces(usuario, senha):
    # URL do recurso com o workspace
    url = f"{GEOSERVER_URL}/rest/workspaces/"

    # Fazer a solicitação GET
    response = requests.get(url, auth=HTTPBasicAuth(usuario, senha))

    # Transformar o retorno em JSON em bytes para uma lista com dicionários
    response_json = json.loads(response.content.decode('utf-8'))
    # Acessar os workspaces dentro da lista
    workspaces = response_json['workspaces']['workspace']
    
    nomes_workspaces = []
    # Iterar sobre a lista de workspaces
    for workspace in workspaces:
        nomes_workspaces.append(workspace['name'])
    return nomes_workspaces


def criar_estilo(usuario, senha, workspace, caminho_arquivo):
    # URL do recurso com o workspace
    url = f"{GEOSERVER_URL}/rest/workspaces/{workspace}/styles"

    # Abrindo o arquivo zip em modo binário
    with open(caminho_arquivo, 'rb') as arquivo:
        # Definindo o cabeçalho
        header = {
            'Content-type': 'application/zip'
        }

        # Fazendo a solicitação POST
        response = requests.post(url, headers=header, data=arquivo, auth=HTTPBasicAuth(usuario, senha))

    # Verificando a resposta
    if response.status_code == 201:
        return 'Estilo carregado com sucesso!'
    else:
        return (f'Erro ao carregar estilo: {response.status_code}', response.text)

# c = r'C:\Users\eric_cabral\Downloads\obras_publicas.zip'
# workspace = 'UbaC4764'
# final = criar_estilo('admin', 'geodados', workspace, c)
# print(final)
