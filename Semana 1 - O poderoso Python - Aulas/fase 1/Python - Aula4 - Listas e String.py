#listas e String
frase = 'Curso de python'
lista_nomes = ['joão', 'maria', 'willames', 'diego']

for i in range(len(lista_nomes)):
    print('PRIMEIRO USO DO SORTED')
    print ('posição do nome é: {} e o nome é: {}'.format(i+1, sorted(lista_nomes[i])))

for k in sorted(lista_nomes):
    print('SEGUNDO USO DO SORTED')
    print ('esse é o k  {} '.format(k))
    print('TERCEIRO USO DO SORTED')
    print(sorted(lista_nomes))
    
print('SLICE')
print(frase[9:21:2])
