Algoritmo suma_hasta_cero
	
    Definir numero, suma Como Entero
    suma <- 0
	
    Escribir "Ingrese un n�mero (0 para terminar):"
    Leer numero
	
    Mientras numero <> 0 Hacer
        suma <- suma + numero
        Escribir "Ingrese otro n�mero (0 para terminar):"
        Leer numero
    FinMientras
	
    Escribir "La suma total de los n�meros es: ", suma
	
FinAlgoritmo

