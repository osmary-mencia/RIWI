Algoritmo mayor_de_tre_numeros
	
	Definir num1, num2, num3 Como real
	
	Escribir "Determine el mayor numero de tres numeros"
	Escribir "Digite su primer numero"
	leer num1
	Escribir "Digite su segundo numero"
	leer num2
	Escribir "Digite su tercer numero"
	leer num3
	
	si num1 >= num2 y num1 >= num3 Entonces
		mayor <- num1
	SiNo
		si num2 >= num1 y num2>= num3 Entonces
			mayor <- num2
		SiNo
			mayor <- num3
		FinSi
	FinSi
	
	Escribir "El numero mas grande es: " , mayor
	
FinAlgoritmo
