from Request_Scrapy import Request_Scraper
from utility_functions import get_config


def main():
    """
    Programa principal
    """
    config = get_config()
    scraper = Request_Scraper(config)
    scraper.run()

if __name__ == "__main__":
    main()