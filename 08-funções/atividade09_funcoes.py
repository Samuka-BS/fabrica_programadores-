# Autor: Samuel Barbosa

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

def calcular (peso, altura):
    imc = peso/(altura*altura)
    print(f'O resultado do seu imc é: {imc:.2f}') 
    if imc <= 18.5:
        print('Magreza')
    elif imc <= 24.9:
        print('Normal')
    elif imc <= 29.9:
        print('Sobrepeso')
    elif imc <= 39.9:
        print('Obesidade')
    else:
        print('Obesidade Grave') 
calcular(peso, altura)

