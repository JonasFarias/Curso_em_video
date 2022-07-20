'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

temporario = []
principal = []

while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resposta in 'N':
        break