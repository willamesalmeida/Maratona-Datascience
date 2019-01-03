# 9 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).
f = float(input("Forneça um valor de temperatura em Farenheit pra converter em celsius: "))
c = (5 * (f - 32) / 9)
print ("O valor em Farenheit fornecida de: {} tem sua equivalencia em celsius de: {}".format(f, c))
c2 = (f - 32) / 1.8
print (' valor em celsius {}'.format(c2))