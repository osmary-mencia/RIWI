print('===========')
print('CONVERTIDOR')
print('=========== \n')

print('Menu de opciones: \n')

print('Presiona 1. Para convertinir de numero a palabra')
print('Presiona 2. Para convertinir de palabra a numero\n')

opcion = int(input('Cual es tu opcion deseada: '))

if opcion == 1:
    num = int(input('\nCual es el numero que deseas convertir a palabra: '))
    if num == 1:
        print(f'\nEl numero {num} en la letra es "Uno".')
    elif num == 2:
        print(f'\nEl numero {num} en la letra es "Dos".')
    elif num == 3:
        print(f'\nEl numero {num} en la letra es "Tres".')
    elif num == 4:
        print(f'\nEl numero {num} en la letra es "Cuatro".')
    elif num == 5:
        print(f'\nEl numero {num} en la letra es "Cinco".')
    else:
        print('\nLo siento!! Este numero aun no se encuentra registrado. ')
        print('Intenta con un numero del 1 al 5')
elif opcion == 2:
    print()
    palabra = (input('Cual es la palabra que deseas convertir a numero: ')).lower()
    if palabra == 'uno':
        print(f'La palabra "{palabra}" en numero es "1".')
    elif palabra == 'dos':
        print(f'La palabra "{palabra}" en numero es "2".')
    elif palabra == 'tres':
        print(f'La palabra "{palabra}" en numero es "3".')
    elif palabra == 'cuatro':
        print(f'La palabra "{palabra}" en numero es "4".')
    elif palabra == 'cinco':
        print(f'La palabra "{palabra}" en numero es "5".')
    else:
        print('Lo siento!! Esta palabra aun no se encuentra registrada. ')
        print('Intenta con una palabra del uno al cinco')
else:
    print('Lo siento!! esa opcion no se encuentra en el menu.')