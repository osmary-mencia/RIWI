# definición de variables y entrada de datos

sueldo_actual = float(input("Ingresa tu sueldo actual: ").replace(".", ""))
porcentaje_aumento = float(input("Ingresa tu porcentaje de aumento: "))

# procedimiento

aumento = sueldo_actual * (porcentaje_aumento / 100)
sueldo_nuevo = sueldo_actual + aumento

# salida de datos
print(f"El nuevo sueldo es: {sueldo_nuevo}")
