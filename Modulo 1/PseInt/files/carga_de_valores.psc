Algoritmo carga_de_valores 
	// Inicializamos las variables
    negativos <- 0
    positivos <- 0
    acumulado <- 0
    suma_pares <- 0
	
    // Bucle para ingresar 10 números
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        Escribir "Ingrese el valor ", i
        Leer numero
        
        // Contamos los valores negativos y positivos
        Si numero < 0 Entonces
            negativos <- negativos + 1
        Sino
            Si numero > 0 Entonces
                positivos <- positivos + 1
            FinSi
        FinSi
		
        // Acumulamos el total de los números para el promedio
        acumulado <- acumulado + numero
		
        // Si el número es par, lo sumamos a la variable suma_pares
        Si numero Mod 2 = 0 Entonces
            suma_pares <- suma_pares + numero
        FinSi
    FinPara
	
    // Calculamos el promedio
    promedio <- acumulado / 10
	
    // Mostramos los resultados
    Escribir "A) La cantidad de valores negativos es: ", negativos
    Escribir "B) La cantidad de valores positivos es: ", positivos
    Escribir "C) El promedio de los valores ingresados es: ", promedio
    Escribir "D) El valor acumulado de los números pares es: ", suma_pares
FinAlgoritmo
