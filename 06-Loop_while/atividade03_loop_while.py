# Autor: Samuel Barbosa
# Projeto: Loop While

numero = int(input('Digite um número para a tabuada: '))
inicio = int(input('Digite o primeiro valor da tabuada: '))
fim = int(input('Digite o ultimo valor da tabuada: '))
while inicio <=fim:
    print(f'{numero} x {inicio} = {numero * inicio}')
    inicio = inicio + 1