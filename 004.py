#
n1 = input('Digite algo:')
print('Tipo primitivo:', type(n1))
print('Tem espaço?', n1.isspace())
print('Ele é um numero?', n1.isnumeric())
print('Ele é uma palavra?', n1.isalpha())
print('Ele é alfanumerico?', n1.isalnum())
print('Está em maiusculo?', n1.isupper())
print('Esta em minusculo?', n1.islower())
print('Esta capitalizado?', n1.istitle())
