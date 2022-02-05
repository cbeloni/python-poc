class Atributos(object):

    def __init__(self, *args):
        super(Atributos, self).__init__(*args)
        self.__nome = "Meu Nome"


if __name__ == '__main__':
    a : Atributos = Atributos()
    print (a.__dict__)
            
        