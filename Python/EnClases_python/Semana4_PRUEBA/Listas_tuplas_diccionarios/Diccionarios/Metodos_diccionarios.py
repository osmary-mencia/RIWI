# Métodos útiles de los diccionarios en Python

print("*" * 35)
print("|     Métodos útiles de Diccionarios     |")
print("*" * 35)
print()

# Creamos un diccionario de ejemplo
persona = {
    "nombre": "Osmary",
    "edad": 20,
    "profesion": "Desarrolladora"
}

print("Diccionario original:", persona)
print()

# 1. get() → Obtiene el valor de una clave, si no existe devuelve un valor por defecto
print("1. get: obtiene el valor de una clave de forma segura")
print("Edad:", persona.get("edad"))
print("Ciudad (clave no existente):", persona.get("ciudad", "No disponible"))
print()

# 2. keys() → Devuelve todas las claves del diccionario
print("2. keys: muestra todas las claves")
print("Claves:", list(persona.keys()))
print()

# 3. values() → Devuelve todos los valores del diccionario
print("3. values: muestra todos los valores")
print("Valores:", list(persona.values()))
print()

# 4. items() → Devuelve una lista de tuplas (clave, valor)
print("4. items: muestra claves y valores juntos")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
print()

# 5. update() → Agrega o actualiza claves en el diccionario
print("5. update: actualiza o agrega una nueva clave y valor")
persona.update({"edad": 21, "ciudad": "Bogotá"})
print("Diccionario actualizado:", persona)
print()

# 6. pop() → Elimina una clave y devuelve su valor
print("6. pop: elimina una clave específica y devuelve su valor")
profesion = persona.pop("profesion")
print("Valor eliminado:", profesion)
print("Diccionario actual:", persona)
print()

# 7. popitem() → Elimina y devuelve el último par clave:valor agregado
print("7. popitem: elimina el último elemento insertado")
ultimo = persona.popitem()
print("Elemento eliminado:", ultimo)
print("Diccionario actual:", persona)
print()

# 8. clear() → Elimina todos los elementos del diccionario
print("8. clear: elimina todos los elementos")
persona.clear()
print("Diccionario vacío:", persona)
