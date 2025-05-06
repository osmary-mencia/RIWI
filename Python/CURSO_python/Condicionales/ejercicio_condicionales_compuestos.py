print("Sistema para calcular el promedio de un alumno")

nombre = str(input("Para comenzar, ¿Cual es tu nombre?: "))

nota1 = float(input(nombre + " ¿Cual es tu calificacion en Matematicas: "))
nota2 = float(input(nombre + " ¿Cual es tu calificacion en Quimica: "))
nota3 = float(input(nombre + " ¿Cual es tu calificacion en Fisica: "))

promedio = (nota1+nota2+nota3)/3

if promedio >= 3:
    print(f"Felicilades!! {nombre} aprobaste con un promedio de: {promedio: .2f}")
else:
    print(f"Lo siento {nombre}, no aprobaste.")
    
print("fin")