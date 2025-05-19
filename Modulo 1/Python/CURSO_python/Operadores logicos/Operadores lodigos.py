"""
permiten agrupar condiciones logicas dentro de unas misma condicion,|
es decir, que con los operadores logicos podemos usar multiples relaciones 
dentro de la misma condicion logica

"""
#conjuncion -------------------------------------------------------------

print('Conjuncion (and)')

num_uno = int(input('Escribe un numero que sea mayor a 2 y menor a 5: '))

if num_uno > 2 and num_uno <5:
    print(f'El numero {num_uno} cumple con la condicion')
else:
    print(f'El numero {num_uno} no cumple con la condicion \n')
    
#Disyuncion -----------------------------------------------------

print('Disyuncion (or)')

palabra = input('Para cumplir con loa condicion escribe "si" o "yes": ')

if palabra == 'si' or palabra == 'yes':
    print(f'La condicion se ha cumplido\n')
else: 
    print('La condicion no se ha cumplido\n')
    
#negacion --------------------------------------------------------------

print('Negacion (not)')

num_uno = int(input('Introduce un numero igual a 5:'))

if  not num_uno == 5:
    print(f'El numero es diferente a 5 y si se cumple la condicion\n')
else:
    print('El numero es igual a 5 y no cumple la condicion\n')