print('******************************************************')
print('* SISTEMA PARA EVALUAR CALIFICACIONES Y ESTADISTICAS *')
print('******************************************************\n')
#Entrada de datos -> se le pide al usuario que ingrese una nota
#Si ingresa un valor que no sea numerico de retorna un mesaje de error y se cierra el programa
try:
    nota = float(input("Ingresa una calificacion entre 0 y 100: "))
except ValueError:
    print("¡ERROR! Debes ingresar una calificion valida.")
    print("PROGRAMA FINALIZADO.")
    exit()
#Si la nota esta en el rango permitido evaluamos si ha aprobado o reprobado
if 0 <= nota <= 100:
    if nota >= 70:
        print("¡FELICIDADES :)! Has aprobado.")
        print("BUEN TRABAJO!! sigue asi...")
    else:
        print("¡OH NO :(! Has reprobado.")
        print("SIGUE ESTUDIANDO!! en la proxima te ira mejor...")
#Si se ingresa una nota que no esta en el rango permitido le retorna un mensaje y se cierra el programa
else:
    print("Calificacion invalida." , nota,  "se encuentra fuera del rango.")
    print("\nINTENTA DE NUEVO")
    print("PROGRAMA FINALIZADO.")
    exit()


print("\n*** SISTEMA DE PROMEDIO DE CALIFICACIONES ***")
#Se pide al usuario que ingrese una lista de notas separadas por comas para calcular el promedio total
entrada = input("\nIngresa una lista de calificaciones separadas por comas: ")

#se valida que se ingresen valores numericos en el rango permitido con comas y sin valores no numericos
try:
    calificaciones = []
    for x in entrada.split(","):
        valor = float(x.strip())  # Intenta convertir a número
        if 0 <= valor <= 100:     # Verifica que esté en el rango
            calificaciones.append(valor)
        else: #si no se cumple le retorna un mensaje de error
            print("Hay valores fuera del rango permitido")
            print("\nPROGRAMA FINALIZADO.")
            print("INTENTA DE NUEVO")
            exit()
#si se cumple los requisitos de la lista se calcula el promedio total de la califcaciones
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print("\nEl promedio es:", round(promedio, 2))
        if 0 <= nota <= 100:
            if nota >= 70:
                print("\n¡FELICIDADES :)! Has aprobado.")
                print("BUEN TRABAJO!! sigue asi...")
            else:
                print("¡OH NO :(! Has reprovado.")
                print("SIGUE ESTUDIANDO!! en la proxima te ira mejor...")
    else:
        print("No se ingresaron calificaciones válidas.")
        print("PROGRAMA FINALIZADO.")
        print("INTENTA DE NUEVO")
        exit()
#en caso de que se ingrese un valor no numerico se retorna un mesaje de error y se cierra el programa
except ValueError:
    print("¡ERROR! Ingresaste un valor no numérico o te falto separar las notas con comas.")
    print("PROGRAMA FINALIZADO.")
    print("INTENTA DE NUEVO")
    exit()

#Contar calificaciones mayores a un valor.
#le pedimos el usuario que ingrese una calificaion en especifico para decirle cuantas notas son mayores asa
valor = float(input("\nIngresa una calificacion para comparar cuantas calificaciones son mayores: "))
contador = 0
i = 0
while i < len(calificaciones):
    if calificaciones[i] > valor:
        contador += 1
    i += 1
print("Cantidad de calificaciones mayores a", valor, " son:", contador)

#Verificar y contar calificación específica
#le pedimos al usuario que ingrese un nota en especifico y le indicamos las veces que se repite
especifica = float(input("\nIngresa una calificación específica para buscar en tu lista de calificaciones: "))
conteo = 0
for calificacion in calificaciones:
    if calificacion < 0 or calificacion > 100:
        continue
    if calificacion == especifica:
        conteo += 1
    if conteo > 10:
        print("Hay mas de 10 calificaciones con ese valor.")
        break
print("La calificación", especifica, "aparece", conteo, "veces.")
print("Fin del programa.")
