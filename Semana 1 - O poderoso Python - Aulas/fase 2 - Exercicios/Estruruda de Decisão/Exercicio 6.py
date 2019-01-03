""" Faça um Programa que leia três números e mostre o maior deles. """
a, b, c = map(float, input("Digite três valores e direi qual é o maior: ").split())
if a > b and a > c:
    print("O maior valor é {}".format(a))
elif b > a and b > c : 
    print("O maior valor é {}".format(b))
elif c > a and c > b :
    print("O maior valor é {}".format(c))
