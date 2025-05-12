"""
🧠 AHORA: NUEVO RETO PARA TI
📌 Reto mixto: juego de adivinar un número

Usa random.randint() para generar un número aleatorio entre 1 y 10.

Usa un while para pedirle al usuario que adivine el número.

Si el usuario adivina, muestra “¡Correcto!” y termina.

Si no, dile si el número es mayor o menor y vuelve a pedir.

"""
import random


print('\nAdivina el numero secreto entre el 1 al 10.')
numero_secreto = random.randint(1,10)
numero = int(input('Ingresa tu numero: '))


while numero != numero_secreto:
    if numero > numero_secreto:
        print('El numero es menor')

    else: 
        print('El numero es mayor')
    
    numero=int(input('Ingresa otro numero: '))
    
print('Adivinaste el numero secreto')