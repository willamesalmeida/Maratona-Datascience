""" Faça um Programa que leia três números e mostre o maior e o menor deles. """
a, b, c = map(float, input("Digite três valores e direi qual é o maior: ").split())
if a < b and a < c:
    print("O menor valor é {}".format(a))
elif b < a and b < c : 
    print("O menor valor é {}".format(b))
elif c < a and c < b :
    print("O menor valor é {}".format(c))
