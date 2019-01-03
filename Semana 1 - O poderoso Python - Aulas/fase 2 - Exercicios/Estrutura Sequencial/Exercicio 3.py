# 3 - Faça um Programa que peça dois números e imprima a soma.

a, b = map(int, input("Forneça dois números, com espaço entre eles, para saber a soma deles: ").split())
soma = a + b
print("A soma dos números fornecidos é: {}".format(soma))