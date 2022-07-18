'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoa = list()

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'S':
        pessoa.append([nome, peso])
    elif continuar in 'N':
        pessoa.append([nome, peso])
        break


print(pessoa)