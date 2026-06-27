numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')

try:
    numero1 = int(numero1)
    numero2 = int(numero2)
    print(numero1 + numero2)
except:
    print('Somente permitido números.')
    