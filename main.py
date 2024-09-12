# Meu nome é Marcelo dos Santos Junior
# Meu nick do discord é mjuniorbral
# Meu e-mail pessoal é mjuniorbral@gmail.com
# Eu trabalho com mentoria de programação na linguagem python e faço consultoria para iniciantes em programação.
# Se estiver interessado em algo mais aprofundado, me contate pelo discord ou pelo meu e-mail. Deixo claro que o serviço é pago.

# Preferência pessoal: Alterei o módulo principal do programa para main.py, pois o nome do programa em si já está no nome da pasta. Além disso, o main.py é apenas o módulo principal que será rodado pelo interpretador.

import random 

jogadores = []
lados_moeda = ["cara","coroa"]
lado_jogador = dict() # Criando um dicionário para armazenar o lado com o jogador relativo após a escolha

# Usar uma lista de jogadores é melhor do que colocar em variáveis 
jogadores.append(input("Digite o nome do jogador 1 "))  # Posição do jogador1 na lista jogadores é 0
jogadores.append(input("Digite o nome do jogador 2 "))  # Posição do jogador2 na lista jogadores é 1

i_primeiro_jogador = random.randint(0,1)  # Sorteio da posição do primeiro jogador
print(f"{jogadores[i_primeiro_jogador]}, você foi sorteado para escolher o lado da moeda.")
# Apenas há uma escolha. O outro pega a opção por exclusão, por isso não precisa fazer a verificação de escolhas dos jogadores,
# mas sim só avisar qual é a opção dada ao segundo jogador

# Usar o while para verificar todas as vezes que a opção escolhida for errada
while True:
    lado_primeiro_jogador = input('Escolha: "cara" ou "coroa"?\n(escreva abaixo sua escolha sem as aspas e apenas com letras minúsculas)\n')
    if not (lado_primeiro_jogador in lados_moeda):  # Tratamento de bugs do jogo (verificação do que foi digitado)
        print("A opção digitada não está entre as válidas. Cuide para digitar a opção corretamente.")
        continue
    break
# Guardando a escolha do primeiro_jogador em uma dicionário
lado_jogador[jogadores[i_primeiro_jogador]] = lado_primeiro_jogador
# Como a lista só tem dois elementos (lista binária), subtraindo o index da escolha, eu retorno a outra escolha
# (ex: se index==1, -> 1-1==0; se index==0, -> 0-1=-1, último elemento de uma lista de dois, equivalente ao index 1)
lado_segundo_jogador = lados_moeda[ lados_moeda.index( lado_primeiro_jogador ) - 1 ]
# Registrando o lado do segundo jogador que não precisa escolher por si só.
# Usando a mesma lógica de index-1 para pegar o outro jogador na lista de jogadores
i_segundo_jogador = i_primeiro_jogador - 1
escolhas[jogadores[i_segundo_jogador]] = lado_segundo_jogador

# Sorteando o cara e coroa
# A função choice te ajuda a evitar ter que sortear um valor de index depois pegar a string correspondente
lado_sorteado = random.choice(["cara","coroa"]) # mudei o nome da variável para ser mais significativo

# Com um dicionário, eu posso evitar o exceção de estruturas de condições para relacionar a escolha de um jogador com o próprio jogador
jogador_vencedor = lado_jogador[lado_sorteado]
print(f"{jogador_vencedor}, você ganhou o cara e coroa. Parabéns!")

# Comentários sobre seu código:
# - Quando você ver no seu código muitos ifs, estranhe. Não significa que esteja errado, ou que você precisa mudar algo. Mas geralmente existe um jeito mais limpo e fácil de resolver o que você deseja.
# - Estudo sobre listas e dicionários, pq as vezes armazenar as informações de forma imutáveis em várias variáveis pode complicar a sua vida em funções dinâmicas como um jogo.
# - Você fez a verificação da escolha sobreposta dos jogadores, mas só fez uma vez. Faça um teste: rode o programa e quando for escolher o lado da moeda, escreve coroa em todos os inputs que o programa te pedir:
#        o programa vai rodar com os dois jogadores com a mesma opção. Nesse caso você pode usar o while loop como usei na minha versão do programa.
