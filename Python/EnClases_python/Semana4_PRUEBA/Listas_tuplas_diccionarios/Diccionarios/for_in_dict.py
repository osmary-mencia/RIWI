"""
🔄 ¿Qué es el ciclo for?
Se usa para repetir instrucciones por cada elemento de una colección (como una lista, tupla o diccionario).

"""
# For in diccionarios
persona = {
    'nombre': 'Osmary',
    'edad': 20
}

# Tiene 3 formas principales:

# 1. solo las claves:
#Imprime las claves del diccionario 
print('Solos claves')
for clave in persona:
    print(clave)

#Otra forma de hacerlo es:
"""
KEYS()

Devuelve todas las claves del diccionario en un dict_keys, 
para facilitar su posterior manejo te recomiendo convertirlo en una lista
"""
print('\nOtra forma de hacerlo\n')
for clave in persona.keys():
    print(clave)
print()
#----------------------------------
#2. Clave y valor:
print('Clave y valor\n')
#Imprime las claves y el valor
for clave, valor in persona.items():
    print(f'{clave} : {valor}')

#otra forma de hacerlo es 
print('\nOtra forma de hacerlo\n')
items = dict(persona.items())
print(items)

#3. solo valores:
print('\nSolos valores\n')
for valor in persona.values():
    print(valor)
    
#otra forma de hacerlo es 
print('\nOtra forma de hacerlo\n')

valores = list(persona.values())
print(valores)