from random import randint
from random import choice

def jogar():
    portas = [1,2,3]
    portas_monstro = [1,2,3]
    porta_premio = randint(1, 3)
    portas_monstro.remove(porta_premio)
    porta_escolhida = choice(portas)

    if porta_escolhida == porta_premio:
        return True;
    return False;

def jogar_mudando_porta():
    portas = [1,2,3]
    portas_monstro = [1,2,3]
    porta_premio = randint(1, 3)
    portas_monstro.remove(porta_premio)
    porta_escolhida = choice(portas)

    porta_abrir = [1,2,3]
    porta_abrir.remove(porta_escolhida)
    if porta_escolhida != porta_premio:
        porta_abrir.remove(porta_premio)
    if len(porta_abrir) > 1: 
        porta_abrir.remove(porta_abrir[0])

    porta_aberta = porta_abrir[0]

    porta_nova_escolha = [1,2,3]
    porta_nova_escolha.remove(porta_aberta)
    porta_nova_escolha.remove(porta_escolhida)
    porta_nova_escolha = porta_nova_escolha[0]

    if porta_nova_escolha == porta_premio:
        return True;
    return False;

vitorias = 0;
for i in range(100000):
    ganhou = jogar_mudando_porta();
    if ganhou: 
        vitorias += 1
print("quantidade de vitórias mudando de porta")
print(str((vitorias*100)/100000)+"%")

vitorias = 0;
for i in range(100000):
    ganhou = jogar();
    if ganhou: 
        vitorias += 1
print("quantidade de vitórias sem mudar a porta")
print(str((vitorias*100)/100000)+"%")


