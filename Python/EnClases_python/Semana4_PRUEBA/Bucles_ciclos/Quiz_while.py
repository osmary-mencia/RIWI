"""
🔸 Reto 1 – Solo con while:
📌 Objetivo:
Usa un ciclo while para pedirle al usuario (con input()) que ingrese una contraseña.
El programa debe seguir pidiendo la contraseña hasta que el usuario escriba "python123".

🔍 Pista: usa un while con una condición que revise si la contraseña es incorrecta.
"""

contraseña_correcta = 'python123'

contraseña = input('Ingresa la contraseña: ')

while contraseña != contraseña_correcta:
    print('Contraseña incorrecta')
    contraseña = input('Intenta de nuevo: ')
print('Contraseña correcta')
    