Algoritmo validar_contraseña
	
    Definir contraseña_correcta, contraseña_usuario Como Cadena
	
    contraseña_correcta <- "abc123"
    contraseña_usuario <- ""
	
    Mientras contraseña_usuario <> contraseña_correcta Hacer
        Escribir "Ingrese la contraseña:"
        Leer contraseña_usuario
		
        Si contraseña_usuario <> contraseña_correcta Entonces
            Escribir "Contraseña incorrecta. Intenta de nuevo."
        FinSi
    FinMientras
	
    Escribir "¡Acceso concedido!"
	
FinAlgoritmo

