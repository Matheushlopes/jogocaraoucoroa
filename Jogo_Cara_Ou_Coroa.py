import random 

jogador1 = input("Digite o nome do jogador 1 ")
jogador2 = input("Digite o nome do jogador 2 ")

jogador_aleatorio = random.randrange(0,2)
cara_ou_coroa = random.randrange(0,2)


if cara_ou_coroa == 0:
    cara_ou_coroa = 'Cara'
else:
    cara_ou_coroa = 'Coroa'


if jogador_aleatorio == 0:
    jogador1_result = input(f'{jogador1}, Escolha Cara ou Coroa')
    jogador2_result = input(f'{jogador2}, Escolha Cara ou Coroa')
    if jogador2_result == jogador1_result:
        print(f'O {jogador1}, Já Selecionou essa opção, escolha outro')
        jogador2_result = input(f'{jogador2}, Escolha Cara ou Coroa')
    



elif jogador_aleatorio == 1:
    jogador2_result = input(f'{jogador2}, Escolha Cara ou Coroa')
    jogador1_result = input(f'{jogador1}, Escolha Cara ou Coroa')
    if jogador1_result == jogador2_result:
        print(f'O {jogador2}, Já Selecionou essa opção, escolha outro')
        jogador1_result = input(f'{jogador1}, Escolha Cara ou Coroa')
   
if jogador1_result == cara_ou_coroa:
    print(f'{jogador1}, Ganhou!! ')
else:
    print(f'{jogador2}, Ganhou !!!')






      
        


#
#cara_ou_coroa = random.randrange(0,2)