#difinicion de variables y entrada de datos

num_uno = int(input("Ingresa tu primer numero: "))
num_dos = int(input("Ingresa tu segundo numero: "))

#procedimiento
if num_uno > num_dos:
    print(f"El numero {num_uno} es mayor que el numero  {num_dos}")
else:
    if num_dos > num_uno: 
        print(f"El numero {num_dos} es mayor que el numero {num_uno}")
    else:
        print("Los dos numeros son iguales")