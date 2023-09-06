"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    num = int(input('Digite um número:'))
except:
    print('O usuário não digitou um número inteiro.')
else:
    if num%2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é ímpar')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hr = int(input('Digite a hora: '))
except:
    print('Digite um número inteiro')
else:
    if 0 <= hr <= 11:
        print('Bom dia!')
    elif hr <=17:
        print('Boa tarde!')
    elif hr <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
