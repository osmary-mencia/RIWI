def calculadora_aritmetica (operacion_aritmetica, num_uno, num_dos):
    
    resultado_aritmetico = 0
    opcion_ejecutada = True
    mensaje = ""
    
    if operacion_aritmetica == 'suma':
        resultado_aritmetico = num_uno + num_dos
        
    elif operacion_aritmetica == 'resta':
        resultado_aritmetico = num_uno - num_dos
    
    elif operacion_aritmetica == 'multiplicacion':
        resultado_aritmetico = num_uno * num_dos
        
    elif operacion_aritmetica == 'division':
        resultado_aritmetico = num_uno / num_dos
    else:
        opcion_ejecutada = False
        mensaje = 'Opcion invalida'
        
    return {
        'operacion_aritmetica': operacion_aritmetica,
        'resultado_aritmetico': resultado_aritmetico,
        'mensaje': mensaje,
        'opcion_ejecutada': opcion_ejecutada
    }

primer_dato_num = int(input('Ingrese el primer valor: '))
segundo_dato_num = int(input('Ingrese el segundo valor: '))
operacion = input('Esccriba la opcion: ')

resultado = calculadora_aritmetica(operacion, primer_dato_num, segundo_dato_num)

if resultado ['operacion_aritmetica']:
    print(resultado['resultado_aritmetico'])
else:
    print(resultado['mensaje'])

print(resultado)