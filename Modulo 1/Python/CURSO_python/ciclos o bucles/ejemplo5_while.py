secreto = 11
intento = None
intentos = 0 

while intento != secreto:
    
    try:    
        intento = int(input('Adivina el numero secreto del 1 al 15:  '))
        
        if intento > 15 or intento <1:
            print('Lo siento ingresaste un valor fuera del rango permitido, TRY AGAIN')
        
        intentos += 1
        
        if intento < secreto:
            print('El numero es mas alto')
        elif intento > secreto:
            print('El numero es mas bajo.')
        else:
            print(f'LO LOGRASTE! en {intentos} intentos.')
            break
        
    except ValueError:
        print('Ingresaste un valor no numerico, TRY AGAIN')
        
