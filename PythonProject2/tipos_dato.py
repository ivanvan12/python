#hint es una pista que se les puede colocar o no a las variables para saber de que tipo son(int,str,bool,float,etc...)
#se puede poner dobles comillas "" o la comillas '' para definir una cadena o string, no afecta a la variable
a: int = 12
b: str = 'hola bebé'
d: str = "preñador"
c: float = 3.1416
e: bool = True
f: bool= False

print(type(a))
print(type(b))
print(type(c))
print(type(e))
print(type(f))
print(type(d))
#se puede poner una pista que no coincida con el tipo de variable

aa: int = 56
print(type(aa))

print(id(aa))

ab: int = 2
ac: float = 2.1111
ad: bool = True
ae: bool = False
af: str = 'nea szs'

print(type(ab))
print(id(ab))
print(type(ac))
print(id(ac))
print(type(ad))
print(id(ad))
print(type(ae))
print(id(ae))
print(type(af))
print(id(af))

