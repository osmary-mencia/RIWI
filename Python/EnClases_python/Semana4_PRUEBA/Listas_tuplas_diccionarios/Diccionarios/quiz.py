#Crea un diccionario con 2 claves: "nombre" y "profesion". 
# Usa .get() para obtener "edad" con valor por defecto "Desconocida".

persona = {
    'nombre': 'Osmary',
    'profesion': 'Desarrollo de software'
}
print('\n')
print(persona)
print('\n')

print(persona.get('edad', 'Desconocida'))