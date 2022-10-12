#Porção inteira de um numero qual
from math import trunc
n = float(input('Digite um numero: '))
inteiro = trunc(n)
print('O numero {} tem a parte inteira {}.'.format(n, inteiro))
