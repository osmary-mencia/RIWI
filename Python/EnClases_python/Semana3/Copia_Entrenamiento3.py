# Diccionario vacío para almacenar el inventario
inventario = {}

# Función lambda para calcular el valor total del inventario
calcular_valor_total = lambda inv: sum(info["precio"] * info["cantidad"] for info in inv.values())

# Menú principal del programa
def menu():
    while True:
        print('\n🌸  ＷＥＬＣＯＭＥ   ＴＯ   ＯＳＭＡＲＹ\'Ｓ   ＳＨＯＰ 🌸')
        print('\n             ⡷⠂𝙶𝙴𝚂𝚃𝙾𝚁 𝙳𝙴 𝙸𝙽𝚅𝙴𝙽𝚃𝙰𝚁𝙸𝙾⠐⢾\n')
        print('1. Añadir un producto')
        print('2. Consultar un producto')
        print('3. Cambiar precio de un producto')
        print('4. Eliminar un producto')
        print('5. Ver el inventario')
        print('6. Calcular valor total del inventario')
        print('0. Salir\n')

        opcion = input('Elige una opción del menú: ').strip()

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
            print('\nミ💖 Hasta la próxima 💖 彡')
            break
        else:
            print('❌ Opción inválida. Elige una opción válida del menú.')

# Agregar un producto al inventario
def agregar_producto():
    nombre = input('\nNombre del producto: ').strip().upper()
    if not nombre:
        print('⚠️ El nombre no puede estar vacío.')
        return

    if nombre in inventario:
        print('⚠️ Este producto ya existe.')
        return

    try:
        precio = float(input('Precio: '))
        if precio < 0:
            print('⚠️ El precio no puede ser negativo.')
            return
        cantidad = int(input('Cantidad: '))
        if cantidad < 0:
            print('⚠️ La cantidad no puede ser negativa.')
            return
    except ValueError:
        print('⚠️ Entrada inválida. Usa números para precio y cantidad.')
        return

    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print('✅ Producto agregado correctamente.')

# Consultar un producto por nombre
def consultar_producto():
    nombre = input('\nNombre del producto a consultar: ').strip().upper()
    producto = inventario.get(nombre)

    if producto:
        print(f"\n📦 {nombre} → Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")
    else:
        print('❌ El producto no existe en el inventario.')

# Cambiar el precio de un producto existente
def cambiar_precio():
    nombre = input('\nProducto al que deseas cambiar el precio: ').strip().upper()

    if nombre not in inventario:
        print('❌ El producto no existe en el inventario.')
        return

    try:
        nuevo_precio = float(input('Nuevo precio: '))
        if nuevo_precio < 0:
            print('⚠️ El precio no puede ser negativo.')
            return
    except ValueError:
        print('⚠️ Entrada inválida. Usa un número válido.')
        return

    inventario[nombre]["precio"] = nuevo_precio
    print('✅ Precio actualizado.')

# Eliminar un producto del inventario
def eliminar_producto():
    nombre = input('\nNombre del producto a eliminar: ').strip().upper()

    if nombre in inventario:
        del inventario[nombre]
        print('🗑️ Producto eliminado del inventario.')
    else:
        print('❌ El producto no existe.')

# Mostrar todos los productos del inventario
def mostrar_inventario():
    if not inventario:
        print('📭 El inventario está vacío.')
        return

    print(f"\n{'Producto':<20}{'Precio ($)':<12}{'Cantidad':<10}")
    print('-' * 45)
    for nombre, datos in inventario.items():
        print(f"{nombre:<20}${datos['precio']:<12.2f}{datos['cantidad']:<10}")

# Calcular el valor total del inventario usando una función lambda
def calcular_valorTotal_inventario():
    if not inventario:
        print('📭 El inventario está vacío.')
    else:
        total = calcular_valor_total(inventario)
        print(f"\n💰 Valor total del inventario: ${total:.2f}")

# Ejecutar el menú principal
menu()
