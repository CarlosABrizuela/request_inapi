from Request_Scrapy import Request_Scraper
from utility_functions import get_config, get_registros


def main():
    """
    Programa principal
    """
    print("Inicio")
    config = get_config()
    lista_registros = get_registros(config)
    scraper = Request_Scraper(config)
    scraper.run(lista_registros)
    print("Fin")

if __name__ == "__main__":
    main()