print('\nIntroduce dos numeros para comparar.\n')

num1 = float(input('Ingresa el primer numero: '))
num2 = float(input('Ingresa el segundo numero: '))

if num1 != num2:
    print('\nSon numeros diferentes...')
if num1 == num2:
    print('Son numeros iguales...')
if num1 > num2:
    print(f'El {num1} es mayor que {num2}')
if num1 < num2:
    print(f'El {num1} es menor que {num2}')
if num1 <= num2:
    print(f'El numero {num1} es menor o igual que {num2}')
if num1 >= num2:
    print(f'El numero {num1} es mayor o igual que {num2}')