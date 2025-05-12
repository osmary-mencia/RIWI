"""
🔸 for como uso general (más allá de listas, tuplas y diccionarios)
Puedes usar for con:

1. range() – Para repetir un número específico de veces
"""

for i in range(5):
    print(i)
    
print('\nOtra forma de hacerlo\n')

for i in range(1,6):
    print(i)
    
print('\nSobre cadenas de texto\n')

texto = 'Hola'

for letra in texto:
    print(letra , end=('-' ))