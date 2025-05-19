"""
Son colecciones de pares clave:valor.
se escricriben con llaves {}

"""
persona = {
    'nombre': 'ana',
    'edad': 25,
    'ciudad': 'barranquilla'
}

print(persona['nombre']) #-> imprime el valor que contiene la clave nombre
persona['edad']= 26 #-> actualiza el valor de la clave edad
persona['profesion'] = 'Ingeneria' # esto agrega un nuevo clave:valor en el diccionario persona
print(persona) #imprime el diccionario

#diccionario editado
print('\nDiccionario editado\n')
persona['nombre'] = 'Osmary'
persona['edad']= 20
print(persona)