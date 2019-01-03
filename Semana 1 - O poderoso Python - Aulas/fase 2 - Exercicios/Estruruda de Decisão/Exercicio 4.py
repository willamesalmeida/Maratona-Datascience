# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Forneça uma letra e direi se é consoante ou vogal: ")

if ('AEIOU'.find(letra.upper()) >= 0):
    print("E vogal")
else:
    print("Consoante")