Algoritmo validar_contrase�a
	
    Definir contrase�a_correcta, contrase�a_usuario Como Cadena
	
    contrase�a_correcta <- "abc123"
    contrase�a_usuario <- ""
	
    Mientras contrase�a_usuario <> contrase�a_correcta Hacer
        Escribir "Ingrese la contrase�a:"
        Leer contrase�a_usuario
		
        Si contrase�a_usuario <> contrase�a_correcta Entonces
            Escribir "Contrase�a incorrecta. Intenta de nuevo."
        FinSi
    FinMientras
	
    Escribir "�Acceso concedido!"
	
FinAlgoritmo

