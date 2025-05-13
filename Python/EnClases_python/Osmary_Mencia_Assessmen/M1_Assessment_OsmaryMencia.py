#An empty dictionary is created to store inventory products.
inventory = { }

#The main program menu is created
def menu ( ):
    
    print('\n🌸  ＷＥＬＣＯＭＥ   ＴＯ   ＯＳＭＡＲＹ\'Ｓ   ＳＨＯＰ 🌸')
    
#Before starting the program, the user is asked to enter 5 products so that the menu can be displayed.
    five_initial_products()


    while True:
        
        print('\n             ⡷⠂Inventory Manager⠐⢾\n')
        print('(1) Add a product.')
        print('(2) Consult a product in inventory.')
        print('(3) Update the price of a product.')
        print('(4) Delete a product from inventory.')
        print('(5) Calculate total inventory value.')
        print('(0) Exit.')
        
        
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
            
            
#Function that asks for the 5 initial products when the program starts
def five_initial_products():
    print('\nBefore starting, enter 5 products into the inventory.')
    
    #the counter starts at zero
    contador = 0
    
    #Until this condition is met it will be repeated
    while contador < 5:
        
        #you are asked for the name of the product
        name = input(f'\nEnter product number {contador+1}. \nProduct name: ').strip().upper()
        
        #If the name is already in the inventory, it returns an error message.
        if name in inventory:
            print('\n⚠️ This product already exists.')
            continue
        
        #If you do not enter anything in the name, it returns an error message.
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
            
            inventory[name] = {'price': price, 'amount': amount}
            print('\n✅ Products added successfully.\n')
            
            contador +=1
            
        except ValueError:
            print('\n⚠️ Invalid entry. Enter numbers for price and amount.\n')
       
    
# Add a product to inventory
def add_product():
    
    name = input('\nProduct name: ').strip().upper()
    
    #If you do not enter anything in the name, it returns an error message.
    if not name:
        print('\n⚠️ The name product cannot be empty.')
        return
    
    #If the name is already in the inventory, it returns an error message.
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
    
# Query a product by name
def consult_product():
    name = input('Product name to consult: ').strip().upper()
    product = inventory.get(name)
  
    if product:
        print(f"\n {name} -> Precio: ${product['price']:.2f}, Amount: {product['amount']}")
    else:
        print('\n❌ The product doesn\'t exist in inventory')
        
# Change the price of an existing product
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
    
    inventory[name]['price'] = new_price
    print('\n✅ Updated price.')

# Delete a product from inventory  
def delete_product():
    name = input('\nProduct name to delete: ').strip().upper()
    
    if name in inventory:
        del inventory[name]
        print('\n✅ Product deleted from inventory.')
    else:
        print('\n❌ The product doesn\'t exist in inventory')
        
# Calculate the total value of the inventory
calculate_total_values = lambda inv: sum(info['price'] * info['amount'] for info in inv.values())

def calculate_productos_inventory():
    if not inventory:
       print('\nThe inventory is empty')
       return
    else:
        print(f"\n{'Product':<20}{'Price ($)':<12}{'Amount':<10}")
        print('-' * 45)
        for name, datas in inventory.items():
            print(f"{name:<20}${datas['price']:<12.2f}{datas['amount']:<10}")
        
        total = calculate_total_values(inventory)
        print(f'\n💲Total inventory value: ${total:.2f}')
          
#Run the main menu
menu()