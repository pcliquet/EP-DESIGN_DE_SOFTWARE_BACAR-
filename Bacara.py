# EP - Design de Software
# Equipe: Pedro Cliquet do Amaral
# Data: 18/10/2020

import random


fichas = 100

while fichas > 0 :
    if fichas == 0 :
        break
    carta = random.randint(0,9)
    print('Fichas disponiveis {0} ' .format(fichas))

    aposta = int(input('quanto quer apostar? '))
    if aposta > fichas:
        print('Não possui toda essa quantia')
    if aposta == 0:
        break
    metodo = input('Como quer apostar?(mesa/jogador/empate) ')
    
    #DISTRIBUINDO CARTAS
    carta_1 = random.randint(0,9)
    carta_2 = random.randint(0,9)
    carta_3 = random.randint(0,9)
    carta_4 = random.randint(0,9)
    mesa = [carta_1,carta_2]
    jogador = [carta_3,carta_4]
    print('Mão da mesa:')
    print(mesa)
    mao_mesa = sum(mesa)
    print('Mão do jogador:')
    print(jogador)
    mao_jogador = sum(jogador)   
    
    
    #MESA
    if mao_mesa <= 5:
        print('Mesa recebe mais uma carta')
        carta_3 = random.randint(0,9)
        mesa.append(carta_3)
        mao_mesa = sum(mesa)
        print(mesa)
    if mao_mesa > 10 :
        print('Soma da mão da mesa:')
        mao_mesa = mao_mesa - 10
        print(mao_mesa)
    
    #JOGADOR
    if mao_jogador <= 5:
        print('Jogador recebe mais uma carta')
        carta_4 = random.randint(0,9)
        jogador.append(carta_4)
        mao_jogador = sum(jogador)
        print(jogador) 
        print('Soma da mão do jogador:')
        print(mao_jogador)
    if mao_jogador >= 10 :
       mao_jogador = mao_jogador - 10
       print('Soma da mao da jogador:')
       print(mao_jogador)    
    #Comissão
    taxa_mesa = int(aposta*(1.01/100))
    taxa_jogador = int(aposta*(1.29/100))
    taxa_empate = int(aposta*(15.75/100))


    #METODO
    #apostando na mesa
    if metodo == 'mesa':
        if mao_mesa == mao_jogador:
            fichas = fichas - aposta
            print('Você perdeu!')
        if mao_mesa > mao_jogador:
            fichas = int(fichas + aposta*(95/100)) - taxa_mesa
            print('Você ganhou!')
        elif mao_jogador > mao_mesa:
            fichas = fichas - aposta
            print('Você perdeu!')

    #apostando no jogador
    if metodo == 'jogador':
        if mao_mesa < mao_jogador:
            fichas = fichas + aposta - taxa_jogador
            print('Você ganhou!')
        elif mao_jogador < mao_mesa:
            fichas = fichas - aposta
            print('Você perdeu!')    
        if mao_mesa == mao_jogador:
            fichas = fichas - aposta
            print('Você perdeu!')
    #apostando no empate
    if metodo == 'empate':
        if mao_jogador == mao_mesa:
            fichas = fichas + aposta*8 - taxa_empate
            print('Você ganhou!')
        else:
            fichas = fichas - aposta
            print('Você perdeu!')
