# 💼 Diccionario vacío para almacenar los productos del inventario
inventory = {}

# 📋 Menú principal del programa
def menu():
    print('\n🌸  Ｗｅｌｃｏｍｅ   Ｔｏ   ＯＳＭＡＲＹ\'uff53   ＳｈｏＰ 🌸')

    # ✅ Antes de mostrar el menú, se agregan obligatoriamente 5 productos iniciales
    five_initial_products()

    # 🔁 Bucle principal para mostrar el menú y permitir acciones múltiples
    while True:
        print('\n             ⡇⁂Inventory Manager⁒⡾\n')
        print('(1) Add a product.')
        print('(2) Consult a product in inventory.')
        print('(3) Update the price of a product.')
        print('(4) Delete a product from inventory.')
        print('(5) Calculate total inventory value.')
        print('(0) Exit.')

        opcion = input('\nChoose an available option from the menu: ').strip().lower()

        # 🔀 Se evalúa la opción elegida por el usuario
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
            print('\nn🐟💖 See you later 💖 彡')
            break
        else:
            print('\n ❌ Invalid option. Choose a valid option from the menu.')


# 🟡 Función para ingresar los 5 productos obligatorios al iniciar el programa
def five_initial_products():
    print('\nBefore starting, enter 5 products into the inventory.')
    contador = 0  # 🔢 Contador para asegurarse de ingresar exactamente 5 productos

    while contador < 5:
        name = input(f'\nEnter product number {contador+1}. \nProduct name: ').strip().upper()

        # ⛘ Validaciones de entrada: vacío o repetido
        if name in inventory:
            print('\n⚠️ This product already exists.')
            continue
        if not name:
            print('\n⚠️ The name product cannot be empty')
            continue

        try:
            price = float(input('Price: '))  # ✅ Conversión a número decimal
            if price < 0:
                print('\n⚠️ The price cannot be negative.\n')
                continue

            amount = int(input('Amount: '))  # ✅ Conversión a entero
            if amount < 0:
                print('\n⚠️ The amount cannot be negative.\n')
                continue

            # ✔️ Almacena el producto como un diccionario con precio y cantidad
            inventory[name] = {'price': price, 'amount': amount}
            print('\n✅ Products added successfully.\n')
            contador += 1  # ⬆️ Aumenta el contador tras ingresar un producto válido

        except ValueError:
            print('\n⚠️ Invalid entry. Enter numbers for price and amount.\n')


# ➕ Función para añadir nuevos productos luego de los 5 iniciales
def add_product():
    name = input('\nProduct name: ').strip().upper()

    if not name:
        print('\n⚠️ The name product cannot be empty.')
        return

    if name in inventory:
        print('\n⚠️ This product already exists.')
        return

    try:
        price = float(input('Price: '))
        if price < 0:
            print('\n⚠️ The price cannot be negative.')
            return
        amount = int(input('Amount: '))
        if amount < 0:
            print('\n⚠️ The amount cannot be negative.')
            return
    except ValueError:
        print('\n⚠️ Invalid entry. Enter numbers for price and amount.')
        return

    inventory[name] = {'price': price, 'amount': amount}
    print('✅ Product added successfully.')


# 🔎 Función para consultar un producto por su nombre
def consult_product():
    name = input('Product name to consult: ').strip().upper()
    product = inventory.get(name)  # 🔍 Busca en el diccionario

    if product:
        print(f"\n {name} -> Precio: ${product['price']:.2f}, Amount: {product['amount']}")
    else:
        print('\n❌ The product doesn\'t exist in inventory')


# 🔧 Función para actualizar el precio de un producto existente
def update_price():
    name = input('\nProduct name you want to change the price of: ').strip().upper()

    if name not in inventory:
        print('\n❌The product doesn\'t exist in inventory')
        return

    try:
        new_price = float(input('New price: '))
        if new_price < 0:
            print('\n⚠️ The price cannot be negative.')
            return
    except ValueError:
        print('⚠️ Invalid entry. Enter numbers for price.')
        return

    inventory[name]['price'] = new_price  # 🔁 Se actualiza el precio manteniendo la cantidad igual
    print('\n✅ Updated price.')


# 🗑️ Función para eliminar un producto del inventario
def delete_product():
    name = input('\nProduct name to delete: ').strip().upper()

    if name in inventory:
        del inventory[name]  # ❌ Elimina el producto del diccionario
        print('\n✅ Product deleted from inventory.')
    else:
        print('\n❌ The product doesn\'t exist in inventory')


# 🧲 Función lambda para calcular el valor total del inventario
calculate_total_values = lambda inv: sum(info['price'] * info['amount'] for info in inv.values())


# 💰 Función que imprime todos los productos y calcula el total del inventario
def calculate_productos_inventory():
    if not inventory:
        print('\nThe inventory is empty')
        return
    else:
        print(f"\n{'Product':<20}{'Price ($)':<12}{'Amount':<10}")
        print('-' * 45)

        for name, datas in inventory.items():
            print(f"{name:<20}${datas['price']:<12.2f}{datas['amount']:<10}")

        total = calculate_total_values(inventory)  # ✅ Llama la función lambda
        print(f'\n💲Total inventory value: ${total:.2f}')


# ▶️ Se ejecuta el menú principal
def run():
    menu()

run()
