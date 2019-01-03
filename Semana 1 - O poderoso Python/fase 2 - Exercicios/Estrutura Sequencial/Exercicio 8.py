# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor = float(input("Diga quanto ganha por hora e a quantidade de horas que trabalha e seu salario sera calculado. Forneca o valor por horas: "))
horas = float(input("Forneca a quantidade de horas trabalhadas no mês: "))
salario = horas * valor
print("O valor ganho por horas é de: {} e as horas trabalhada é de: {}, seu salario é: {}".format(valor, horas, salario))