#1#Escreva um programa que peça ao usuário para adivinhar um 
#número que você deverá escolher com antecedência até que ele acerte.
#Para ajudar o usuário, o programa deve informar se o número é maior ou
#menor que o número a ser adivinhado. Ao final, imprima o número
#adivinhado e a quantidade de tentativas.

numero_sorte = 70
tentativas = 0
while True:

    numero = int(input("digite o numero da sorte"))

    if numero > numero_sorte:
        print("numero maior que numero da sorte: ")
        tentativas +=1
    if numero < numero_sorte:
        print("numero menor que numero da sorte: ")
        tentativas +=1
    if numero == numero_sorte:
        break
print(f'parabens, {numero_sorte} premiado, e voce teve {tentativas}tentativas')
