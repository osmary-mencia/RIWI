# 🔐 Palabra secreta que el jugador debe adivinar
palabra_secreta = "banana"

# 📜 Crea una lista con guiones para mostrar el progreso del jugador
# Ejemplo: ['_', '_', '_', '_', '_', '_']
progreso = ["_"] * len(palabra_secreta)

# ❤️ Vidas del jugador (cantidad de intentos fallidos permitidos)
vidas = 5

# 🕹️ Bucle principal del juego: se repite mientras queden guiones y vidas
while "_" in progreso and vidas > 0:
    # 🔎 Muestra el progreso actual uniendo la lista con espacios
    # '.join(progreso)' convierte la lista ['b', '_', '_'] en "b _ _"
    print("\nPalabra:", " ".join(progreso))
    
    # 🧠 Pide al jugador que ingrese una letra (minusculas y sin espacios)
    letra = input("Adivina una letra: ").lower().strip()

    # 🔄 Verifica si la letra está en la palabra
    if letra in palabra_secreta:
        # Si está, recorre la palabra y reemplaza el guión por la letra correcta
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                progreso[i] = letra
        print("✅ ¡Letra correcta!")
    else:
        # Si no está, se pierde una vida
        vidas -= 1
        print(f"❌ Esa letra no está. Te quedan {vidas} vidas.")

# 🏁 Fin del juego: ¿ganó o perdió?
if "_" not in progreso:
    print(f"\n🎉 ¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
else:
    print(f"\n💀 Te quedaste sin vidas. La palabra era: {palabra_secreta}")

"""
💡 ¿Qué hace .join()?
El método .join() convierte una lista de texto en una cadena unida por lo que tú elijas.
Ejemplo:

python
Copiar
Editar
lista = ['H', 'O', 'L', 'A']
print("".join(lista))     # Resultado: 'HOLA'
print("-".join(lista))    # Resultado: 'H-O-L-A'
print(" ".join(lista))    # Resultado: 'H O L A'
👉 En nuestro juego usamos " ".join(progreso) para que la palabra aparezca con espacios entre letras:
_ _ _ _ _ _ en lugar de ______
"""