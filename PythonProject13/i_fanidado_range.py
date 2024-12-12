# edad = int(input('ingresa tu edad para saber si estás en el rango de los 20\'s o de los 30\'s: '))
#
# veintes = edad>=20 and edad<30
#
# treintas = edad>=30 and edad<40
#
# if veintes or treintas:
#     if veintes:
#         print('estás dentro del rango de los 20\'s')
#     elif treintas:
#         print('estás dentro del rango de los 30\'s')
# else:
#     print('estás fuera del rango')

# edad=int(input('ingresa tu edad: '))
# if edad>=20 and edad<30 or edad>=30 and edad<40:
#     if edad>=20 and edad<30:
#         print('estás dentro del rango de los 20\'s')
#     elif edad>=30 and edad<40:
#         print('estás dentro del rango de los 30\'s')
# else:
#     print('estás fuera de rango')

# edad=int(input('ingresa tu edad para saber si estás dentro del rango de los 20\'s o de los 30\'s: '))
#
# if 20<=edad<30 or 30<=edad<40:
#     print('estás dentro del rango de los 20\'s o de los 30\'s')
# else:
#     print('estás fuera del rango de los 20\'s y 30\'s')

# vacaciones=input('estás en vacaciones: s o n?: ')
# descanso=input('estás en día de descanso: s o n?: ')

# if vacaciones != 's' and vacaciones != 'n' or descanso != 's' and descanso != 'n':
#     print('has introducido un valor invalido, vuelve a intentarlo, ingresa s para si o n para no')
# elif vacaciones =='s' or descanso=='s':
#     print('puedes ir al juego')
# else:
#     print('no puedes ir al juego')

vacaciones = True
descanso = False

if not (vacaciones or descanso):
    print('no puedes ir al juego')
else:
    print('puedes ir al juego')