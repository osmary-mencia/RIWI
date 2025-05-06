numero = int(input('Escribe un numero positivo (0 para salir): '))
suma = 0
while numero != 0:
    if numero > 0:
        suma += numero
    else: 
        print('Numero no valido. intente de nuevo')
    numero = int(input('Escribe otro numero positivo (0 para salir): '))
print(f'La suma total es: {suma}')