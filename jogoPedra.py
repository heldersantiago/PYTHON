itens = ('PEDRA', 'PAPEL', 'TESOURA')
from random import randint
from time import sleep
import os 
Computador = randint(0,2)
sair = 'SAIR'
saida = ''

print('JOGO DO HELDER SANTIAGO, PEDRA-PAPEL-TESOURA')

while sair !=saida:

    Nome = input('Digite o seu nome pra iniciar o Jogo... \n>>>>>>>>')

    print('''
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    ''')
    Jogador = int(input('QUAL E A SUA JOGADA? \n>>>>>>>>>'))
    os.system('cls')
    print('PEDRA...')
    sleep(0.5)
    print('PAPEL...')
    sleep(0.5)
    print('TESOURA...')
    sleep(0.5)
    print('*=='*14)
    print('O computador Jogou: {} '.format(itens[Computador]))
    print(Nome,',jogaste: {} '.format(itens[Jogador]))
    print('*='*14, )
    print('          RESULTADO           ')
    if Computador ==  0: #Computador Jogou PEDRA
        
        if Jogador == 0:
            print('EMPATE!')
        elif Jogador == 1:
            print(Nome,',PARABENS, VENCESTE!')
        elif Jogador == 2:
            print(Nome,',Infelizmente PERDESTE!')
        else:
            print('JOGADA INVALIDA!')

    elif Computador == 1: #Computador Jogou PAPEL

        if Jogador == 0:
            print(Nome,',Infelizmente PERDESTE!')
        elif Jogador == 1:
            print('EMPATE!')
        elif Jogador == 2:
            print(Nome,',PARABENS, VENCESTE!')
        else:
            print('JOGADA INVALIDA!')   

    elif Computador == 2: #Computador Jogou TESOURA

        if Jogador == 0:
            print(Nome,',PARABENS, VENCESTE!')
        elif Jogador == 1:
            print(Nome,',Infelizmente PERDESTE!')
        elif Jogador == 2:
            print('EMPATE')
        else:
            print('JOGADA INVALIDA!')
    saida = str(input('SAIR ou CONTINUAR \n>>>>>')).upper()
    os.system('cls')
    