# Autor: Samuel Barbosa
# Projeto: Tabuada com loop FOR

numero = int(input('Digite um número para a tabuada: '))

# loop FOR
for i in range (0,11):
    print(f'{numero} x {i} = {i * numero}')