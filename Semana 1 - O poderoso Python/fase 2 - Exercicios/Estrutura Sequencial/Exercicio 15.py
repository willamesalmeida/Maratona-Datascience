'''
15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
valor, horas = map(float, input("Forneça o valor ganho por horas e a quantidade de horas trabalhada no mês: ").split())
salario_bruto = valor * horas

ir = 11 * salario_bruto / 100
inss = 8 * salario_bruto / 100
sind = 5 * salario_bruto / 100
salrio_liquido = salario_bruto - ir - inss - sind
print("+ Salário bruto : {:.2f} R$ \n- IR (11%) : {:.2f} R$ \n- INSS (8%) : {:.2f} R$ \n- Sindicato (5%) : {:.2f} R$ \n= Salário Liquido : {:.2f} R$".format(salario_bruto, ir, inss, sind, salrio_liquido))