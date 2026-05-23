nome = input('Digite seu nome: ')
telefone = input('Digite seu telefone: ')
cidade = input('Digite sua cidade: ')
salario = float(input('Digite seu salário: '))

if salario >=1000:
    print('Você possui um bom saláiro')
elif salario >700:
    print('Você possui um salário razoável')
elif salario >500:
    print('Você possui um salário baixo')
else:
    print('Você possui um salário muito baixo')