jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida {c+1} ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' * 60)
print(jogador) #resolução simples
print('-' * 60)
for k, v in jogador.items(): #resolução um pouco melhor
    print(f'{k}: {v}')
print('-' * 60)
print(f' o Jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.') #tambem poderia ter utilizador {tot} para quantidade de jogos.
for i, v in enumerate(jogador['gols']):
    print(f'    Na partida {i+1}, fez {v} gols.')
print(f'    Foi um total de {jogador["total"]} gols.')