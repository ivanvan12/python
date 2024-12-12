print('Proporcione los siguientes datos del libro:')
nombre=input('Cuál es el nombre del libro?: ')
id=int(input('Cuál es el ID del libro?: '))
precio=float(input('Ingresa el precio: '))
envio=(input('El envio es gratuito? s o n?: '))
ee=''

if envio=='s':

    envio=True
    ee='Sí'
elif envio=='n':
    envio=False
    ee='No'
else:
    print('error, has ingresado un dato invalido, vuelve a repetirlo usando s para si y n para no en minusculas.')

print(f'''
Nombre: {nombre}
ID: {id}
Precio: {precio}
Envio gratuito: {ee}
''')
