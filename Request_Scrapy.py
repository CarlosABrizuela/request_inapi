import json
import requests
import time
from AbstractScraper import AbstractScraper
from requests.exceptions import ProxyError
import concurrent.futures

class Request_Scraper(AbstractScraper):
    def __init__(self, config):
        """Inicia el Scraper

        Args:
            config (dict): contiene las configuraciones: proxy, proxy_ip_port, output
        """
        self.config = config
        super().__init__(self.config['base_url'])
        self.data = []
        self.actual_register = None
        self.session = requests.Session()
        if self.config['proxy']:
            self.session.proxies = config['proxy_ip_port']

    def fetch(self, url, payload):
        """
        Realiza una solicitud HTTP a la URL especificada y devuelve la respuesta en formato json.
        """
        max_intentos = self.config['max_intentos'] 
        delay_intentos = self.config['delay_intentos']
        intentos = 0

        while intentos < max_intentos:
            try:
                response = self.session.post(self.full_url(url), json=payload)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Error en la solicitud. Código de estado: {response.status_code}. Reintentando...")

            except ProxyError as e:
                print('Error de proxy:', e)
                return None
            except requests.RequestException as e:
                print(f"Error de solicitud: {e}. Reintentando...")

            intentos += 1
            time.sleep(delay_intentos)

        print(f"No se pudo hacer el request a: {url}. Fin de intentos")
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
        with open(self.config["output"], 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, indent=4, ensure_ascii=False)
            print(f"Se guardaron los datos en: {self.config['output']}")

    def close(self):
        """
        Cerrar la sesion
        """
        self.session.close()
    
    def run(self, lista_registros):
        """
        Ejecución del codigo
        args:
            lista_registros (list): lista de los registros. 
        """
        def run_registro(registro):
            self.actual_register = registro
            self.buscar_marcas()
            
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.config['numero_hilos']) as executor:
            executor.map(run_registro, lista_registros)

        self.to_json()
        self.close()
    
    
    def buscar_marcas(self):
        """
        busca las marcas para el numero de registro actual
        """
        print(f"Registro: {self.actual_register}")
        payload = {
            "LastNumSol": 0,
            "Hash": "",
            "IDW": "",
            "responseCaptcha": "este texto no se validará",
            "param1": "",
            "param2": self.actual_register,
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
        response = self.fetch(self.config['url_busca_marca'], payload)
        
        if(response):
            response_dict = json.loads(response['d'])
            hash = response_dict['Hash']
            marcas = response_dict['Marcas']
            self.busca_marca_por_solicitud(marcas, hash) #siguiente método

    def busca_marca_por_solicitud(self, marcas, hash):
        """
        obtiene para cada marca el detalle
        """
        for marca in marcas:
            payload = {
                "Hash": hash,
                "IDW": "",
                "numeroSolicitud": marca['id']
            }
            response = self.fetch(self.config['url_busca_por_solicitud'], payload)
            if(response):
                response_dict = json.loads(response['d'])
                instancias = response_dict['Marca']['Instancias']
                lista_instancias = []
                for instancia in instancias:
                    instancia_dict = {}
                    # Observada de fondo y fecha de observada de fondo
                    subtobservada = "Resolución de observaciones de fondo de marca"
                    observada_de_fondo = True if instancia['EstadoDescripcion'].count(subtobservada)>0 else False
                    fecha_observada_de_fondo = instancia['Fecha'] if observada_de_fondo else None
                    # Apelaciones
                    subtapelaciones = "Recurso de apelacion"
                    apelaciones = True if instancia['EstadoDescripcion'].count(subtapelaciones)>0 else False
                    # IPT e IPTV
                    subtIPT = "IPT"
                    ipt = True if instancia['EstadoDescripcion'].count(subtIPT)>0 else False
                    ## Crear un objeto con los valores
                    instancia_dict["Observada_de_fondo"]= observada_de_fondo
                    instancia_dict["Fecha_observada_de_fondo"]= fecha_observada_de_fondo
                    instancia_dict["Apelaciones"]= apelaciones
                    instancia_dict["IPT"]= ipt
                    lista_instancias.append(instancia_dict)

                registro = {}
                registro["registro"]= self.actual_register
                registro["instancias"]= lista_instancias
                self.data.append(registro)
