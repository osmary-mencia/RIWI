"""
🧠 RETO 1: Diccionario de contactos
📌 Objetivo: Crea un sistema donde el usuario pueda agregar contactos 
con nombre y número de teléfono usando un diccionario.
🧩 Detalles:
Usa while True para mostrar un menú con estas opciones:
    Agregar contacto
    Ver contactos
    Buscar un contacto por nombre
    Salir

Guarda los contactos en un diccionario así:
contactos = {
    "Ana": "04141234567",
    "Luis": "04242345678"
}
Si el usuario busca un contacto que no existe, muestra: "Contacto no encontrado" (usa .get()).
"""
contactos = {}

while True:
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("\nDICCIONARIO DE CONTACTOS\n")
    
    print('MENU DE OPCIONES\n')
    print('1. Agregar contacto.')
    print('2. Ver contactos.')
    print('3. Buscar un contacto por nombre.')
    print('0. Preciona o para SALIR o escribe la palabra salir.fr\n')
    
    opcion = input('Ingresa una opcion del menu: ').upper()
    
    if opcion == '1':
        
        nombre_contacto = input('\nIngresa el nombre de tu contacto: ').strip().title()
        
        if nombre_contacto in contactos:
            print('\nEste contacto ya existe.')
        
        try:
            numero_contacto =int(input('\nIngresa el numero sin puntos y comas: '))
            if numero_contacto < 0:
                print('\nError. El numero no puede ser negativo.')
            else:   
                contactos[nombre_contacto]= numero_contacto
        except ValueError:
            print('\nEntrada inválida. Debes ingresar números.')
        
    
    elif opcion == '2':
        print('\nLista de contactos: \n')
        
        for clave, valor in contactos.items():
            print(f'{clave} : {valor}\n')
    
    elif opcion == '3':
        
        nombre_contacto = input('\nIngresa el nombre del contacto que deseas buscar: ').strip().title()
        contacto = contactos.get(nombre_contacto, 'Contacto no encontrado.')
        
        if contacto != 'Contacto no encontrado.':
            print(f'\nNombre: {nombre_contacto}\nNúmero: {contacto}')
        else:
            print(f'\n{contacto}')

        
    elif opcion == 'SALIR' or opcion == '0':
        print('Fin del programa')
        break
    else:
        print('\nERROR!! Ingresa una opcion valida del menu.')
        
            