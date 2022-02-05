import logging
import time
from functools import wraps

def contador(func):
    """decorator que calcula o tempo de uma função"""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Inicio")
        inicio = time.time()
        result = func(*args, **kwargs)
        fim = time.time()
        print("Resultado final da função %s: " % func.__name__, fim-inicio)
        logging.info("fim")
        return result
    
    return wrapper

@contador
def contar(n):
    while n > 0:
        n -= 1    
    return "finalizado"
            
def main():
    contar(100000)
    contador(contar(10000))
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    main()
    