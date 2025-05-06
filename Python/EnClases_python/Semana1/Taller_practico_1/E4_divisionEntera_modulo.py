#difinicion de variables y entrada de datos

num_uno = int(input("Ingresa tu primer numero: "))
num_dos = int(input("Ingresa tu segundo numero: "))

#procedimiento
division = num_uno // num_dos
modulo = num_uno % num_dos

#Salida de datos
print(f"El resultado de la division entera es: {division}")
print(f"El resultado del modulo es: {modulo}")