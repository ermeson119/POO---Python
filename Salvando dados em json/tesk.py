import json
CAMINHO_ARQUIVO = 'salvandoJson.json'

class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Ermeson', 25)
p2 =  Pessoa('Matheus', 21)
p3 =  Pessoa('João Victor', 22)

banco = [vars(p1), vars(p2), vars(p3)]


with open(CAMINHO_ARQUIVO, 'w') as arquivos:
    json.dump(banco, arquivos, ensure_ascii=False, indent=2)