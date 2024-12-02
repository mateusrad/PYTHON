def rico_do_mate(N, L, Q, participantes):
    total_cuia_cheia = int(L / Q)            #quantas cuias serão cheias
    ultima_cuia = L - (total_cuia_cheia * Q) #qunatidade na ultima cuia
    if ultima_cuia == 0.0:                   #se o resto da divisão do L por cuias for igual a 0
        ultima_cuia = Q                      #então a ultima cuia terá a qtd da cuia
    total_cuia = total_cuia_cheia + 1        #total de cuias
    vol_da_rodada = N * Q                    # qtd de agua por rodada


    #for Q in L:
        #print(Q)

    cuias_inteira = total_cuia_cheia * Q


    qtd_ultima_cuia = L - (total_cuia_cheia * Q)

    posicao_rico = int(ultima_cuia // Q)

    print(f'{total_cuia_cheia} cuias cheias com {Q}')
    print(f'1 cuia com {ultima_cuia:.1f}')
    print(f'{total_cuia} cuias no total')
    print(f'qtd de agua por rodada {vol_da_rodada}')
    print('posição rico', posicao_rico)
    #print('Cuias inteira', cuias_inteira)



    print('Qtd da ultima cuia', qtd_ultima_cuia)
#    print('{} {:.1f}'.format(participantes[posicao_rico], qtd_ultima_cuia))

#rico_do_mate(3, 3.5, 0.3, ['Maria', 'Renato', 'Juca'])
#rico_do_mate(3, 3.0, 0.3, ['Lara', 'Milena', 'Matheus'])
#rico_do_mate(4, 3.0, 0.3, ['Lara', 'Milena', 'Matheus', 'Thiago'])
#rico_do_mate(4, 4.5, 0.3, ['Lara', 'Milena', 'Matheus', 'Thiago'])
rico_do_mate(4, 4.7, 0.3, ['Lara', 'Milena', 'Matheus', 'Thiago'])

