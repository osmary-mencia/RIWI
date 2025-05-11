"""
🔹 Método .get() en diccionarios:
se usa para obtener el valor de una clave, igual que diccionario[clave], 
pero sin que dé error si la clave no existe.
"""

#🔸 Ejemplo sin .get()

persona = {
    'nombre': 'osmary',
    
}

print(persona['nombre'])
# print(persona['edad']) -> reforma un error ya que edad no existe

#🔸 Ejemplo con .get()

print(persona.get('nombre'))
print(persona.get('edad'))
print(persona.get('edad','No disponible'))