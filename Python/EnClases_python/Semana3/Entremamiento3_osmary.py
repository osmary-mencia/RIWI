#Se crea el inventario vacio como dict que va almacenar los datos ingresados
inventario = {}

#Se crea el menu con las opciones 
def menu():
    
    while True:
        print("\n🌸  ＷＥＬＣＯＭＥ   ＴＯ   ＯＳＭＡＲＹ'Ｓ   ＳＨＯＰ 🌸 \n")
        
        print('             ⡷⠂𝙶𝙴𝚂𝚃𝙾𝚁 𝙳𝙴 𝙸𝙽𝚅𝙴𝙽𝚃𝙰𝚃𝙸𝙾⠐⢾\n')
        
        print('1. Añadir un producto.')
        print('2. Consultar un producto.')
        print('3. Cambiar precio de un producto.')
        print('4. Eliminar un producto.')
        print('5. Ver el inventario.')
        print('6. Calcular valor total del inventario.')
        print('0. Salir.\n')
        
#Se define la variable que le da la opcion al usuario de elegir una opcion
        opcion = input('Ingresa una opcion numerica del menu del: ')

#Se crea una condicion para validar la entrada de datos 
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            consultar_producto()
        elif opcion == '3':
            cambiar_precio()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            calcular_valorTotal_inventario()
        elif opcion == '6':
            mostrar_inventario()
        elif opcion == '0':
            print('\nミ💖 Hasta la proxima 💖 彡')
            print('Fin del programa.')
            break
        else:
            print('Opcion invalida. Elige una Opcion que este en el menu.')

#Se crea funcion para almacenar 
def agregar_producto():
    nombre_producto = input('Ingresa el nombre del producto: ').strip()
    if nombre_producto in inventario:
        print('Este producto ya existe en el inventario.')
        return 
    
    try:
        precio_producto = float(input('El precio es: '))
        if precio_producto < 0:
            print('El precio no puede ser negativo.')
            return
        cantidad_producto = int(input('La cantidad es: '))
        if cantidad_producto < 0:
            print('La cantidad no puede ser negativa.')
            return
    except ValueError:
        print('Entrada inválida. Debes ingresar números.')
        return

    inventario[nombre_producto] = (precio_producto, cantidad_producto)
    print("Producto agregado correctamente.")

def consultar_producto():
    nombre_producto = input('Ingresa el nombre del producto que deseas buscar: ').strip()
    producto = inventario.get(nombre_producto)
    if producto:
        print(f'El producto es: {nombre_producto}\n El precio del producto es: {producto[0]:.2f}\n La cantidad del producto es: {producto[1]}')
    else:
        print(f"El producto {nombre_producto} no existe en el inventario.")

def cambiar_precio():
    nombre_producto = input('Ingresa el nombre del producto que deseas modificarle el precio: ').strip()
    if nombre_producto in inventario:
        try:
            nuevo_precio = float(input('Ingresa el nuevo precio: '))
            if nuevo_precio < 0:
                print('El precio no puede ser negativo.')
                return
        except ValueError:
            print('Entrada inválida. Debes ingresar un número.')
            return

        cantidad_actual = inventario[nombre_producto][1]
        inventario[nombre_producto] = (nuevo_precio, cantidad_actual)
        print('Precio actualizado.')
    else:
        print('El producto no existe en el inventario')

def eliminar_producto():
    nombre_producto = input("Ingresa el producto a eliminar: ").strip()
    if nombre_producto in inventario:
        del inventario[nombre_producto]
        print('El producto se elimino del inventario.')
    else:
        print('Este producto no existe')

def calcular_valorTotal_inventario():
    total = sum(precio * cantidad for precio, cantidad in inventario.values())
    print(f"El valor total del inventario es: ${total:.2f}")

def mostrar_inventario():
    if not inventario:
        print('El inventario está vacío.')
    else:
        print('\nLista del inventario:')
        for nombre_producto, (precio_producto, cantidad_producto) in inventario.items():
            print(f'{nombre_producto}: ${precio_producto:.2f} | Cantidad: {cantidad_producto}')

menu()