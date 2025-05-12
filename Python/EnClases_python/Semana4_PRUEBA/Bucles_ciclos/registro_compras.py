"""
🔥 Reto difícil: Registro de compras
📌 Objetivo: Crea un programa que permita al usuario registrar productos en un carrito.

Detalles:
Usa un ciclo while para pedir al usuario que ingrese productos uno a uno.

Usa una lista para guardar los productos.

Si el usuario escribe "salir", el programa debe terminar el bucle y mostrar:

Los productos registrados (uno por uno con for)

La cantidad total de productos.
"""
carrito = []

while True:
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("\n🌸  ＷＥＬＣＯＭＥ   ＴＯ   ＯＳＭＡＲＹ'Ｓ   ＳＨＯＰ 🌸 \n")
    
    print('             ⡷⠂CARRITO DE COMPRA⠐⢾\n')
    
    print('MENU DE OPCIONES\n')
    print('1. Añadir producto al carrito.')
    print('2. Ver productos del carrito.')
    print('SALIR\n')
    
    opcion = input('Ingresa un opcion del menu: ').upper()
    
    if opcion == '1':
        producto = input('\nIngresa un producto en el carrito: ').upper().strip()
        carrito.append(producto)
        
    elif opcion == '2':
        if not carrito:
            print('\nEl carrito esta vacio.\n')
        else: 
            print('\nProductos del carrito:\n')
            for producto in carrito:
                print(f' - {producto}')
        
    elif opcion == 'SALIR':
        print('\nGracias por tu compra en Osmary 🌸\n')
        if carrito:
            print('Productos de tu carrito: \n')
            for producto in carrito:
                print(f' - {producto}')
            print(f'\nTotal de productos en el carrito: {len(carrito)}')
        else:
            print('\nTu carrito estaba vacío.')
        print('\nFin del programa.')
        break
    
    else:
        print('Opcion invalida. Ingresa una opcion del menu')
        
        
    
    