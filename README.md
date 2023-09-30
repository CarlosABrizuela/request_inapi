# Request Inapi
Test challenge de scraping de la pagina inapi. para AUTOscraping.
Para el Challenge se usó Python 3.11.5, y la librería requests.
El objetivo es obtener los datos para una lista de numeros de registros en la página de búsqueda, 
una vez obtenidos de estos analizamos solo las instancias administrativas, para luego armar un
fichero .json de salida. 
Formato de salida:
```json
[{
        {"registro": NRO_REGISTRO, 
        "instancias": [
            {
                "Observada_de_fondo": True/False, 
                "Fecha_observada_de_fondo": Fecha, 
                "Apelaciones": True/False, 
                "IPT": True/False
            }, 
            "..."
            ]},
        {"..."},"..."
}]
```
La configuración del crawler se realiza mediante un fichero ubicado en la carpeta raíz "config.yaml".
Con los siguientes valores:
```yaml
base_url: https://ion.inapi.cl  #La url de inapi
url_busca_marca: /Marca/BuscarMarca.aspx/FindMarcas #url para la búsqueda de las marcas
url_busca_por_solicitud: /Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud #url para buscar por nro de solicitud
proxy: False    # true/false segun se use o no proxies
proxy_ip_port:  # proxy:puerto. Ejemplo:  37.19.220.129:8443
output_file_name: salida    #nombre del fichero de salida sin extensión
output_dir: C:/Users/LNKIZ/Desktop/Test python/proyecto/request_inapi/files/   #carpeta del fichero de salida
registers_list_file_name: register_number_list.txt      #nombre del fichero con la lista de nro de registro con extensión
register_list_dir: C:/Users/LNKIZ/Desktop/Test python/proyecto/request_inapi/files/  # Carpeta donde se encuentra el fichero con la lista
numero_hilos: 5     # Número de hilos para el procesamiento en paralelo
max_intentos: 3     # Cantidad de intentos máximos en cada fetch
delay_intentos: 5   # El tiempo de espera en segundos entre cada intento fallido
```

## Bibliotecas utilizadas

- [requests](https://requests.readthedocs.io/): Se utiliza para hacer solicitudes http.
- [PyYAML](https://pyyaml.org/): Se utiliza para manejar la configuración del scraper en un archivo YAML.

## Clona el proyecto
- git clone https://github.com/CarlosABrizuela/request_inapi.git
- cd scraping-proyecto

## Instala las bibliotecas requeridas
- pip install -r requirements.txt

## Uso del scraper
- python main.py

## Licencia
- Sin Licencia

