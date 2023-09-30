import yaml

def get_registros(config):
    """
    Abre el archivo con la lista de numeros de registro y la devuelve
    """
    ruta_full = config['register_list_dir'] + config['registers_list_file_name']
    try:
        with open(ruta_full) as f_registros:
            lista_registros = f_registros.read().split("\n")
            return lista_registros
    except FileNotFoundError as e:
        print(f"El archivo no se encontró. {e.filename}")
        return []

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
        config['register_list_dir']= ''
        config['numero_hilos']= 1
        config['delay_intentos']= 0
        config['max_intentos']= 1
        return config
    
# print(get_registros(get_config()))