# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

a, b, c, d = map(float, input('Forneca as 4 notas bimestrais para saber a média (utilize espaço entre as notas): ').split())
media = (a + b + c + d)/4
if media < 7.0:
    print("A sua média é de: {}. Infelizmente você não passou".format(media))
if media >= 7 and media < 8:
    print("A sua média é de: {}. Voçê foi aprovado, mas sua média não foi das melhores, vamos melhorar isso!".format(media))
if media >= 8 and media < 9:
    print('A sua média é de: {}. Parabéns! voçê foi bem, continue estudando para melhorar cada vez mais!'.format(media))
if media >= 9 and media < 10:
    print('A sua média é de: {}. Parabéns! voçê muito bem, continue estudando para chegar a perfeição!'.format(media))
if media == 10 :
    print('A sua média é de: {}. Parabéns! voçê foi perfeito, não pare de estudar, esse é o caminho para o sucesso!'.format(media))
