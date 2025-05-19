"""
🧩 Reto corto: Validación de entrada

📌 Objetivo: Pide al usuario que escriba una palabra que tenga más de 5 letras.
Sigue pidiendo con while hasta que lo haga correctamente.
Luego imprime: "Palabra aceptada: <palabra>".

🧠 Tip:
Usa len(palabra) para saber cuántas letras tiene.
"""

palabra = input('Ingresa un palabras con las de 5 letras: ')

while len(palabra) < 5:
    print(f'La palabra {palabra} no cumple los requisitos minimos')
    palabra = input('Ingresa otra palabra: ')
        
print(f'La palabra {palabra} es aceptada')