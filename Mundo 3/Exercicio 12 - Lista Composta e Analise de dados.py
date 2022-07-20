'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

temporario = []
principal = []
maior = 0
menor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = temporario[1]
        menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resposta in 'N':
        break

print('=' * 30)
print(f'Ao todo foram cadastrado {len(principal)} pessoas.')
print(f'O maior peso cadastrado é {maior}Kg. Peso de ', end='')
for pessoas in principal:
    if pessoas[1] == maior:
        print(f'[{pessoas[0]}] ', end='')
print()
print(f'O menor peso cadastrado é {menor}Kg. Peso de ', end='')
for pessoas in principal:
    if pessoas[1] == menor:
        print(f'[{pessoas[0]}] ', end='')
print()