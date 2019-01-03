''' 11 - Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.'''

int1, int2 = map(int, input("Forneça dois números inteiros: ").split())
real = float(input("Forneça um numero do conjunto dos números reais: "))
a = (int1 *2)*(int2 / 2)
print("a) o produto do dobro do primeiro com metade do segundo é: {}".format(a))
b = ((3*int1)+ real)
print("b) a soma do triplo do primeiro com o terceiro é: {}".format(b))
c = real**3
print("c) o terceiro elevado ao cubo é: {}".format(c))
