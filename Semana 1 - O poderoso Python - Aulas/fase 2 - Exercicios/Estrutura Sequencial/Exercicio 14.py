""" 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
seu trabalho.Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de 
pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
 """
peso = float(input("forneça o valor em kilos da pesca: "))
multa = 4.00
peso_maximo = 50

if peso > peso_maximo:
    execsso_kg = peso - peso_maximo
    multa_a_pagar = multa * execsso_kg
    print("A quantidade de quilos obtidos por João é de {}kg que utrapassar o limite em {}kg. Devera paga multa de {}R$ pelo excesso".format(peso, execsso_kg, multa_a_pagar ))
else:
    print("A quantidade de quilos obtidos por João é de {}kg e não é necessario pagar multa.".format(peso))
