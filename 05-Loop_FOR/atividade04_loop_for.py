# Autor: Samuel Barbosa
# Projeto: loop for - variáveis de início e fim

numero = int(input('Digite um número para a tabuada: '))
numero_inicio = int(input('Digite o inicio da tabuada: '))
numero_fim = int(input('Digite o fim da tabuada: '))

# loop FOR
for i in range (numero_inicio, numero_fim + 1):
    print(f'{numero} x {i} = {i * numero}')