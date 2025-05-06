Algoritmo calculadora_completa

	Definir primer_numero Como Entero
	Definir segundo_numero Como Entero
	Definir resultado Como real
	Definir operacion_matematica Como Caracter
	
	Escribir "BIEMVENIDO A SU CALCULADORA"
	
	Escribir "Digite su primer numero"
	leer primer_numero
	
	Escribir "Digite su segundo numero"
	leer segundo_numero
	
	
	Escribir "Elija una opcion"
	leer operacion_matematica
	
	si operacion_matematica es igual que "sumar" entonces 
		resultado = primer_numero + segundo_numero
		Escribir "El resultado de la suma es: " , resultado
	FinSi
	
	si operacion_matematica es igual que "restar" entonces 
		resultado = primer_numero - segundo_numero
		Escribir "El resultado de la resta es: " , resultado
	FinSi
	
	si operacion_matematica es igual que "multiplicar" entonces 
		resultado = primer_numero * segundo_numero
		Escribir "El resultado de la multiplicacion es: " , resultado
	FinSi
	
	si operacion_matematica es igual que "dividir" entonces 
		resultado = primer_numero / segundo_numero
		Escribir "El resultado de la division es: " , resultado
	FinSi
	

	
	
FinAlgoritmo
