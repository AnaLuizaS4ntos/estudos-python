#Pintar a parede
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
print('A sua parede tem a dimensão de {}x{}, a area é {}m²,'
       'Voce precisara de {}l de tinta para pintar a parede.'.format(l,a,l*a,(l*a)/2))
