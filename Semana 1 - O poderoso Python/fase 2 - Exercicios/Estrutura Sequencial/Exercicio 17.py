'''
17 - Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou 
em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
tamanho = float(input('Quantos metros quadrados devem ser pintados: '))

litros = (tamanho / 6.0) * 1.1  
latas = int(litros / 18.0)
galoes = int(litros / 3.6)

if (litros % 18 != 0):
    latas += 1

if (litros % 3.6 != 0):
    galoes += 1

mist_Latas = int(litros / 18.0)
mist_Galoes = int((litros - (mist_Latas * 18.0)) / 3.6)
if ((litros - (mist_Latas * 18.0) % 3.6 != 0)):
    mist_Galoes += 1

print ("Quantidade de Latas: {} e o valor total: {} R$".format(latas, (latas*80)))
print ('Quantidade de Galoes: {} e o valor total: {} R$'.format(galoes,(galoes*25))) 
print ('Quantidade de Latas: {}, quantidade de Galoes: {} e o valor total: {} R$'.format(mist_Latas, mist_Galoes, (mist_Latas * 80)+(mist_Galoes*25)))