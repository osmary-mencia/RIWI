import os
os.system ('cls')

print('===============================')
print('CONVERTIDOR DE NUMEROS A LETRAS')
print('===============================')

num = int(input('Cual es el numero que deseas convertir: '))

if num == 1:
    print(f'El numero {num} es "Uno".')
elif num == 2:
    print(f'El numero {num} es "Dos".')
elif num == 3:
    print(f'El numero {num} es "Tres".')
elif num == 4:
    print(f'El numero {num} es "Cuatro".')
elif num == 5:
    print(f'El numero {num} es "Cinco".')
else:
    print('Lo siento!! Este numero aun no se encuentra registrado. ')
    print('Intenta con un numero del 1 al 5')