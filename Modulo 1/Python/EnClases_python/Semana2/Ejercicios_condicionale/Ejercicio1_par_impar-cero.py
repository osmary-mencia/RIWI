#Entrada de datos
numero = int(input("Ingrese un numero: "))

#Procedimiento 
if numero > 0 :
    if numero % 2 == 0:
        print(f"El numero {numero} es un numero positivo par")
    else:
        print(f'El numero {numero} es un numero positivo impar')
elif numero < 0:
    if numero % 2 == 0:
        print(f'El numero {numero}, es numero negativo par')
    else:
        print(f'El numero {numero}, es un numero negativo impar')
else:
    print(f'El numero es cero')