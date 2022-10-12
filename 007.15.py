#Aluguel de carros
da = int(input('Quantos dias voce usou o carro alugado? '))
km = float(input('Quantos quilometros rodados? '))
d = 60*da
k = 0.15*km
print('O total a pagar será de: R$ {}'.format(d+k))
