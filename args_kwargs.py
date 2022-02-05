def raiser(ex): raise ex

def parametro_args(*args):
    
    primeiro_valor = args[0] if args else raiser(ValueError("Parâmetro obrigatório"))
    print (f"primeiro valor: {primeiro_valor}")
    
    for arg in args:
        print (arg)
        
def parametros_kwargs(**kwargs):
    for kwarg in kwargs.items():
        print (kwarg)
        
        
if __name__ == '__main__':
    parametro_args("1234", 123)
    
    parametros_kwargs(campo="teste", nome="caue",sobrenome="beloni")
            