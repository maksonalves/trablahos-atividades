'''def media(*args):
    soma = 0
    contagem = 0

    for i in args:
        soma += i
        contagem += 1

    media = soma / contagem

    print(media)

media1 = media(1, 2, 3, 4)
media1 = media(2, 3, 4)    
media1 = media(3, 4)    
'''
def media(*args):
    soma = 0
    contador = 0

    for i in args:
        soma += i
        contador += 1

    media = soma / contador

    print(f"as notas: {args} deram a media de {media}")

escolha = int(input("Escolha uma das opções: \n" +
                    "1 - 2 notas \n" +
                    "2 - 4 notas \n" +
                    "3 - 6 notas \n"))

match escolha:
    case 1: 
        n1 = float(input("digite a primeira nota: "))
        n2 = float(input("digite a segunda nota: "))

        media(n1, n2)
    case 2:
        n1 = float(input("digite a primeira nota: "))
        n2 = float(input("digite a segunda nota: "))
        n3 = float(input("digite a terceira nota: "))
        n4 = float(input("digite a quarta nota: "))

        media(n1,n2,n3,n4)
    case 3:
        n1 = float(input("digite a primeira nota: "))
        n2 = float(input("digite a segunda nota: "))
        n3 = float(input("digite a terceira nota: "))
        n4 = float(input("digite a quarta nota: "))
        n5 = float(input("digite a quinta nota: "))
        n6 = float(input("digite a sexta nota: "))

        media(n1,n2,n3,n4,n5,n6)
        