'''Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista.
No final, mostre qual foi o
maior e o menor valor digitado e as
suas respectivas posições na lista.'''

valores = []
for contador in range(0, 5):
    valor = int(input('Digite um valor: '))
    valores.append(valor)
print(f'O maior valor digitado foi {max(valores)}, na posição ')
print(f'O menor valor digitadoo foi {min(valores)}, na posição ')

print('ACABOU!')
print(valores)