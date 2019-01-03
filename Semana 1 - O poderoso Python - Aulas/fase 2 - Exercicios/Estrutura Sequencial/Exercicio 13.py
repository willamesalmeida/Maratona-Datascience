""" 13 - Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 
 """
altura = float(input("Forneça sua altura para calcular seu peso ideal: "))
print("Com essa altura o peso ideal, para homem é de: {:.2f} , e para mulher é de: {:.2f}".format(((72.7 * altura) - 58), ((62.1 * altura) - 44.7)))