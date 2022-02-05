class Pessoa(object):
    def __init__(self: object, nome: str) -> None:
        '''
        in: nome: nome da pessoa
        '''
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome   

    @nome.setter
    def nome(self, value):
         # este código é executado sempre que alguém fizer 
         # self.nome = value
         self.__nome = value

if __name__ == '__main__':
    print ('Inicio:')
    caue : Pessoa = Pessoa("Caue")    
    raquel = Pessoa = Pessoa(nome="Raquel")
    
    print (caue.nome)    
    print (raquel.nome)

    print (id(caue))
    print (id(raquel))