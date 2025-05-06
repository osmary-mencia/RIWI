print('\nCalculadora con una sola variable\n')
print('********************')
print('* Menu de opciones *')
print('********************')
print('1.Suma')
print('2.Resta')
print('3.Multiplicacion')
print('4.Division')
print('5.Divivsion entera')
print('6.Exponente')
print('7.Modulo o resto\n')

numero = int(input('Introduce la opcion deseada: '))

if numero == 1:
    print('Elegiste Suma\n')
    numero = float(input('Ingresa el primer numero: '))
    numero += float(input('Ingresa el primer numero: '))
    print(f'El resultado de la suma es: {numero}')
elif numero == 2:
    print('Elegiste Resta\n')
    numero = float(input('Ingresa el primer numero: '))
    numero -= float(input('Ingresa el primer numero: '))
    print(f'El resultado de la resta es: {numero}')
elif numero == 3:
    print('Elegiste Multiplicacion\n')
    numero = float(input('Ingresa el primer numero: '))
    numero *= float(input('Ingresa el primer numero: '))
    print(f'El resultado de la Multiplicacion es: {numero}')
elif numero == 4:
    print('Elegiste Division\n')
    numero = float(input('Ingresa el primer numero: '))
    numero /= float(input('Ingresa el primer numero: '))
    print(f'El resultado de la division es: {numero:.2f}')
elif numero == 5:
    print('Elegiste Division entera\n')
    numero = float(input('Ingresa el primer numero: '))
    numero //= float(input('Ingresa el primer numero: '))
    print(f'El resultado de la division entera es: {numero}')
elif numero == 6:
    print('Elegiste Exponete\n')
    numero = float(input('Ingresa el primer numero: '))
    numero **= float(input('Ingresa el primer numero: '))
    print(f'El resultado de la exponenciacion es: {numero}')
elif numero == 7:
    print('Elegiste Modulo o resto\n')
    numero = float(input('Ingresa el primer numero: '))
    numero %= float(input('Ingresa el primer numero: '))
    print(f'El resultado del modulo o resto es: {numero}')
else:
    print('Lo siento. Esa opcion no existe.')