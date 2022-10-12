#Aumento de salario
n = float(input('Qual o seu salario atual do funcionario: R$ '))
print('Um funcionario que recebia R${:.2f}, com aumento de 15%, passa a receber R${:.2f}.'.format(n, n+(n*15/100)))
