# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("Digite um o valor do raio e receba o valor da area do circulo: "))
pi =  3.141592
area = pi * (raio**2)
print(" O valor da area do circulo é de A= {:.0f} x {:.2f} =  {}".format(raio, pi, area))