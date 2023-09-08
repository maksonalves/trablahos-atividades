'''def info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} : {valor}")

info(nome = "getulio", idade= 22, peso= 65, altura= 1.76)
'''

def info(**kwargs):
    if kwargs.get("nome", False) != False:
        print(f"Bem vindo {kwargs['nome']}")
    else:
        print("Bem vindo")


escolha = input("Você quer se indenficar?(s/n) ")

if escolha == "s":
    nome = input("Digite o seu nome: ")

    info(nome = nome)
else:
    info()
