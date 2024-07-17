import requests
from requests.auth import HTTPBasicAuth
from config import GEOSERVER_URL


def criar_estilo(usuario, senha):
    # URL do recurso
    url = f"{GEOSERVER_URL}/rest/styles.json"

    # Fazer a solicitação GET com autenticação
    response = requests.get(url, auth=HTTPBasicAuth(usuario, senha))

    # Verificar o status da resposta
    if response.status_code == 200:
        return response.content
    else:
        response.raise_for_status()
