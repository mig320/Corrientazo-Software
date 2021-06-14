def indentificador():
    numero_mesa = int(input("digite el numero de mesa: "))
    return numero_mesa



def mensaje(mensaje: str):
    print(mensaje)





def opciones_pedido(): #define las opcione para hacer pedido.
    print("1. Sopa")
    print("2. Principio")
    print("3. Carne")
    print("4. Ensalada")
    print("5. Jugo")

def menu_principal():
    print("1. Realizar pedido")
    print("2. Ver pedido")
    print("3. Modificar pedido")
    print("4. Eliminar pedido")
    print("5. Ver todos los  pedidos")

    opcion = None
    
    while opcion == None:
        try:
            opcion = int(input("Ingrese una opción: "))
        except:        
            print("Entrada inválida: Se debe ingresar una opción numérica.")    

    #Retornar opción al controlador
    return opcion



   
def formulario_realizar_pedido(numero_mesa):
    datos = None
    while datos == None:
        try: #verificamos que todos los datos sean correctos.
            numero_de_mesa = numero_mesa
            sopas  = int(input("digite cuantas sopas desean: "))
            principio = int(input("digite cuantos principios: "))
            carne = int(input("digite cuntas carnes desea: "))
            ensalada = int(input("digite cuantas ensaladas solicitan: "))
            jugo = int(input("digite la cantidad de jugos que necesitan: "))
            datos  = True #si todo los datos son correctos datos cambia y continuamos con la ejecucion.
        except:
            print("alguno de los datos antaeriores es incorrecto") 
    
    ########## se agrega toda la informacion en un dicionario #######
    pedido = {
        "numero mesa" : numero_de_mesa,
        "sopas": sopas,
        "principio": principio,
        "carne"  : carne,
        "ensalada" : ensalada,
        "jugo" : jugo
        } 
    return pedido, numero_de_mesa


################## se busca ver el estado del pedido ##############
def formulario_ver_pedido(pedidos, numero_mesa):
    print(pedidos[str(numero_mesa)])


def fornulario_moficar_pedido(opciones_pedido_menu : list):
    
    print("elementos a modificar")
    opciones_pedido()
    opcion_pedido = int(input("digite el plato del pedido que desea modificar"))
    cantidad_actulizada = int(input("digite la cantidad de" + opciones_pedido_menu[opcion_pedido - 1 ] + " a modificar:"))

    return opcion_pedido, cantidad_actulizada

    
#def formulario_modificar_pedido(pedidos: dict ) -> dict:
   # numero_mesa = int(input("digite el numero de la mesa para modificar el pedido"))




#numero_mesa()
