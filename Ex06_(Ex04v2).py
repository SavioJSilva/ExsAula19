jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c+1} ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SsNn':
            break
        print('Por favor, Responda apenas S ou N.')
    if r == 'N':
        break
print('-' * 60)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)
while True:
    dados = int(input('Mostar dados de qual jogador? (999 interrompe) '))
    if dados == 999:
        break
    if dados >= len(time):
        print(f'Não existe jogador com o código {dados}!')
    else:
        print(f' -- DADOS DO JOGADOR {time[dados]["Nome"]}:')
        for i, g in enumerate(time[dados]['gols']):0
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 60)
print(f'                Volte sempre! ')