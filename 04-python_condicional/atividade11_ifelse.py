nome = input('Digite seu nome: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float (input('Digite a terceira nota: '))
nota_final = (nota1 + nota2 + nota3) / 3
if nota_final >=7:
    print('Parabéns ' + nome + ' você foi aprovado')
elif nota_final >=4:
    print('Você está de recuperação')
else:
    print('Desculpe ' + nome + ' você foi reprovado')