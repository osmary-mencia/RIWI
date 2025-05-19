Algoritmo pedir_numeros
	Definir numero Como Entero
    Repetir
        Escribir "Ingresa un número positivo: "
        Leer numero
        Si numero < 0 Entonces
            Escribir "Número negativo ingresado. El programa se detiene."
        Sino
            Escribir "El número ingresado es ", numero
        FinSi
    Hasta Que numero < 0
	
FinAlgoritmo
