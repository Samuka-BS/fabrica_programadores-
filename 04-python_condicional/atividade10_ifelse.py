nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc =  peso / (altura * altura)

# exibir o resultado com variável
print('O resultado é: ',imc)
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
   