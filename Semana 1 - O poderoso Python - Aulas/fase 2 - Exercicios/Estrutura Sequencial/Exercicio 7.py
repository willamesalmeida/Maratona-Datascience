# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Forneça um valor para calcular a area do quadrado: "))
area = lado ** 2
print("A area do quadrado é de: {:.0f} e o seu dobro é de: {:.0f}".format(area, area*2))