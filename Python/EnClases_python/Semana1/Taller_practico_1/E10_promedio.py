#Se definen tres variables y la entrada de datos

num1 = float(input(" ¿Cual es tu primer numero: "))
num2 = float(input(" ¿Cual es tu segundo numero: "))
num3 = float(input(" ¿Cual es tu tercer numero: "))

#sacer promedio de tres numeros
promedio = (num1+num2+num3)/3

#salida de datos
print(f"El promedio de los tres numeros es: {promedio: .2f}")
    