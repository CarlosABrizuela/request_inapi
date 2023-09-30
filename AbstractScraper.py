from abc import ABC, abstractmethod

class AbstractScraper(ABC):
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = None

    @abstractmethod
    def fetch(self, url):
        """
        Realiza una solicitud HTTP a la URL especificada y devuelve la respuesta.
        """
        pass

    @abstractmethod
    def to_json(self):
        """
        Convierte los datos extraídos en formato JSON.
        """
    
    @abstractmethod
    def close(self):
        """
        Cerrar la sesion
        """
        pass
    
    @abstractmethod
    def run(self):
        """
        Ejecución del codigo
        """
        pass