#Se creo un diccionario vacio para el inventario
inventario = { }

#Se crea funcion para el usuario añada productos al inventario 

def añadir_productos (nombre_producto, precio_producto,cantidad_disponible):
    if nombre_producto in inventario:
        print(f'{nombre_producto} ya existe en el inventario.')
        
    else:
        inventario[nombre_producto]= (precio_producto,cantidad_disponible)
        print(f'El producto {nombre_producto}, se añadio exitosamente.')

#Se crea funcion para e el usuario consulte la existencia de algun producto en el inventario
        
def consultar_producto (nombre_producto):
    if nombre_producto in inventario:
        precio_producto, cantidad_disponible = inventario[nombre_producto]
        print(f'PRODUCTO: {nombre_producto}\n PRECIO: {precio_producto}\n CANTIDAD: {cantidad_disponible}\n')
    else:
        print(f'Lo siento. El producto {nombre_producto} no se encuenta en el inventario.')
        
#Se crea funcion para el usuario pueda actualizar el precio del producto

def actualizar_precio (nombre_producto, precio_nuevo_producto):
    if nombre_producto in inventario:
        precio_producto, cantidad_disponible = inventario[nombre_producto]
        inventario[nombre_producto] = (precio_nuevo_producto, cantidad_disponible)
        print(f'El precio del producto {nombre_producto} se ha actualizado')
    else:
        print('Lo siento, ese producto no existe.\nIngresa uno que este disponible en el inventario.')

#Se crea una funcion para el usuario pueda eliminar productos del inventario

def eliminar_proctudo (nombre_producto):
    if nombre_producto in inventario:
        del inventario[nombre_producto]
        print(f'El producto {nombre_producto} fue eliminado exitosamente.')
    else:
        print('Lo siento, ese producto no existe.\nIngresa uno que este disponible en el inventario.')
        
# Se crea una funcion para calcular el valor total del inventario

def calcular_valor_total (inventario):
    total = sum(map(lambda item: item[0] * item[1], inventario.values()))
    print(f"Valor total del inventario: {total}")