#Teorema de pitagoras, HIPOTENUSA
from math import sin, cos, tan, radians
n = float(input('Digite o Cateto Oposto: '))
n1 = float(input('Digite o Cateto Adjacente: '))
co = n**2
ca = n1**2
h = (co+ca)**(1/2)
#OR MATH.HYPOT(CO, CA)
print('A hipotenusa vai medir {:.2f}'.format(h))

