#Ler nome completo que mostra: todas as letras mauisculas, minusculas,total de letras e quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo:')).strip()
list = [nome]
print('Em letras maiusculas seu nome fica:',nome.upper())
print('Em letras minusculas seu nome fica:',nome.lower())
print('Seu nome sem espaços tem o total de {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))

