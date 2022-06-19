'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''



numero1 = int(input('Valor 1: '))
numero2 = int(input('Valor 2: '))

opcao = 0

while menu != True:
    if opcao == 1:
        print('{} + {} = {}'.format(numero1,numero2, (numero1 + numero2)))
    print('[ 1 ] SOMAR: ')
    print('[ 2 ] MULTIPLICAR: ')
    print('[ 3 ] MAIOR: ')
    print('[ 4 ] NOVOS NUMEROS: ')
    print('[ 5 ] SAIR DO PROGRAMA: ')
opcao = int(input('Qual a sua opção: '))


