Algoritmo factorial_numero
    Definir numero, i, factorial Como Entero
    factorial <- 1
	
    Escribir "Ingrese un n�mero para calcular su factorial:"
    Leer numero
	
    Para i <- 1 Hasta numero Con Paso 1 Hacer
        factorial <- factorial * i
    FinPara
	
    Escribir "El factorial de ", numero, " es: ", factorial
FinAlgoritmo
