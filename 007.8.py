#Conversão
n = float(input('Uma distancia em metros: '))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000
print('O valor da medida {} correspode:'.format(n))
print('{} Km'.format(km))
print('{} Hm'.format(hm))
print('{} Dam'.format(dam))
print('{:.0f} Dm'.format(dm))
print('{:.0f} Cm'.format(cm))
print('{:.0f} Mm'.format(mm))
