class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #E uma Fabrica de objeto. nao tem acesso a instancia, mas tem acesso direto a propria classe sem precisar instanciar.
    @classmethod
    def criar_pessoa_com_25_anos(cls, nome):
        return cls(nome, 25)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("Anônimo", idade)
    

pessoa1 =  Pessoa.criar_pessoa_com_25_anos("Ermeson")
print("Nome:", pessoa1.nome, "\nIdade:" ,pessoa1.idade)

#isso aqui e a mesma coisa do que o objeto Pessoa3 na linha 29 e 30 só que declarado em uma função dentro da classe (Uma fabrica).
pessoa2 = Pessoa.criar_sem_nome(20)
print("Nome:", pessoa2.nome, "\nIdade: ",pessoa2.idade)


pessoa3 = Pessoa("Pedro", 28)
print("Nome:", pessoa3.nome, "\nIdade: ",pessoa3.idade)