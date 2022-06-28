'''Crie um programa que leia o
nome e o preço de vários produtos.
O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''


print('=' * 25)
print('SUPER LOJA DO JONINHAS')
print('=' * 25)

total_compras = 0
total_produtos_mais_caros = 0
produto_mais_caro = ' '
valor_mais_caro = 0
produto_mais_barato = ' '
valor_mais_barato = 1000

while True:


    produto = str(input('PRODUTO: '))
    preco = float(input('Valor do PRODUTO: '))
    total_compras = preco + total_compras
    if preco >= 1000:
        valor_mais_caro = preco
        total_produtos_mais_caros += 1
    elif preco < valor_mais_barato:
        valor_mais_barato = preco
        produto_mais_barato = produto
    opcao = str(input('Deseja continuar as COMPRAS [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'O TOTAL da compra R$: {total_compras}')
print(f'{total_produtos_mais_caros}, custam mais de 1000 reais')
print(f'O PRODUTO mais barato é : {produto_mais_barato}')





