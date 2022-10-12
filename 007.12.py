#Desconto
n = float(input('Qual é o preço do produto? R$ '))
print('O produto custava R${} e com o desconto de 5% o valor será de R${:.2f}'.format(n, n-(n*5/100)))