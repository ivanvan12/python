# nro=int(input('ingrese un #ro entre 1 y 100: '))
#
# if 1<=nro<=100:
#     print(f'el #ro {nro} está dentro del rango de 1 a 100')
# else:
#     print(f'el #ro {nro} está fuera del rango del 1 al 100')

#num = int(input('ingresa un número entre 1 y 10: '))

# if num>=1 and num<=10:
#     print(f'el número {num}, está dentro del rando de 1 al 10')
# else:
#     print(f'el número {num}, está fuera del rango del 1 al 10')

numero0=int(input('ingrese un numero para saber si esta en el rango entre 0 y 5: '))

rango_min=0
rango_max=5

conca=numero0>=rango_min and numero0<=rango_max

if conca:
    print(f'el número {numero0} está dentro del rango de 0 a 5')
else:
    print(f'el número {numero0} no está dentro del rango de 0 a 5')