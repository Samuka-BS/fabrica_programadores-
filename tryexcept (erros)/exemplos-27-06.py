numeros = [1,2,0,3,4,5]

for numero in numeros:
    try:
        print(10/numero)
    except:
        print('Ocorreu um erro.')

try:
    print(10/2)
except:
    print('Ocorreu um erro.')