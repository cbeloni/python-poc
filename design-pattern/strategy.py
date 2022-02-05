import logging

class Rede:

    def pagar(self: object, valor: int = 0):
        print("estou pagando pela rede %s" % valor)


class Cielo:

    def pagar(self: object, valor: int = 0):
        print("estou pagando pela Cielo %s" % valor)

if __name__ == '__main__':
    print("inicio")

    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    print("Strategy lista")
    gateways: list = []
    gateways.append(Rede())
    gateways.append(Cielo())

    gatewayFiltrado = [i for i in gateways if type(i).__name__ == 'Cielo'][0]

    gatewayFiltrado.pagar(1)
    

    print("Strategy dict")
    gatewaysDict: dict  = {}
    gatewaysDict['Cielo'] = Cielo()
    gatewaysDict['Rede'] = Rede()

    logging.info("inicio logging")
    try:
        gatewayGenerico = gatewaysDict['Cielo']
    except:
        logging.exception("Erro para obter gateway")

    gatewayGenerico.pagar()

    chave = 'Cielo'
    gatewayGenericoTernary = gatewaysDict[chave] if chave in gatewaysDict.keys() else Rede()
       
    nome_classe = type(Cielo()).__name__
    
    print("nome classe: " + nome_classe)
   
    
    print("Gateway genérico ternary if: ")
    gatewayGenericoTernary.pagar()



    print ("fim")