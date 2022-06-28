'''Crie um programa que leia a idade
e o sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''


print('=' * 20)
print('CADASTRE UMA PESSOA!')
print('=' * 20)

total_pessoas_maiores = 0
mulheres_menores = 0
total_homens = 0

while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        total_pessoas_maiores += 1
    sexo = str(input('Sexo [M/F}: ')).strip().upper()[0]
    if sexo == 'M':
        total_homens += 1
    elif sexo == 'F' and idade < 18:
        mulheres_menores += 1
    opção = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'Total de PESSOAS maiores de 18 : {total_pessoas_maiores}')
print(f'Total de MULHERES menores de !8: {mulheres_menores}')
print(f'Total de HOMENS cadastrado é de {total_homens}')

