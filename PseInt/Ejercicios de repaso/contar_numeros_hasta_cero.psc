Algoritmo contar_numeros_hasta_cero
	
    Definir numero Como Entero 
    Definir contador Como Entero
	
    contador <- 0
	
    Escribir "Ingrese un n�mero (0 para salir):"
    Leer numero
	
    Mientras numero <> 0 Hacer
        contador <- contador + 1
        Escribir "Ingrese otro n�mero (0 para salir):"
        Leer numero
    FinMientras
	
    Escribir "Ingresaste ", contador, " n�meros."
	
FinAlgoritmo

