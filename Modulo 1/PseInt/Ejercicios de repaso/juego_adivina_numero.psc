Algoritmo juego_adivina_numero
	
    Definir numero_secreto, intento Como Entero
    numero_secreto <- 7
    intento <- 0
	
    Escribir "¡Adivina el número secreto entre 1 y 10!"
	
    Mientras intento <> numero_secreto Hacer
        Escribir "Ingresa tu intento:"
        Leer intento
		
        Si intento < numero_secreto Entonces
            Escribir "El número secreto es mayor."
        SiNo
            Si intento > numero_secreto Entonces
                Escribir "El número secreto es menor."
            FinSi
        FinSi
    FinMientras
	
    Escribir "¡Felicidades! Adivinaste el número."
	
FinAlgoritmo
