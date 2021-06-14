import sys
import model
import view

def validacion_de_pedido(numero_mesa, pedidos: dict): #con esta funcion validamos si hay pedido en esa mesa. 
    for mesa  in pedidos.keys():
        if str(numero_mesa) == mesa:
            return False
    return True


#pedidos = model.read()
main = True

while main == True:
    
    opcion = view.menu_principal()
    pedidos = model.read()
    
    if opcion == 1:
        numero_mesa = view.indentificador()
        
        if validacion_de_pedido(numero_mesa, pedidos) :
            pedido_nuevo, numero_mesa = view.formulario_realizar_pedido(numero_mesa)
            pedidos[numero_mesa] = pedido_nuevo
            model.write(pedidos)
        else:
            view.mensaje(f"la mesa {numero_mesa} ya tiene orden asignada")

    elif opcion == 2:
        
        numero_mesa = view.indentificador()
        if validacion_de_pedido(numero_mesa, pedidos) :
            view.mensaje("no hay pedido para esa mesa")
        else:    
            view.formulario_ver_pedido(pedidos, numero_mesa)

    elif opcion == 3:
        numero_mesa =  view.indentificador()
        if validacion_de_pedido(numero_mesa, pedidos) :
            view.mensaje("no hay pedido para esa mesa")
        else:
            lista_opciones_pedidos = [ "sopas", "principio", "carne", "ensalada", "jugo"]    
            opcion_modificar, cantidad_actualizada = view.fornulario_moficar_pedido(lista_opciones_pedidos)
            pedidos = model.update(pedidos, numero_mesa,lista_opciones_pedidos[opcion_modificar - 1], cantidad_actualizada)
            model.write(pedidos)
    elif opcion == 4:
        numero_mesa  = view.indentificador()
        if validacion_de_pedido(numero_mesa, pedidos) :
            view.mensaje("no hay pedido para esa mesa")
        else:
            view.mensaje( f"eliminando pedido de mesa:  {numero_mesa}")
            pedidos = model.delete(pedidos, numero_mesa)
            model.write(pedidos)
    elif opcion == 5:
        print(pedidos)

    elif opcion == 0:
        sys.exit(1)