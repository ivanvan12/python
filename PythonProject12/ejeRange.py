edad=int(input('introduce tu edad para saber si estás entre los 20s o los 30s: '))

veintes= 20<=edad<30

print(veintes)

treintas= edad>=30 and edad<40

print(treintas)

if veintes or treintas:
    print('estás dentro del rango de los 20\'s o de los 30\'s')
else:
    print("'estás fuera de rango de los' 20s' y de los 30s'")