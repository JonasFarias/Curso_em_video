'''Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os
valores pares e os valores
ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista = []

while True:
    numero = int(input('Digite um numero: '))
    resposta = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resposta in 'N':
        break