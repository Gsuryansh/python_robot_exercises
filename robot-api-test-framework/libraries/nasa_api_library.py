import requests
import json
import os


class NasaApiLibrary:
    def __init__(self, config_file='config/config.json'):
        config_path = os.path.join(os.path.dirname(__file__), '..', config_file)
        with open(config_path, 'r') as file:
            config = json.load(file)
        self.base_url = config.get('base_url')

    def get_data(self, params=None):
        response = requests.get(f"{self.base_url}", params=params)
        response.raise_for_status()
        return response.status_code, response.json()