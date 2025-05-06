Algoritmo Clasificaion_edades
	
	Definir edad_usuario Como Entero
	
	Escribir "2.Clasificacion de edades"
	Escribir "INGRESE SU EDAD"
	Leer edad_usuario
	
si edad_usuario <12 Entonces
	Escribir "Eres un niño"
SiNo
	si edad_usuario >=13 y edad_usuario <=17 Entonces
		Escribir "Eres un adolescente"
	SiNo
			Escribir "Eres un adulto"
	FinSi
FinSi
	
	
FinAlgoritmo
