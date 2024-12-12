#tipo boolean (bool en python)

a=True
b=False

d=0
f=0

if a or b == True:
    print('verdadero')
else:
    print('falso')

if a == False:
    f=45
elif b == False:
    d=75
else:
    print('todo es falso')

print('d',d)
print('f',f)

z=3<2
y=6>3
xy=6>=6
yx=7<=5

print(z)
print(y)
print(xy)
print(yx)