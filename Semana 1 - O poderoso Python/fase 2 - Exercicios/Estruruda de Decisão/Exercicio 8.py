""" Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. """
a, b, c = map(float, input("Digite três valores de tres produtos e direi qual deve comprar: ").split())
if a < b and a < c:
    print("O produto que voçê deve compra e o de valor {}".format(a))
elif b < a and b < c : 
    print("O produto que voçê deve compra e o de valor {}".format(b))
elif c < a and c < b :
    print("O produto que voçê deve compra e o de valor {}".format(c))
