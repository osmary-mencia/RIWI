# Entrada datos

primer_numero_ingresado = float(input("Ingrese primer número - "))
segundo_numero_ingresado = float(input("Ingrese segundo número - "))

# None es un valor especial que representa la ausencia de un valor 
resultado = None

# Procesamiento 

print("suma - resta - multiplicacion")

# el ciclo While permite ejecutar un bloque de código repetidamente mientras una condición sea verdadera
# en este caso hacemos que el ciclo se repita siempre y cuando el valor de resultado sea diferente a "float"
# y el valor de resultado solo se asigna si se cumple uno de los casos del match.

while type(resultado).__name__ != 'float':
    operacion = input("Ingrese el tipo de operacion - ")

# El valor de resultado solo se cambiará si entramos en el match, como funciona el match?
# el match es una estructura de control que permite realizar coincidencia de patrones,
# es una alternativa más legible que los bloques if-elif-else cuando se necesitan comparar un valor con múltiples constantes

    match operacion : 
        case "suma" : 
            resultado = primer_numero_ingresado + segundo_numero_ingresado # Si el valor de operacion es igual a "suma", se cumple esto
        case "resta" :
            resultado = primer_numero_ingresado - segundo_numero_ingresado # Si el valor de operacion es igual a "resta", se cumple esto
        case "multiplicacion" :
            resultado = primer_numero_ingresado * segundo_numero_ingresado # Si el valor de operacion es igual a "multiplicacion", se cumple esto
        case _: # el caso _ (guion bajo) significa "por defecto", o sea que si no hay ninguna coincidencia en los casos, se ejecuta este bloque
            print("----------La operacion no es valida----------") # Si el valor de operacion no coincide a ninguno de los casos, se cumple esto

# Salida de datos

print(f"el resultado de la {operacion} es: {resultado}")