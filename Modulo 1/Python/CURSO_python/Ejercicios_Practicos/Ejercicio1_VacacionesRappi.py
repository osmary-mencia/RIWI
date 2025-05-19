print('\n=============================')
print('|SISTEMA VACACIONAL DE RAPPI|')
print('=============================\n')

nombre_usuario = input('Ingresa tu nombre: ').title()
clave_departamento = int(input('Ingresa la clave de tu departamento: '))
años_servicio = float(input('Ingresa tu años de servicio: '))

if clave_departamento == 1:
    if años_servicio >= 1:
        print(f'El empleado {nombre_usuario}, tiene derecho a 6 dias de vacaciones.')
    elif años_servicio >= 2 and años_servicio <=6:
        print(f'El empleado {nombre_usuario}, tiene derecho a 14 dias de vanaciones.')
    elif años_servicio > 7:
        print(f'El empleado {nombre_usuario}, tiene derecho a 20 dias de vacaciones.')
    else:
        print(f'{nombre_usuario} LO SIENTO!! aun no tienes derecho a vacaciones.')
       
elif clave_departamento == 2:
    if años_servicio >= 1:
        print(f'El empleado {nombre_usuario}, tiene derecho a 7 dias de vacaciones.')
    elif años_servicio >= 2 and años_servicio <=6:
        print(f'El empleado {nombre_usuario}, tiene derecho a 15 dias de vanaciones.')
    elif años_servicio > 7:
        print(f'El empleado {nombre_usuario}, tiene derecho a 22 dias de vacaciones.')
    else:
        print('LO SIENTO!! aun no tienes derecho a vacaciones.')
        
elif clave_departamento == 3:
    if años_servicio >= 1:
        print(f'El empleado {nombre_usuario}, tiene derecho a 10 dias de vacaciones.')
    elif años_servicio >= 2 and años_servicio <=6:
        print(f'El empleado {nombre_usuario}, tiene derecho a 20 dias de vanaciones.')
    elif años_servicio > 7:
        print(f'El empleado {nombre_usuario}, tiene derecho a 30 dias de vacaciones.')
    else:
        print('LO SIENTO!! aun no tienes derecho a vacaciones.')
else:
    print('LO SIENTO!! esa clave de departamento no existe.')
    print('TRY AGAIN')