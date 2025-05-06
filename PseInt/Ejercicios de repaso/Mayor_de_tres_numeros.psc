Algoritmo Mayor_de_tres_numeros
	
	Definir num1, num2, num3 Como Entero
	
	Escribir "Ingrese su primer numero"
	leer num1
	Escribir "Ingrese su segundo numero"
	leer num2
	Escribir "ingrese su tercer numero"
	leer num3
	
	si num1 >= num2 y num1>=num3 Entonces
		mayor <- num1
	SiNo
		si num2 >= num1 y num2>=num3 Entonces
			mayor <- num2
		SiNo
			mayor<-num3
		FinSi
	FinSi
	Escribir "El numero mayor es: " , mayor
FinAlgoritmo
