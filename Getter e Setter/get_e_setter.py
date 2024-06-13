#@property é uma propriedade do objeto, ela é um 
# metodo que se comporta como um atributo.

# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
class Pessoa: 
    def __init__(self, user, passaword):
        self.user_client = user
        self.passw = passaword


##########################################
        #GETTER
##########################################
    @property
    def user(self):
        return self.user_client
    
    @property
    def passaword(self):
        return self.passw
##########################################


cliente = Pessoa("Ermeson", "123456")

print(cliente.user , cliente.passaword )

