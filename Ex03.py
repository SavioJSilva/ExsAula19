from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 caso não houver): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('-' * 60)
for k, v in dados.items():
    print(f' - {k}: {v}')


