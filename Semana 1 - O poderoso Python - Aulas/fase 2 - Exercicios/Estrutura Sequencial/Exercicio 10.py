# 10 - Faça um Programa que peça a temperatura em graus clesius, transforme e mostre a temperatura em graus farenheit.
# C = (5 * (F-32) / 9).
f = float(input("Forneça um valor de temperatura em clesius pra converter em Farenheit: "))
c = 1.8 * f + 32
print ("O valor em celsius fornecida de: {:.2f} tem sua equivalencia em Farenheit de: {:.2f}".format(f, c))
