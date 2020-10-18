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
    if mao_mesa < 5:
        print('Mesa recebe mais uma carta')
        carta_3 = random.randint(0,9)
        mesa.append(carta_3)
        mao_mesa = sum(mesa)
        print(mesa)
        print(mao_mesa)
    if mao_mesa > 10 :
        print('Soma da mao da mesa:')
        mao_mesa = mao_mesa - 10
        print(mao_mesa)
    
    #JOGADOR
    if mao_jogador < 5:
        print('Jogador recebe mais uma carta')
        carta_4 = random.randint(0,9)
        jogador.append(carta_4)
        mao_jogador = sum(jogador)
        print(jogador) 
        print('Soma da mão do jogador:')
        print(mao_jogador)
    if mao_jogador > 10 :
       mao_jogador = mao_jogador - 10
       print('Soma da mao da jogador:')
       print(mao_jogador)    
    
    #METODO
    if metodo == 'mesa':
        if mao_jogador < mao_mesa:
            fichas = fichas + aposta*(95/100)
            print('Você ganhou!')
        if mao_mesa == 8:
            fichas = fichas + aposta*(95/100)
            print('Você ganhou!')
        if mao_mesa == 9:
            fichas = fichas + aposta
            print('Você ganhou!')
        else:
            fichas = fichas - aposta
            print('Você perdeu!')
    if metodo == 'jogador':
        if mao_mesa < mao_jogador:
            fichas = fichas + aposta
            print('Você ganhou!')
        if mao_jogador == 8:
            fichas = fichas + aposta
            print('Você ganhou!')
        if mao_jogador == 9:
            fichas = fichas + aposta
            print('Você ganhou!')
        else:
            fichas = fichas - aposta
            print('Você perdeu!')    
    if metodo == 'empate':
        if mao_jogador == mao_mesa:
            fichas = fichas + aposta*8
            print('Você ganhou!')
        else:
            fichas = fichas - aposta
            print('Você perdeu!')
