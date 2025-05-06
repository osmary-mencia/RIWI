data = input("Ingrese un numero entero: ")
# el type().__name__ nos sirve para saber el tipo de dato de una variable
print("El tipo de dato original: ", type(data).__name__)

'''
la cláusula try se utiliza para delimitar un bloque de código donde se espera que pueda ocurrir 
una excepción (error durante la ejecución). Si ocurre una excepción en el bloque try, el programa 
no se detiene inmediatamente, sino que la ejecución se "transfiere" al bloque except correspondiente
'''
try:
    # tambien podemos asignarle un tipo de dato a una variable y cambiar el original
    # en este caso cambiamos el tipo de dato de data pasando de "str(string)" a "int(integer)"
    data = int(data)    
except:
    print('No se puede realizar la operacion')

tipo_de_dato = type(data).__name__
print("El tipo de dato nuevo es: ", tipo_de_dato)