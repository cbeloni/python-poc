from abc import ABCMeta, abstractclassmethod

class Ordem(metaclass=ABCMeta):
    
    @abstractclassmethod
    def executar(self):
        pass

class OrdemCompra(Ordem):
    
    def __init__(self) -> None:
        self._acao = Acao()
    
    def executar(self):
        self._acao.comprar()

class OrdemVenda(Ordem):

    def __init__(self) -> None:
        self._acao = Acao()
    
    def executar(self):
        self._acao.vender()

class Acao:
    
    def comprar(self):
        print("comprando")
        
    def vender(self):
        print("vendndo")
        
class Agente:
    
    def __init__(self) -> None:
        self._ordens = []
    
    def adicionar_ordem(self, ordem):
        self._ordens.append(ordem)
    
    def executar_ordens(self):
        for ordem in self._ordens:
            ordem.executar()            
    
if __name__ == '__main__':
    agente = Agente()
    agente.adicionar_ordem(OrdemCompra())
    agente.adicionar_ordem(OrdemVenda())
    
    agente.executar_ordens()