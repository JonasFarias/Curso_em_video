'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.'''

from random import randint

print('=-=' * 10)
print('     PAR ou IMPAR')
print('=-=' * 10)



while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(1, 10)
    total = jogador + computador
    esolha = ' '
    while esolha not in 'PpIi':
        esolha = str(input('Escolha Par ou Impar: ')).strip().upper()[0]
    print(f'Você Jogou {jogador}, e o computador jogou {computador}, o total é de {total}')


