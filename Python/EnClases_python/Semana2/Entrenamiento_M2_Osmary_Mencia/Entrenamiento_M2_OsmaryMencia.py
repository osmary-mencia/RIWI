print('******************************************************')
print('* SISTEMA PARA EVALUAR CALIFICACIONES Y ESTADISTICAS *')
print('******************************************************\n')

while True:
    try:
        #Se le pide al usuario que ingrese un calificacion en el rango especificado
        nota = float(input("Ingresa una calificacion entre 0 y 100: "))
        
        #Si la nota no esta en el rango le retorna un mensaje de intentar de nuevo porque no esta en el rango
        if nota >= 0 and nota <=100:
            break
        else:
            print("\nCalificacion invalida." , nota,  "se encuentra fuera del rango permitido del 0 al 100.")
            print("INTENTA DE NUEVO\n")
            
    #si el usuario ingresa un valor no numerico le retorna un mensaje de error y que lo intente de nuevo
    except ValueError:
        print("¡ERROR! Debes ingresar una calificion valida.")
        print("\nINTENTALO DE NUEVO!")
        continue
    
#Si la nota esta en el rango permitido le dice si aprobo o no 
if nota >= 70:
    print("\n¡FELICIDADES :)! Has aprobado.")
    print("BUEN TRABAJO!! sigue asi...")
else:
    print("\n¡OH NO :(! Has reprobado.")
    print("SIGUE ESTUDIANDO!! en la próxima te irá mejor...")

while True:
    print("\n*** SISTEMA DE PROMEDIO DE CALIFICACIONES ***")
    
    #Se pide al usuario que ingrese una lista de notas separadas por comas para calcular el promedio total
    entrada = input("\nIngresa una lista de calificaciones separadas por comas: ")
    try:
        calificaciones = []     #Definimos la lista que almacenara la calificaciones ingresadas
        for x in entrada.split(","):    #Permite la entrada de datos separados por coma
            valor = float(x.strip())    #Borra los espacios en blanco y convierte el valor en un flotante 
            if valor >= 0 and valor <=100:       # Verifica que esté en el rango permitido 
                calificaciones.append(valor) #Guarda el valor ingresado en la lista
            else: #Si hay un valor que este fuera del rango permitido le retorna un mensaje de error y que lo intente de nuevo
                print("¡ERROR! Hay valores fuera del rango permitido del 0 al 100.")
                print("INTENTA DE NUEVO")
                break
        if calificaciones: #si las calificaciones ingresadas estan en el rango permitido se calcula el promedio total de ellas
            promedio = sum(calificaciones) / len(calificaciones) 
            print("\nEl promedio es:", round(promedio, 2))
            if promedio >= 70:#Si es mayor a 70 le retorna un mesaje de aprobado
                print("¡FELICIDADES :)! Has aprobado.")
                print("BUEN TRABAJO!! sigue asi...")
            else:#Si no es mayor a 70 le retorna un mesaje reprobado
                print("¡OH NO :(! Has reprobado.")
                print("SIGUE ESTUDIANDO!! en la proxima te ira mejor...")
            break
       
    #en caso de que se ingrese un valor no numerico se retorna un mesaje de error y que lo intente de nuevo
    except ValueError:
        print("¡ERROR! Ingresaste un valor no numérico o te falto separar las notas con comas.")
        print("\nINTENTA DE NUEVO")
        continue



while True: #Contar calificaciones mayores a un valor.
    try: 
        #le pedimos el usuario que ingrese una calificaion en especifico para decirle cuantas notas son mayores asa
        valor = float(input("\nIngresa una calificacion para comparar cuantas calificaciones son mayores esa: "))
        
        if valor >= 0 and valor <=100: # Verificamos que esté en el rango permitido 
            break
        else: #Si no le retorna un mensaje de error y que lo intente de nuevo
            print("¡ERROR! Ingresaste un valor fuera del rango permitido del 0 al 100.")
            print("INTENTA DE NUEVO")
            continue
    except ValueError:
        #En caso de que ingrese un valor no numerico le retorna un mensaje de error y que lo intente de nuevo
        print("\n¡ERROR! Ingresaste un valor NO numerico.")
        print("INTENTA DE NUEVO")
        
#Si el valor ingresado esta en el rango permitido se ejecula la condicion
contador = 0
indice = 0
while indice < len(calificaciones): #mientras indice sea menor a la cantidad de calificaciones que tiene la lista
    #se ejecutara esta funcion
    if calificaciones[indice] > valor:
        contador += 1
    indice += 1 
#Se imprimiran la cantidad de calificaciones que hay mayor al valor ingresado
print("Cantidad de calificaciones mayores a", valor, " son: ", contador)

#Verificar y contar cuentas veces se repite una calificacion
while True: 
    try:
        #le pedimos al usuario que ingrese un calificacion especifica y le indicamos las veces que se repite
        especifica_nota = float(input("\nIngresa una calificación específica para buscar cuantas veces se repite en tu lista de calificaciones: "))
        if especifica_nota >= 0 and especifica_nota <=100: # Verificamos que esté en el rango permitido 
            break
        else: #Si no le retorna un mensaje de error y que lo intente de nuevo
            print("¡ERROR! Ingresaste un fuera del rango permitido del 0 al 100.")
            print("INTENTA DE NUEVO")
            continue
    except ValueError:#En caso de que ingrese un valor no numerico le retorna un mensaje de error y que lo intente de nuevo
        print("\n¡ERROR! Ingresaste un valor NO numerico.")
        print("INTENTA DE NUEVO")
        
#Si el valor ingresado esta en el rango permitido se ejecula la condicion
conteo = 0
for calificacion in calificaciones:
    if calificacion == especifica_nota:
        conteo += 1
if conteo == 0: #SI el usuario ingresa un valor que no esta en la lita o no se repite se retorna el mensaje de abajo
    print("No se ha encontrado ninguna coincidencia dentro de las calificiones.")
#Se imprime en pantalla la calificacion especifica y las veces que esta se repitio      
print("La calificación", especifica_nota, "se repite ", conteo, "veces.")

print("Fin del programa.")