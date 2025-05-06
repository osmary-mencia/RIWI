import os
os.system('cls')

print('Contador de números positivos')

contador = 0  # Empezamos el contador en 0

for i in range(10):  # Se repite 10 veces
    numero = float(input(f'Ingresa el número {i + 1}: '))
    if numero > 0:
        contador += 1  # Sumamos 1 si el número es positivo

print(f'Se ingresaron {contador} números positivos.')
