'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.'''



valor = 0
validacao = 'Ss'
soma = 0
contador = 0

while validacao not in 'Nn':
    valor = int(input('Digite um numero: '))
    validacao = str(input('Quer continuar Sim ou Não: ')).strip().upper()[0]
    contador += 1
    soma = soma + valor

media = soma / contador
print('Você Digitou {} e a media foi de {}'.format(contador, media))
print('FIM')
