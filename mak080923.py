 #Faça uma função que receba um valor inteiro e positivo e calcula o seu fatorial.

def fatorial(numero):
    acumulador = 1
    expressão = f"{numero} "
    # for i in range(1, numero + 1):
    #     acumulador *= i

    for i in range(numero, 0, -1):
        acumulador *= i

        if i != numero:
            expressão += f"* {i} "

    expressão += f"= {acumulador}"

    return expressão

numero = int(input("Digite um numero inteiro e positivo: "))

print(fatorial(numero))