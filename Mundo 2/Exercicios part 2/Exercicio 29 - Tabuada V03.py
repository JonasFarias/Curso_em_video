'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''


tabuada2 = 0
numero = 0

tabuada = int(input('Qual Tabuada você quer saber: '))
while True:
    while numero <= 9:
        numero += 1
        resultado = tabuada * numero
        print(f'{tabuada} X {numero} = {resultado}')
    tabuada = int(input('Teste: '))

print('OBRIGADO!')