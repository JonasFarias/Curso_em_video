#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso
# esteja errado, peça a digitação novamente até ter um valor correto.



sexo = ''

while sexo != 'M' or 'F':
    sexo = str(input('Informe, seu Sexo [M/F]: ')).upper()
    if sexo == 'M':
        print('Sexo informado é Masculino!')
    elif sexo == 'F':
        print('Sexo informado é Feminino!')
    else:
        print('Dado invalido!')


print('Obrigado')