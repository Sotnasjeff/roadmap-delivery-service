import requests
from flask import current_app

class BrasilApiClient:
    def get_cep(cep: int):
        api_url = current_app.config['BRASIL_API_URI']
        response = requests.get(f'{api_url}{cep}')
        response.raise_for_status()
        return response.json()