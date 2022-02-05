import pytest

from exceptions.custom_exceptions import ValorInvalidoServico

""" GWT: Given When Then """
    
def test_quando_calculo_receber_zero_division_entao_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_quando_value_error_entao_exception():
    with pytest.raises(ValueError):
        myfunc()
    
def test_quando_func_exception_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
        
def test_custom_exception_match():
    with pytest.raises(ValorInvalidoServico, match=r".* chamada do serviço.*"):
        my_custom_exception()
       
def myfunc():
    raise ValueError("Exception 123 raised")

def my_custom_exception():
    raise ValorInvalidoServico("Erro na chamada do serviço")