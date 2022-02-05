
class Rede:
    
    def pagar(self: object, valor: int = 0):
        print("estou pagando pela rede %s" % valor)


class Cielo:

    def pagar(self: object, valor: int = 0):
        print("estou pagando pela Cielo %s" % valor)
        

class PagamentoFactory:
    
    def __init__(self: object, adquirente: str = "Cielo") -> None:
        self._adquirente = adquirente
    
    def criarFormaPagamento(self: object) -> object:
        return eval(self._adquirente)()
    

if __name__ == '__main__':
    adquirente = PagamentoFactory("REDE".title()).criarFormaPagamento()
    adquirente.pagar(10)
    