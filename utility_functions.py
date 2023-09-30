import yaml

def get_config():
    """
    Obtiene los datos de configuracion del archivo /file/config.yml
    """
    try:
        with open("config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)
            config["output"] = config["output_dir"] + config["output_file_name"] + ".json"
            return config
    except FileNotFoundError as e:
        print(f"El archivo no se encontró. {e.filename}")
        config = {}
        config["output"]= "salida.json"
        config["base_url"]= "https://ion.inapi.cl"
        config['url_busca_marca']= "/Marca/BuscarMarca.aspx/FindMarcas"
        config['url_busca_por_solicitud']= "/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud"
        config["proxy_ip_port"] = None
        return config
    