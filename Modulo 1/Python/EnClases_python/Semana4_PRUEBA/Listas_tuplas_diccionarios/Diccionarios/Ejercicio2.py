#Crea un diccionario con 3 palabras y sus significados. 
#Usa un for para imprimir algo como: "La palabra <clave> significa <valor>".

print('\nPalabras en español y si significado en ingles\n')

palabras_significado = {
    'Hola' : 'Hi o hello',
    'Chao' : 'Goodbye',
    'Lindo': 'Cute'
}

for clave, valor in palabras_significado.items():
    print(f'La palabra {clave} significa {valor}')