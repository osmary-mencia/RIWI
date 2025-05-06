Algoritmo comparacion_de_dos_numeros
	
	Definir num1, num2 Como Real
	
	Escribir "Comparacion de dos numeros"
	Escribir "Ingrese su primer numero"
	Leer num1
	Escribir "ingrese su segundo numero"
	leer num2
	
	si num1 > num2 Entonces
		Escribir "El numero mayor es: " , num1
	SiNo
		si num2 > num1 Entonces
			Escribir "El numero mayor es: " num2
		SiNo
			Escribir "Los dos numero son iguales"
		FinSi
	FinSi
	
FinAlgoritmo
