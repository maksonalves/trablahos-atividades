from functools import reduce

'''numeros = [8, 6, 10, 1.5, 4]

quadrados = list(map(lambda x: x ** 2,numeros))

print(quadrados)'''



'''def quadrados(x):
    return x ** 2

numeros = [8, 6, 10, 1.5, 4]

numeros_quadrados = list(map(quadrados, numeros))

print(numeros_quadrados)'''



'''numero = [7, 3, 5, 12, 9]

impar = list(filter(lambda x: x % 2 != 0, numero))

print(impar)'''



numero = [7, 3, 5, 12, 9]

soma = reduce(lambda x, y: x + y, numero)

print(soma)