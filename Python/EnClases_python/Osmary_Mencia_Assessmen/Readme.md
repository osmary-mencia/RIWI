# 🌸  ＷＥＬＣＯＭＥ   ＴＯ   ＯＳＭＡＲＹ'Ｓ   ＳＨＯＰ 🌸

## Cuando comienza el programa pedira 5 productos a ingresar para avanzar.

Ejemplo:

Enter product number 1. 
Product name: pan 
Price: 500 
Amount: 5

✅ Products added successfully.


Enter product number 2. 
Product name: huevo
Price: 700 
Amount: 3

✅ Products added successfully.


Enter product number 3. 
Product name: carne
Price: 15000
Amount: 1

✅ Products added successfully.


Enter product number 4. 
Product name: pollo
Price: 20000
Amount: 1

✅ Products added successfully.


Enter product number 5. 
Product name: galletas
Price: 1000
Amount: 5

✅ Products added successfully.

## Cuando se ingresen todos los productos pedidos inicialmente se mostrara el menu de opciones y se pide que se ingrese una opcion del menu.

EJEMPLO: 

⡷⠂Inventory Manager⠐⢾

(1) Add a product.
(2) Consult a product in inventory.
(3) Update the price of a product.
(4) Delete a product from inventory.
(5) Calculate total inventory value.
(0) Exit.

Choose an available option from the menu: 

## Si el usuario elije la opcion 1 le pedira que ingrese los datos del producto

EJEMPLO:

Product name: harina
Price: 3500
Amount: 4
✅ Product added successfully.

## Si el usuario elije la opcion 2 se le pedira que ingrese el nombre del producto que desea concultar y los mostrara pero si no existe le retorna un mensaje.

EJEMPLO SI NO EXISTE:

Product name: harina
Price: 3500
Amount: 4
✅ Product added successfully.

EJEMPLO SI EXISTE:

Choose an available option from the menu: 2
Product name to consult: PAN

📦 PAN -> Precio: $500.00, Amount: 5

# Si el usuario elije la opcion 3 le pedira el nombre del producto al que le quiere cambiar el precio.

## si el nombre que ingresa no existe en el inventario le retorna un mensaje:

Choose an available option from the menu: 3

Product name you want to change the price of: ola

❌The product doesn't exist in inventory

## si el producto existe entonces le pide el precio nuevo
Choose an available option from the menu: 3

Product name you want to change the price of: pan
New price: 700

✅ Updated price.


# si el usuario elije la opcion 4 se le pide el nombre del producto que quiere eliminar si no existe el muestra un mesaje:

Choose an available option from the menu: 4

Product name to delete: ola

❌ The product doesn't exist in inventory

## Pero si el nombre ingresado si existe lo borra:

Choose an available option from the menu: 4

Product name to delete: pan

✅ Product deleted from inventory.

## La opcion 5 muestra el todos los productos del inventario con el nombre, precio y cantidad.

Choose an available option from the menu: 5

Product             Price ($)   Amount    
---------------------------------------------
PAN                 $500.00      5         
CARNE               $15000.00    1         
GALLETAS            $1000.00     5         
QUESO               $12500.00    2         
HARINA              $3500.00     2         

💲Total inventory value: $54500.00

## y por ultimo la opcion 0 termina el programa

Choose an available option from the menu: 0

nミ💖 See you later 💖 彡