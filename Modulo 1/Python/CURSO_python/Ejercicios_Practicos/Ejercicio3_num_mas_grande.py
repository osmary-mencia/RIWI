print('*******************************************************************')
print('* Sistema para validar ¿Cual es el numero mas grande de los tres? *')
print('*******************************************************************\n')

num_1 = int(input('Ingresa el primer numero: '))
num_2 = int(input('Ingresa el segundo numero: '))
num_3 = int(input('Ingresa el tercer numero: '))

if num_1 > num_2 and num_1 > num_3:
    print(f'El numero {num_1} es el mas grande de los tres')
elif num_2 > num_3:
    print(f'El numero {num_2} es el mas grande de los tres')
else:
    print(f'El numero {num_3} es el mas grande de los tres')