import requests
from requests.auth import HTTPBasicAuth
from config import GEOSERVER_URL


def criar_estilo(usuario, senha, caminho_arquivo):
    # URL do recurso
    url = f"{GEOSERVER_URL}/rest/styles.json"

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
        
c = r'C:\Users\eric_cabral\Downloads\obras_publicas.zip'
final = criar_estilo('admin', 'geodados', c)
print(final)
