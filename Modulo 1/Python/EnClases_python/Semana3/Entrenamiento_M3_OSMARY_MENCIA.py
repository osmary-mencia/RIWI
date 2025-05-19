#Se crea el inventario vacio como diccionario para almacenar los datos ingresados
inventario = {}


#Se crea el menu con las opciones 
def menu():
    
    while True:
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("\n🌸  ＷＥＬＣＯＭＥ   ＴＯ   ＯＳＭＡＲＹ'Ｓ   ＳＨＯＰ 🌸 \n")
        
        print('             ⡷⠂𝙶𝙴𝚂𝚃𝙾𝚁 𝙳𝙴 𝙸𝙽𝚅𝙴𝙽𝚃𝙰𝚃𝙸𝙾⠐⢾\n')
        
        print('1. Añadir un producto.')
        print('2. Consultar un producto.')
        print('3. Cambiar precio de un producto.')
        print('4. Eliminar un producto.')
        print('5. Ver el inventario.')
        print('6. Calcular valor total del inventario.')
        print('0. Salir.\n')
        
#Se define la variable que le da la opcion al usuario de elegir una opcion del menu
        opcion = input('Ingresa una opcion numerica del menu: ')
                
#Se crea una condicion para validar la entrada de datos del menu
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            consultar_producto()
        elif opcion == '3':
            cambiar_precio()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            mostrar_inventario()
        elif opcion == '6':
            calcular_valorTotal_inventario()
        elif opcion == '0':
            print('\nミ💖 Hasta la proxima 💖 彡')
            print('Fin del programa.')
            break
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('¡¡ERROR!!')
            print('\nOpcion invalida. Elige una opcion numerica que este en el menu.\n')
            
#------------------------------------------------------------------------------------------------
#Se crea funcion para la opcion de agregar producto
def agregar_producto():
    
    #Se le pide al usuario que ingrese el nombre del producto
    nombre_producto = input('\nIngresa el nombre del producto: ').strip().upper()
    
    #Se valida que el producto no exista en el inventario
    if nombre_producto in inventario:
        print('\nEste producto ya existe en el inventario.')
        return 
    
    #Si existe el producto entonces se valida la entrada para del precio y cantidad
    try:
        precio_producto = float(input('PRECIO: '))
        if precio_producto < 0:
            print('\nEl precio no puede ser negativo.')
            return
        cantidad_producto = int(input('CANTIDAD: '))
        if cantidad_producto < 0:
            print('\nLa cantidad no puede ser negativa.')
            return
    except ValueError:
        print('\nEntrada inválida. Debes ingresar números.')
        return

#se almacena el preducto en el inventario y le retornamos un mensaje al usuario
    inventario[nombre_producto] = (precio_producto, cantidad_producto)
    print("Producto agregado correctamente.")

#------------------------------------------------------------------------------------------------
#Se crea funcion para la opcion de consultar un producto
def consultar_producto():
    
    nombre_producto = input('\nIngresa el nombre del producto que deseas buscar: ').strip().upper()
    producto = inventario.get(nombre_producto)
    
    if producto:
        print(f'\n PRODUCTO: {nombre_producto}\n PRECIO: {producto[0]:.2f}\n CANTIDAD: {producto[1]}')
    else:
        print(f'\nEl producto {nombre_producto} no existe en el inventario.')

#------------------------------------------------------------------------------------------------
#Se crea funcion para cambiar el precio de un producto
def cambiar_precio():
    #Le pedimos al usuario que ingrese el nombre del producto al que le quiere cambiar el nombre
    nombre_producto = input('\nIngresa el nombre del producto que deseas modificarle el precio: ').strip().upper()
    
    # verificamos que el nombre se encuentre en el inventario para poder cambiarle el precio
    if nombre_producto in inventario:
        try:
            nuevo_precio = float(input('Ingresa el nuevo precio: '))
            
            #Si el usuario ingresa un numero negativo le retornamos un mensaje de error.
            if nuevo_precio < 0:
                print('\n¡¡ERROR!! El precio no puede ser negativo.')
                return
            #Si usuario ingresda letras en el precio le retornamos error
        except ValueError:
            print('\nEntrada inválida. Debes ingresar un número.')
            return

#actualizamos el precio del producto
        cantidad_actual = inventario[nombre_producto][1]
        inventario[nombre_producto] = (nuevo_precio, cantidad_actual)
        print('\nPrecio actualizado.')
        
#Si no esta el retornamos un mesaje que el producto no se encuentra en el inventario
    else:
        print('\nLO SIENTO! Este producto no existe en el inventario')
        
#------------------------------------------------------------------------------------------------
#Se crea funcion para eliminar el producto que el usuario desee
def eliminar_producto():
    #le pedimos al usuario el nombre del producto
    nombre_producto = input("\nIngresa el nombre del producto a eliminar: ").strip().upper()
    
    #verificamos que el producto este en el inventario
    if nombre_producto in inventario:
        del inventario[nombre_producto]
        print('\nEl producto se elimino del inventario.')
    #Si no esta le retornamos un mesaje
    else:
        print('\nEste producto no existe en el invetario')

#------------------------------------------------------------------------------------------------
#Se crea funcion para mostar todo el inventario
def mostrar_inventario():
    
#si no se ha ingresado nada y el usuario quiere ir el inventario re retorna un mensaje 
    if not inventario:
        print('\nEl inventario está vacío.')
    
#si se valida que si hay productos en el inventario lo mostramos
    else:
        print('\nLista del inventario:\n')
        for nombre_producto, (precio_producto, cantidad_producto) in inventario.items():
            print(f'{nombre_producto}: ${precio_producto:.2f} | Cantidad: {cantidad_producto}')
#---------------------------------------------------------------------------------------------------

#Se crea funcion para calcular el valor total de los productos del inventario            
def calcular_valorTotal_inventario():
    if not inventario:
        print('El inventario está vacío.')
    else:
        total = lambda: sum(precio * cantidad for nombre, (precio, cantidad) in inventario.items())
        print(f"\nEl valor total del inventario es: ${total():.2f}")

menu()