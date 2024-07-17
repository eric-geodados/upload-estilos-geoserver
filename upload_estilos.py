import requests
from requests.auth import HTTPBasicAuth
from config import GEOSERVER_URL, GEOSERVER_USUARIO, GEOSERVER_SENHA


def criar_estilo():
    # URL do recurso
    url = f"{GEOSERVER_URL}/rest/styles.json"

    # Fazer a solicitação GET com autenticação
    response = requests.get(url, auth=HTTPBasicAuth(GEOSERVER_USUARIO, GEOSERVER_SENHA))

    # Verificar o status da resposta
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
