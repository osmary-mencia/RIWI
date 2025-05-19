edad = int(input('Ingrese su  edad: '))

if edad <0: 
    print('Lo siento tu edad no puede ser un numero negativo')
else:
    if edad <18:
        print(f'Tu tienes {edad}, aun eres menor de edad.')
    elif edad >=18 and edad <=30:
        print(f'Tu tienes {edad}, ya eres un adulto joven. ')
    elif edad >=31 and edad <65:
        print(f'Tu tienes {edad}, ya eres un adulto maduro. ')
    elif edad >65:
        print(f'Tu tienes {edad}, ya eres un adulto mayor. ')

    
