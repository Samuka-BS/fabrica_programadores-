# Autor: Samuel Barbosa

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

def calcular (peso, altura):
    imc = peso/(altura*altura)


    print(f'O resultado do seu imc é: {imc:.2f}') 

calcular(peso, altura)