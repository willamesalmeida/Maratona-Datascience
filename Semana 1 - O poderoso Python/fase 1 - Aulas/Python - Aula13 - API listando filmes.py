import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def detalhes_do_filme(filme):
    print('Titulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('Premios:', filme['Awards'])
    print('Poster:', filme['Poster'])

sair = True

while (sair == False):
    opc = input('Escreva o nome de um filme ou SAIR para fechar')

    if opc == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(opc)

        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            detalhes_do_filme(filme)


