#Crea una tupla de 3 edades y usa un for para imprimir si cada edad es mayor de 18.

edades = (17,20,15)

for edad in edades:
    if edad > 18:
        print(f'Esta edad {edad} es mayor a 18.')
    else: 
        print(f'Esta edad {edad} no es mayor a 18')