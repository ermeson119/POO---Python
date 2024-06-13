import json
from tesk import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r') as arquivos:
    pessoa = json.load(arquivos)

    p1 = Pessoa(**pessoa[0])
    p2 = Pessoa(**pessoa[1])
    p3 = Pessoa(**pessoa[2])

    print(p1.nome)
    print(p2.nome)
    print(p3.nome)