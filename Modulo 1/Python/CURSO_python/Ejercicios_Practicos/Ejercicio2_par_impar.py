print('====================================================')
print('|| Sistema que valida si un numero es par o impar ||')
print('====================================================\n')

numero = int(input('Por favor, Ingresa un numero entero: '))

if numero % 2 == 0:
    print (f'El numero {numero}, es un numero par')
elif numero % 2 == 1:
    print(f'El numero {numero}, es un numero impar.')
