#difinicion de variables y entrada de datos

num_uno = int(input("Ingresa tu primer numero: "))
num_dos = int(input("Ingresa tu segundo numero: "))

#verificar si ambos numeros son mayores que 10

if num_uno > 10 and num_dos > 10:
    print("Ambos numeros son mayores que 10")
elif num_uno > 10 or num_dos > 10: #verificar si algunos de los dos es mayor que 10
    print("Al menos uno de los dos numeros es mayor que 10.")
else:
    print("Ninguno de los dos numeros es mayor que 10")
    



