# vacaciones=str(input('estás en vacaciones, s o n?: '))
# descanso=str(input('tienes días de descanso, s o n?: ' ))
#
# if vacaciones !='s' and vacaciones !='n' or descanso != 'n' and descanso !='s':
#     print('has ingresado un valor invalido, vuelve a intentarlo, s para si o n para no')
# elif vacaciones == 'n' or descanso == 'n':
#     print('no puedes ir al juego')
# elif vacaciones == 's' or descanso == 's':
#     print('puedes ir al juego')

vacaciones = True
descanso = True

if not (vacaciones and descanso):
    print('no puedes ir al juego')
else:
    print('puedes ir al juego')


