import json

def create(pedidos, indicador, pedido):
    pedidos[indicador] = pedido

def read(rutaArchivo: str = 'datos.json'):
    dicionario_pedidos = {}
    try:
        with open(rutaArchivo) as archivo:
            dicionario_pedidos = json.load(archivo)
    except:
        print("no se pudo abrir el archivo")
        return False
        

    return dicionario_pedidos


def write(pedidos , ruta_archivo = "datos.json"):
    try:
        with open(ruta_archivo, 'w') as archivo_json:
            json.dump(pedidos, archivo_json)
    except:
        print("error no se pudo cargar la orden  al archivo")
        return False
    return True

def update(pedidos,numero_mesa ,opcion_modificar, cantidas_actulizada ):
    pedidos[str(numero_mesa)][opcion_modificar] = cantidas_actulizada
    return pedidos

def delete(pedidos,numero_mesa):
    pedidos.pop(str(numero_mesa))
    return pedidos


print("hola soy miguel")
print("hola agregue una nueva linea aqui")
print("otra linea nueva aqui")
