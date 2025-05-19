Algoritmo suma_n_numeros
    Definir N, i, suma Como Entero
    suma <- 0
	
    Escribir "Ingrese un número N:"
    Leer N
	
    Para i <- 1 Hasta N Con Paso 1 Hacer
        suma <- suma + i
    FinPara
	
    Escribir "La suma de los primeros ", N, " números naturales es: ", suma
FinAlgoritmo

