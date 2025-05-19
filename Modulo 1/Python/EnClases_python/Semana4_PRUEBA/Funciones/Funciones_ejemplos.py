"""
🔹 Parte 1: def → Funciones normales
📌 ¿Qué es una función? Una función es un bloque de código que se puede usar cuando lo necesites, 
en vez de repetir lo mismo varias veces.
"""
print("\n✨ Sintaxis básica:\n")

def saludar():
    print("¡Hola, Osmary!")

saludar()  # Llama a la función

print('\n✅ Función con parámetros:\n')

def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("Ana")
saludar_persona("Luis")

print('\n✅ Función que devuelve algo (return):\n')

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)  # Imprime 8

print('\n🔹 Parte 2: lambda → Funciones anónimas, más cortas\n')
#Una función lambda es como una función rápida, sin nombre, para cosas simples.
print('✨ Sintaxis básica:\n')
sumar = lambda a, b: a + b
print(sumar(3, 4))  # Resultado: 7

print('\nEs igual a:\n')

def sumar(a, b):
    return a + b

print('\n⚡ Uso común: con map, filter, sorted\n')

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]
