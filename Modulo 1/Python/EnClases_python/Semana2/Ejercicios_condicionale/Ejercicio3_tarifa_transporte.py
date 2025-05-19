print('-----Tarifa de transporte segun Dia y Hora-----')

dia_laboral = input('Ingresa si tu dia es laboral. (SI) o (NO): ').upper()

if dia_laboral == 'SI':
    hora = int(input('Ingresa una hora de 0 a las 23: '))
    if hora >=7 and hora <=9 or hora >=17 and hora <=19:
        precio_hora_pico = 3400
        print(f'Estas en hora PICO el pasaje tiene un valor de {precio_hora_pico}')
    else:
        precio = 3300
        print(f'No estas en hora PICO el pasaje tiene un valor de {precio}')

elif dia_laboral == 'NO':
    print('Es fin de semana, no estamos en dias laborales.')

else: 
    print('ERROR!! Ingresa una opcion valida (SI) o (NO)')