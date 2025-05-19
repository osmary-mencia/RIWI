Algoritmo test
	Escribir "total de preguntas"
	Leer total_preguntas
	Escribir "respuestas correctas"
    Leer respuestas_correctas
    
    porcentaje <- (respuestas_correctas / total_preguntas) * 100
    
    Si porcentaje >= 90 Entonces
        nivel <- "Nivel máximo"
    Sino 
		Si porcentaje >= 75 y porcentaje> 50 Entonces
			Escribir  "Nivel medio"
		Sino 
			Si porcentaje >= 50 Entonces
				Escribir"Nivel regular"
			Sino
				Escribir "Fuera de nivel"
			FinSi
			
			Escribir "El porcentaje de respuestas correctas es: ", porcentaje
			
		FinSi
	FinSi
	
FinAlgoritmo
