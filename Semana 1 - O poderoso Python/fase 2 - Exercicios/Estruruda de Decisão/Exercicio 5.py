"""  5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez. """

nota1, nota2 = map(int, input("Foneça as duas notas do aluno(separada por espaço): ").split())
media = (nota1 + nota2)/2
if media >= 7:
    print("Voçê foi Aprovado com média de {}".format(media))
elif media < 7:
    print("Voçê foi Reprovado com média de {}".format(media))
elif media == 10:
    print("Voçê foi Aprovado com Distinção com média de {}".format(media)) 