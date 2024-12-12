edad=int(input('introduce tu edad para comprobar si eres mayor o menor de edad: '))
if 3<edad<18:
    print(f'tienes {edad} años, eres menor de edad')
elif 18<=edad<111:
    print(f'tienes {edad} años, eres mayor de edad')
else:
    print('has introducido una edad incorrecta, debes introducir un valor entre 4 a 110 ')

# edadm=18
#
# edadUs=int(input('ingresa tu edad: '))
#
# if edadUs>=edadm:
#     print(f'tienes {edadUs} años, eres mayor de edad')
# else:
#     print(f'tienes {edadUs} años, eres menor de edad')