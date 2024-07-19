import requests
from requests.auth import HTTPBasicAuth
from config import GEOSERVER_URL
import json
from tkinter import messagebox


def validar_login(usuario, senha):
    url = f"{GEOSERVER_URL}/rest/workspaces/"

    response = requests.get(url, auth=HTTPBasicAuth(usuario, senha))
    
    if response.status_code == 200:
        return True
    else:
        return False
    

def listar_workspaces(usuario, senha):
    # URL do recurso com o workspace
    url = f"{GEOSERVER_URL}/rest/workspaces/"

    # Fazer a solicitação GET
    response = requests.get(url, auth=HTTPBasicAuth(usuario, senha))

    # Transformar o retorno em JSON em bytes para uma lista com dicionários
    response_json = json.loads(response.content.decode('utf-8'))
    # Acessar os workspaces dentro da lista
    workspaces = response_json['workspaces']['workspace']
    
    workspaces_excluir = ['cite', 'it.geosolutions', 'nurc', 'sde', 'sf', 'tiger', 'topp']
    
    nomes_workspaces = []
    # Iterar sobre a lista de workspaces
    for workspace in workspaces:
        if workspace['name'] not in workspaces_excluir:
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

    print(response.status_code)
    if response.status_code == 201:
        return True
    else:
        return False
