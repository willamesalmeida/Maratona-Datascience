# 1 - Faça um Programa que peça dois números e imprima o maior deles.

a, b = map(float, input("Forneça dois valores e direi qual o maior deles: ").split())
if a > b:
    print("O maior número fornecido é: {} ".format(a))
else:
    print("O maior número fornecido é: {} ".format(b))