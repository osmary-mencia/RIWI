tu_nota = float(input("Ingesa tu nota: "))

if tu_nota >= 0 and tu_nota <1:
    print(f'Tu nota es {tu_nota}, no tienes ningun premio')
elif tu_nota >=1 and tu_nota <2:
    print(f'Tu nota es {tu_nota}, tienes un pemio de 100 puntos')
elif tu_nota >= 2 and tu_nota <3:
    print(f'Tu nota es {tu_nota}, tienes un premio de 200 puntos')
elif tu_nota >= 3 and tu_nota <4:
    print(f'Tu nota es {tu_nota}, tienes un premio de 300 puntos')
elif tu_nota >=4 and tu_nota <5:
    print(f'Tu nota es {tu_nota}, Tienes un premio de 400 puntos')
elif tu_nota ==5:
    print(f'Tu nota es {tu_nota}, Tienes un premio de 500 puntos')
else:
    print(f'Lo siento tu nota no esta en el rango permitido de 0 a 5 :3')