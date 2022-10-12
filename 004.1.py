#UTILIZAÇÃO DO COMANDO FORMAT
n = input('Digite algo:')

print('O tipo primitivo é {}'.format(type(n)))
print('Posssui espaço? {}'.format(n.isspace()))
print('É um numero? {}'.format(n.isnumeric()))
print('Possui letra? {}'.format(n.isalpha()))
print('É alfanumerico? {}'.format(n.isalnum()))
print('É maiusculo? {}'.format(n.isupper()))
print('É minusculo? {}'.format(n.islower()))
print('É capitalizada? {}'.format(n.istitle()))
