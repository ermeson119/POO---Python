class Pessoa: 
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_name(self, user):
        self.user = user
    
    def set_password(self, password):
        self.password = password


    @classmethod
    def creat_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    

cliente = Pessoa.creat_with_auth("Ermeson", "121656")
print(cliente.user, cliente.password)