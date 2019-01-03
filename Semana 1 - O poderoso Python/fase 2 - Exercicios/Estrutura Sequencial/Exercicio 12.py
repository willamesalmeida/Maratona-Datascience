''' 12 - Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58 '''

altura = float(input("Forneca uma altura para calcular o peso ideal: "))
peso_ideal = (72.7*altura) - 58
print("Seu peso ideal a sua altura é de: {}".format(peso_ideal))
