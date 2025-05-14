# diccionario vacío llamado inventory. Este diccionario va a guardar la información de todos los productos.
# Clave: nombre del producto
# Valor: otro diccionario que contiene el precio y la cantidad del producto.
inventory = {}


#función llamada menu, que será el corazón del programa. Desde aquí se mostrará el menú y 
# se llamarán las demás funciones según lo que el usuario elija.
def menu():
    
    #Mensaje decorativo para dar la bienvenida al usuario.
    print('\n🌸  ＷＥＬＣＯＭＥ   ＴＯ   ＯＳＭＡＲＹ\'Ｓ   ＳＨＯＰ 🌸')

    # Antes de mostrar el menú, se agregan obligatoriamente 5 productos iniciales
    five_initial_products()

    # Se inicia un bucle infinito (while True:) que servirá para mostrar el menú y ejecutar las acciones del programa
    # hasta que el usuario decida salir.
    while True:
        
        #Se muestra el menú de opciones disponibles para el usuario.
        print('\n             ⡷⠂Inventory Manager⠐⢾\n')
        print('(1) Add a product.')
        print('(2) Consult a product in inventory.')
        print('(3) Update the price of a product.')
        print('(4) Delete a product from inventory.')
        print('(5) Calculate total inventory value.')
        print('(0) Exit.')
        
        #Se solicita al usuario que elija una opción del menú.
        #.strip() elimina espacios innecesarios.
        opcion = input('\nChoose an available option from the menu: ').strip().lower()
        
        if opcion == '1':
            add_product()
        elif opcion == '2':
            consult_product()
        elif opcion == '3':
            update_price()
        elif opcion == '4':
            delete_product()
        elif opcion == '5':
            calculate_productos_inventory()
        elif opcion == '0':
            print('\nnミ💖 See you later 💖 彡')
            break
        else: 
            print('\n ❌ Invalid option. Choose a valid option from the menu.')
            
            
# Se define la función five_initial_products, que se ejecuta antes del menú. 
# Su propósito es obligar al usuario a ingresar 5 productos válidos al inventario antes de comenzar a trabajar con él.
def five_initial_products():
    
    #Muestra un mensaje indicando al usuario que debe ingresar 5 productos antes de continuar.
    print('\nBefore starting, enter 5 products into the inventory.')
    
    # Variable contador que lleva la cuenta de cuántos productos válidos se han ingresado.
    contador = 0
    
    #Bucle while que se repite hasta que el contador llegue a 5, es decir, hasta que se hayan agregado 5 productos exitosamente.
    while contador < 5:
        
        #Se pide el nombre del producto:
        # .strip() elimina espacios en blanco al inicio o final.
        # .upper() convierte el nombre a mayúsculas para evitar duplicados con minúsculas (como "pan" y "PAN").
        name = input(f'\nEnter product number {contador+1}. \nProduct name: ').strip().upper()
        
        #Si el producto ya existe en el inventario, muestra un error y con continue vuelve a pedir el producto sin aumentar el contador.
        if name in inventory:
            print('\n⚠️ This product already exists.')
            continue
        
        # Verifica si el usuario no escribió nada
        # Si el campo está vacío (el usuario solo presionó Enter), lanza un error y pide el producto de nuevo.
        if not name:
            print('\n⚠️ The name product cannot be empty')
            continue
            
        try:
            price = float(input('Price: '))
            if price < 0:
                print('\n⚠️ The price cannot be negative.\n')
                continue
            
            amount = int(input('Amount: '))
            if amount < 0:
                print('\n⚠️ The amount cannot be negative.\n')
                continue
            
            # Si todo es válido, se agrega el producto al diccionario global inventory, 
            # usando como clave el nombre y como valor otro diccionario con price y amount.
            inventory[name] = {'price': price, 'amount': amount}
            
            #Muestra mensaje de éxito al agregar el producto correctamente.
            print('\n✅ Products added successfully.\n')
            
            #Aumenta el contador porque se ingresó un producto válido.
            contador +=1
        
        # Si el usuario escribe letras o algo inválido para el precio o cantidad, se atrapa el error y se muestra un mensaje claro.
        except ValueError:
            print('\n⚠️ Invalid entry. Enter numbers for price and amount.\n')
       
    
# Add a product to inventory
def add_product():
    # Se pide al usuario el nombre del producto.
    # .strip() elimina espacios en blanco al principio y al final.
    # .upper() convierte todo el texto a mayúsculas, lo cual es útil para evitar duplicados escritos con minúsculas o con errores de formato.
    name = input('\nProduct name: ').strip().upper()
    
    # Verifica que el usuario sí haya escrito algo.
    # Si deja el campo vacío, el programa muestra un mensaje de advertencia y termina esta función sin continuar (return).
    if not name:
        print('\n⚠️ The name product cannot be empty.')
        return
    
    # Revisa si ese nombre ya existe como clave en el diccionario inventory.
    # Si sí existe, avisa al usuario y no guarda nada (para evitar duplicados).
    if name in inventory:
        print('\n⚠️ This product already exists.')
        return
    
    # Aquí usamos try porque si el usuario pone letras o símbolos no válidos, eso causaría un ValueError.
    try:
        price = float(input('Price: '))
        # Verifica que el precio no sea negativo, ya que eso no tendría sentido en un inventario.
        if price < 0:
            print('\n⚠️ The price cannot be negative.')
            return
        
        amount = int(input('Amount: '))
        if amount < 0:
            print('\n⚠️ The amount cannot be negative.')
            return
        
    # Si hubo algún error al convertir a float o int (por ejemplo, letras), el programa entra en este bloque y muestra un mensaje sin detenerse.
    except ValueError:
        print('\n⚠️ Invalid entry. Enter numbers for price and amount.')
        return
    
    # Si todo salió bien, se guarda el producto en el diccionario inventory usando:
    # El nombre como clave. 
    # Un diccionario interno como valor, que contiene el precio y la cantidad.
    inventory[name] = {'price': price, 'amount': amount}
    
    # Finalmente, confirma que el producto se agregó correctamente.
    print('✅ Product added successfully.')
    
# Se define la función consult_product, que será llamada cuando el usuario quiera consultar información de un producto en el inventario.
def consult_product():
    
    #Aquí se le pide al usuario el nombre del producto que desea consultar.
    # .strip() elimina espacios en blanco al inicio y al final, para evitar errores si el usuario accidentalmente escribe " pan " en vez de "pan".
    # .upper() convierte todo a mayúsculas. Así se garantiza que los nombres se busquen de forma uniforme (por ejemplo, "Pan", "PAN", "pan" se tratarán igual).
    name = input('Product name to consult: ').strip().upper()
    
    # Se usa el método .get() del diccionario inventory para buscar el producto usando el nombre ingresado.
    # Si el producto existe, se guarda en la variable product. Si no existe, product será None.
    product = inventory.get(name)
    
    # Si product tiene algún valor (es decir, sí existe en el inventario), se muestra en pantalla: 
    # El nombre del producto, El precio, con 2 decimales (:.2f), La cantidad disponible
    if product:
        print(f"\n {name} -> Precio: ${product['price']:.2f}, Amount: {product['amount']}")
    else:
        # Si product es None, entonces el producto no se encontró en el inventario, y se muestra un mensaje claro al usuario.
        print('\n❌ The product doesn\'t exist in inventory')
        
# Define una función llamada update_price que se encargará de actualizar el precio de un producto que ya está en el inventario.
def update_price():
    #  Se le pide al usuario el nombre del producto cuyo precio desea modificar.
    # .strip() elimina espacios en blanco innecesarios.
    # .upper() convierte el nombre a mayúsculas para mantener el mismo formato en el inventario.
    name = input('\nProduct name you want to change the price of: ').strip().upper()

    # Se verifica si el producto existe en el inventario.
    # Si no existe, se muestra un mensaje de error y la función termina con return.
    if name not in inventory:
        print('\n❌The product doesn\'t exist in inventory')
        return
    
    # Se intenta leer un nuevo precio ingresado por el usuario y convertirlo a tipo float (número decimal).
    # Aquí usamos try porque si el usuario escribe letras o símbolos inválidos, Python lanzaría un error.
    try:
        
        new_price = float(input('New price: '))
        #Si el nuevo precio es menor que cero, se muestra un mensaje de advertencia y la función termina.
        if new_price < 0:
            print('\n⚠️ The price cannot be negative.')
            return
        
    #  Si hubo un error al convertir el valor (por ejemplo, el usuario escribió "cinco" en vez de "5"), 
    # este bloque evita que el programa se caiga y muestra un mensaje de error.
    except ValueError:
        print('⚠️ Invalid entry. Enter numbers for price.')
        return
    
    # Si todo es correcto, se actualiza el precio del producto en el diccionario.
    # inventory[name] accede al producto, y 'price' es la clave dentro del diccionario anidado.
    inventory[name]['price'] = new_price
    # Muestra un mensaje confirmando que el precio fue actualizado correctamente.
    print('\n✅ Updated price.')

# Define la función delete_product, que no recibe parámetros y se encargará de eliminar un producto del inventario.  
def delete_product():
    # Solicita al usuario el nombre del producto que desea eliminar.
    # strip() elimina los espacios en blanco al principio y al final del texto (útil si el usuario deja un espacio por error).
    # .upper() convierte todo el texto a mayúsculas, para evitar errores de búsqueda por diferencias de mayúsculas y minúsculas.
    name = input('\nProduct name to delete: ').strip().upper()
    
    # Verifica si el nombre ingresado existe como clave en el diccionario inventory.
    # Si existe, quiere decir que el producto está en el inventario.
    if name in inventory:
        # Elimina la clave name del diccionario inventory, es decir, borra el producto del inventario.
        del inventory[name]
        # Mensaje de confirmación para que el usuario sepa que el producto fue eliminado con éxito.
        print('\n✅ Product deleted from inventory.')
    else:
        #  Si el producto no existe, se muestra un mensaje claro informando al usuario que ese producto no está en el inventario.
        print('\n❌ The product doesn\'t exist in inventory')
        
# Define la función delete_product, que no recibe parámetros y se encargará de eliminar un producto del inventario.
calculate_total_values = lambda inv: sum(info['price'] * info['amount'] for info in inv.values())

def calculate_productos_inventory():
    if not inventory:
       print('\nThe inventory is empty')
       return
    else:
        # Muestra encabezados en tabla:
        # Usa formateo para alinear texto como si fuera una tabla.
        print(f"\n{'Product':<20}{'Price ($)':<12}{'Amount':<10}")
        print('-' * 45)
        # Muestra cada producto:
        # Recorre el inventario con .items() y separa name y datas.
        # Muestra nombre, precio (con 2 decimales), y cantidad.
        for name, datas in inventory.items():
            print(f"{name:<20}${datas['price']:<12.2f}{datas['amount']:<10}")
        
        # Calcula y muestra el valor total:
        # Llama a la función lambda para obtener el total del inventario.
        # Lo muestra con 2 decimales.
        total = calculate_total_values(inventory)
        print(f'\n💲Total inventory value: ${total:.2f}')
          
# Esto ejecuta el programa completo mostrando primero el mensaje de bienvenida, 
# solicitando los 5 productos iniciales, y luego abriendo el menú principal.
menu()