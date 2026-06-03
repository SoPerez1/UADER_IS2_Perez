import json
import sys


class JSONReader:
    """Singleton simple para leer valores desde un archivo JSON.

    La primera instancia creada establece el archivo JSON a usar. Las
    llamadas posteriores retornan la misma instancia (patrón singleton).
    """

    _instance = None

    def __new__(cls, archivo_json: str = None):
        if cls._instance is None:
            cls._instance = super(JSONReader, cls).__new__(cls)
            cls._instance.archivo_json = archivo_json
        return cls._instance

    def __init__(self, archivo_json: str = None):
        if archivo_json is not None:
            self.archivo_json = archivo_json

    def obtener_valor(self, clave: str = 'token1') -> str:
        """Recupera el valor asociado a una clave dentro del archivo JSON."""
        with open(self.archivo_json, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

        if clave in datos:
            return str(datos[clave])

        return f'La clave "{clave}" no existe en el archivo JSON.'

#implementacion inciso d: capa de abstraccion (branching by abstraction)
def proveedor_de_datos(archivo: str, clave: str, usar_nueva_version: bool = True) -> str:
    """Capa intermedia que abstrae la implementación del lector.

    Permite convivir con la versión vieja (procedural) y la nueva (Singleton)
    según se requiera para la migración.
    """
    if usar_nueva_version:
        reader = JSONReader(archivo)
        return reader.obtener_valor(clave)
    else:
       
        with open(archivo, 'r', encoding='utf-8') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        return str(obj[clave])


def main(argv=None):
    """Punto de entrada que usa la abstracción para obtener el valor."""
    argv = argv if argv is not None else sys.argv

    if len(argv) < 2:
        print("Error de programa controlado: Falta el argumento del archivo JSON.")
        print("Uso: python getJason.py <archivo_json> [clave]")
        sys.exit(1)

    jsonfile = argv[1]
    jsonkey = argv[2] if len(argv) > 2 else 'token1'

    try:
        resultado = proveedor_de_datos(jsonfile, jsonkey, usar_nueva_version=True)
        print(resultado)
        
    except FileNotFoundError:
        print(f"Error de programa controlado: El archivo '{jsonfile}' no existe.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error de programa controlado: El archivo '{jsonfile}' no tiene un formato JSON válido.")
        sys.exit(1)
    except KeyError:
        print(f"Error de programa controlado: La clave '{jsonkey}' no existe en el archivo JSON.")
        sys.exit(1)
    except Exception as e:
        print(f"Error de programa controlado inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()