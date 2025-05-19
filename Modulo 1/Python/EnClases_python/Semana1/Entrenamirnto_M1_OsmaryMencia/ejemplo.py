print("Bienvenido Usuario")
Suma_T=0
Nombre_Producto=[]

#se le pedira el usuario el nombre del producto, cantidad del mismo a llevar y su precio.
while True:
    Producto=input("Escriba el nombre del producto:  ")
    Nombre_Producto.append(Producto)
    Cantidad_Llevar=int(input("\nCantidad a llevar: "))
    Precio=float(input("\nIngrese el precio unitario: "))
    Precio*=Cantidad_Llevar
    Suma_T+=Precio
    Repetir=input("\nDesea agregar algo mas? Si/No ")
   
    if Repetir=="No" or Repetir=="no":
        break
    
#En la siguiente linea se le pide al usuario si aplica para un descuento y que luego ingrese el valor del descuento.

Descuento=input("Aplica para descuento? S/si N/no: ")
if(Descuento=="Si" or Descuento=="si" or Descuento=="s" or Descuento=="S" or Descuento=="SI"):
    Descuento=int(input("\nIngrese el valor del descuento: "))
    Descuento=(Descuento/100)*Suma_T
    Suma_T-=Descuento
    print(f"\nEl precio a pagar es {Suma_T}0")
        
else:
    print(f"\nCosto total: {Suma_T}0")
    
#El programa terminara al mostrar el precio final del producto o cuando muestre el precio final, junto a los productos que llevara.
 
print("\nLos productos que llevo fueron: ")
for x in Nombre_Producto:
        print(f"--{x}--")