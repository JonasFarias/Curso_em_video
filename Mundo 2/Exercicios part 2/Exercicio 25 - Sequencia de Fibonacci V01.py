'''Escreva um programa que leia um número N
inteiro qualquer e mostre na tela os N
primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

print('#' * 30)
print('SEQUENCIA DE FIBONACCI V01')
print('#' * 30)
sequencia = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

print('~'*30)
print('{} - {}'.format(t1, t2), end='')
contador = 3
while contador <= sequencia:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' - FIM ')