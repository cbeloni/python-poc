from dataclasses import dataclass

@dataclass(repr=True, init=True)
class DataClassCard:
    '''
    criado init e repr automaticamente
    '''
    rank: str
    suit: str    

@dataclass(frozen=True,repr=True, init=True)
class Immutable:
    '''
    Classe imutável
    '''
    nome: str
    sobrenome: str
        
if __name__ == '__main__':
    card:DataClassCard = DataClassCard(rank = "100", suit = "suit")
    print(card.rank)
    print(card)
    
    immutable:Immutable= Immutable(nome = "caue", sobrenome="beloni")
    print(immutable.nome)
    
        