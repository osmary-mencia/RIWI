print("----SISTEMA DE VALIDACION DE PRODUCTOS----\n")
#entrada de datos del usuario 
nombre_usuario=input("INGRESE SU NOMBRE: ") #le pedimos el nombre al usuario
id_usuario=input("INGRESE SU NUMERO DE IDENTIFICACION: ") #le pedimos la cedula al usuario
print("\n") #es un  salto de linea
#entrada de datos del producto 
nombre_producto = input("-Ingrese el nombre del producto: ").upper()
cantidad_productos = input("-Ingrese la cantidad a llevar: ")
cantidad_productos = float(cantidad_productos)
precio_unitario = float(input("-Ingrese el precio del producto: "))
print("\n")

#procedimiento para calcular el monto total a pagar 
total_precio = cantidad_productos*precio_unitario
#se simula un menu de opciones y se le da al usuario una opcion a elegir
porcentaje_descuento =input("Desea aplicar un descuento: \n(SI)\n(NO)\nINGRESE EL DESCCUENTO: ").upper()

if porcentaje_descuento == "SI": #si la opcion del usuario es SI
    descuento_agregar= float(input("INGRESA UN DESCUENTO ENTRE 1% Y 100%: ")) #Le pedimos al usuario que ingrese su descuento
    if descuento_agregar >=1 and descuento_agregar <=100:#definimos el rango del porcentaje de descuento
        precio_descuento= total_precio*(descuento_agregar/100)#se hace el procedimiento para calcular el descuento
        total_precio_descuento = total_precio - precio_descuento
    else: #SI el usuario ingresa un valor que no esta en el rango del 1 al 100 le retorna mensaje de un error
        print("ERROR!! \nPor favor, Ingresa un valor entre (1% a 100%)")
        print("INTENTALO DE NUEVO!!")   
        exit() #se finaliza el programa
 
#si la opcion de usuario es NO se muestra automaticamente el valor a pagar sin descuento        
elif porcentaje_descuento == "NO" :
    precio_descuento = 0  
    print(f"VALOR A PAGAR:  {nombre_producto} {total_precio:.2f}\n")
else: #si el usuario ingresa un valor diferente a SI y NO le muestra un mesaje y se cierra el programa
    print("Opción no válida!!. Escribe 'SI' o 'NO'.")
    exit()

if porcentaje_descuento == "SI":
    print(f"Tu descuento seria: {precio_descuento:.2f}")
    print(f"Tu total a pagar seria: {nombre_producto} {total_precio_descuento:.2f}")
elif porcentaje_descuento == "NO":
    print("SIN DESCUENTO")
print("\n")
print("GRACIAS POR TU COMPRA!!")