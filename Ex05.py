galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Por favor, digite apenas M para Masculino e F para Feminino.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Quer continuar? [Sim ou Nao] ')).upper()[0]
        if r in 'SN':
            break
        print('Por favor, responda apenas sim ou não.')
    if r == 'N':
        break
print('-' * 60)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print(' ' * 10, 'FIM')