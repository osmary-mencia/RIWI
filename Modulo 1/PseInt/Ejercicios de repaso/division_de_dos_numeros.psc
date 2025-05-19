Algoritmo division_de_dos_numeros
	
	Definir num1, num2, resultado Como Real
	
	Escribir "Ingrese un numero"
	leer num1
	Escribir "Ingrese otro numero"
	leer num2
	
	si num2 <> 0 Entonces
		resultado <- num1 / num2
		Escribir "La division de los dos numeros es: " resultado
	SiNo
		Escribir "Error, no se puede dividir entre 0."
	FinSi
	
FinAlgoritmo
