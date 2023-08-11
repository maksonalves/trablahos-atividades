'''Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11 produzam resto igual a 2.

for i in range (1000,2001):
    if i % 11 == 2 :
        print (i)'''

'''contador = 1000

while contador <= 2000:
    if contador % 11 == 2:
    print(contador)

    contador += 1

Escreva um aplicativo que recebe inteiro e mostra os números pares e ímpares (separados), de 1 até esse inteiro.'''

'''numero = int(input("digite um numero inteiro e positivo: "))

for i in range (1,numero + 1):
    if i % 2 == 0:
        print(f"o numero {i} é par ")
    
    elif i % 2 != 0:
        print(f"o numero {i} é impar ")'''

'''numero = int(input("digite un numero interiro e positivo: "))

for i in range (1, numero + 1):
    if i % 2 == 0: 
        print(i)
    else:
        print(f"{i}",end=' - ')'''

'''3°: Faça um programa que receba a idade, altura e peso de 25 pessoas, Calcule e mostre:
A quantidade de pessoas com idade superior a 50 anos;
A média das Alturas das pessoas com idade entre 10 e 20 anos;
A porcentagem das pessoas com peso inferior a 40 quilos entre todas as pessoas deixadas.'''

velhos = 0
media = 0 
porcentagem = 0
QP = 0
QPM = 0
for i in range (5):

    idade = int(input("digite a idade: "))
    altura = int(input("digite a altura: "))
    peso = int(input("digite a peso: "))

    if idade >= 50:
        velho += 1

    if idade > 10 , idade < 20:
        media += altura
        QP += 1
        media = media/QP

    if peso

