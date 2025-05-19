Algoritmo suma_hasta_cero
	
    Definir numero, suma Como Entero
    suma <- 0
	
    Escribir "Ingrese un número (0 para terminar):"
    Leer numero
	
    Mientras numero <> 0 Hacer
        suma <- suma + numero
        Escribir "Ingrese otro número (0 para terminar):"
        Leer numero
    FinMientras
	
    Escribir "La suma total de los números es: ", suma
	
FinAlgoritmo

