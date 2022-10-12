#Do angulo achar sin cos e tan
from math import sin, cos, tan, radians
n = float(input('Digite um angulo: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print('O angulo {}, possui o Sin {:.2f}, Cos {:.2f} e Tan {:.2}'.format(n, s, c, t))
