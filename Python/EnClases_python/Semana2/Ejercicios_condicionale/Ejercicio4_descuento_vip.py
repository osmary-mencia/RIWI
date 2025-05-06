compra = float(input('Ingrese el monto de su compra: '))
cliente = input('¿Tienes una membrecia VIP?\nSI\nNO: ').strip().upper()

if cliente == 'SI':
    if compra >=500:
        descuento = (compra * 20)/100
        descuento_aplicado = compra - descuento
        print(f'Como eres un cliente VIP, tienes un descuento del 20% en compras mayores a 500')
        print(f'Tienes un descuento de {descuento} en tu compra. ')
        print(f'Total a pagar: {descuento_aplicado}')
    
    if compra <=500:
        descuento = (compra * 10)/100
        descuento_aplicado = compra - descuento
        print(f'Como eres un cliente VIP, tienes un descuento del 10% en compras menores de 500')
        print(f'Tienes un descuento de {descuento} en tu compra. ')
        print(f'Total a pagar: {descuento_aplicado}')

elif cliente == 'NO':
    if compra >=500:
        descuento = (compra * 5)/100
        descuento_aplicado = compra - descuento
        print(f'Como NO eres un cliente VIP, solo tienes un descuento del 5% en compras mayores de 500')
        print(f'Tienes un descuento de {descuento} en tu compra. ')
        print(f'Total a pagar: {descuento_aplicado}')
    if compra <500:
        descuento_aplicado = compra
        print(f'Como NO eres cliente VIP y tu compra no es mayor a 500 NO tienes ningun descuento')
        print(f'Total a pagar: {descuento_aplicado}')
else:
    print('ERROR!!Ingresa un opcion valida SI o NO')