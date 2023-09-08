'''#1. A partir de uma lista de strings, utilize map() e uma função lambda para
#converter todas as letras em maiúscula

lista = ["amanda", "brenda", "carla", "danielle"]

maiusculas = list(map(lambda x:x.upper(), lista))

print(maiusculas)
'''

'''#2. A partir de uma lista de palavras, utilize filter() e uma função lambda para
#filtrar apenas as palavras que possuem mais de 5 letras.

lista = ["amanda", "brenda", "carla", "danielle"]

nomes = list(filter(lambda x: x))
'''

'''#2. Implemente uma função lambda que receba duas strings e retorne a concatenação
#das duas, apenas se ambas as strings tiverem mais de 5 caracteres. Caso contrário,
#a função deve retornar uma mensagem de erro.

contatenar = lambda x, y: (x + y 
                           if len(x) >= 5 and len(y) >= 5 else 
                           "Palavras com menos de 5 caracteres")

print(contatenar("baião","almoço"))'''