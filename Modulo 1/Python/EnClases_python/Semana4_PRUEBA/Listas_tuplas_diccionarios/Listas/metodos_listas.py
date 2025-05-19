# Métodos más comunes para listas en Python

print("*" * 30)
print("|       Métodos para Listas        |")
print("*" * 30)
print()

# Creamos una lista de ejemplo
frutas = ["manzana", "banana", "uva"]
print("Lista original:", frutas)
print()

# 1. append() → Agrega un elemento al final
print("1. append: agrega un elemento al final de la lista")
frutas.append("naranja")
print("Lista actualizada:", frutas)
print()

# 2. insert() → Inserta un elemento en una posición específica
print("2. insert: inserta un elemento en una posición específica")
frutas.insert(1, "pera")  # Inserta "pera" en el índice 1
print("Lista actualizada:", frutas)
print()

# 3. remove() → Elimina un elemento por su valor
print("3. remove: elimina un elemento por su valor")
frutas.remove("banana")
print("Lista actualizada:", frutas)
print()

# 4. pop() → Elimina el último elemento (o el de una posición) y lo devuelve
print("4. pop: elimina y devuelve el último elemento (o uno específico)")
ultimo = frutas.pop()
print("Elemento eliminado:", ultimo)
print("Lista actualizada:", frutas)
print()

# 5. index() → Devuelve la posición de un elemento
print("5. index: muestra el índice (posición) de un elemento")
indice = frutas.index("manzana")
print("La 'manzana' está en la posición:", indice)
print()

# 6. count() → Cuenta cuántas veces aparece un valor
print("6. count: cuántas veces aparece un valor en la lista")
frutas.append("uva")
print("Lista con 'uva' repetida:", frutas)
print("Cantidad de 'uva':", frutas.count("uva"))
print()

# 7. sort() → Ordena la lista (alfabéticamente o numéricamente)
print("7. sort: ordena la lista alfabéticamente")
frutas.sort()
print("Lista ordenada:", frutas)
print()

# 8. reverse() → Invierte el orden de los elementos
print("8. reverse: invierte el orden de los elementos")
frutas.reverse()
print("Lista invertida:", frutas)
print()

# 9. clear() → Vacía completamente la lista
print("9. clear: elimina todos los elementos de la lista")
frutas.clear()
print("Lista vacía:", frutas)
