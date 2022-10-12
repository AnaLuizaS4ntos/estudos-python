#leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
n1 = int(input('Digite um numero: '))
#o numero ocupa 0 1 2 3 espaços
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
