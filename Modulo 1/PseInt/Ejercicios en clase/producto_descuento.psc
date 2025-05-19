Algoritmo producto_descuento
	
	Definir precio_producto Como Real
	Definir porcentaje_descuento Como Real
	Definir descuento Como Real
	Definir precio_final Como Real
	
	Escribir "CALCULE EL DESCUENTO DE UN PRODUCTO"
	Escribir "Ingrese el valor del producto"
	leer precio_producto
	
	Escribir "Ingrese el porsentaje del producto"
	leer porcentaje_descuento
	
	descuento = precio_producto * (porcentaje_descuento/100)
	precio_final= precio_producto - descuento
	
	Escribir "El precio final del producto es de: " precio_final
	
	

	
FinAlgoritmo
