Algoritmo pedir_numeros
	Definir numero Como Entero
    Repetir
        Escribir "Ingresa un n�mero positivo: "
        Leer numero
        Si numero < 0 Entonces
            Escribir "N�mero negativo ingresado. El programa se detiene."
        Sino
            Escribir "El n�mero ingresado es ", numero
        FinSi
    Hasta Que numero < 0
	
FinAlgoritmo
