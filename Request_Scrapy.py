import requests
from AbstractScraper import AbstractScraper

class Request_Scraper(AbstractScraper):
    def __init__(self, config):
        self.config = config
        super().__init__(self.config['base_url'])
        self.data = []
        self.actual_register = None
        self.session = requests.Session()
        if self.config['proxy']:
            self.session.proxies = config['proxy_ip_port']

    def fetch(self, url, payload):
        """
        Realiza una solicitud HTTP a la URL especificada y devuelve la respuesta.
        """
        response = self.session.post(self.full_url(url), json=payload)
        if response.status_code == 200:
            return response.json()
        print(f"Error en la solicitud. Código de estado: {response.status_code}")
        return None

    def full_url(self, url):
        """
        devuleve la url completa
        """
        return self.base_url + url

    def to_json(self):
        """
        Convierte los datos extraídos en formato JSON.
        """
        pass

    def close(self):
        """
        Cerrar la sesion
        """
        self.session.close()
    
    def run(self):
        """
        Ejecución del codigo
        """
        payload_busca_marca = {
            "LastNumSol": 0,
            "Hash": "",
            "IDW": "",
            "responseCaptcha": "este texto no se validará",
            "param1": "",
            "param2": "1236227",
            "param3": "",
            "param4": "",
            "param5": "",
            "param6": "",
            "param7": "",
            "param8": "",
            "param9": "",
            "param10": "",
            "param11": "",
            "param12": "",
            "param13": "",
            "param14": "",
            "param15": "",
            "param16": "",
            "param17": "1",
        }
        print(self.fetch(self.config['url_busca_marca'], payload_busca_marca))
        self.close()
