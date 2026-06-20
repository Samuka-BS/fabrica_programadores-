# Autor: Samuel Barbosa
# Projeto: desvio condicional

# Criação das variáveis
nome = input('Digite seu nome: ')
nota = float(input('Digite a nota final: '))

def status(nota):
    if nota>=6:
         print('Aluno aprovado')
    else:
         print('Aluno reprovado')

status(nota)