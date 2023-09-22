from multiplicador import multiplicador
from divisão import divisão
from soma import soma
from subtração import subtração

while True:
    escolha = int(input('escolha qual operação deseja fazer\n'
                        '1 - soma \n'
                        '2 - subtração \n'
                        '3 - divisão \n'
                        '4 - multiplicação \n'
                        "0 - encerrar" ))

    match escolha:
        case 1:
            soma()
        case 2:
            subtração()
        case 3:
            divisão()
        case 4:
            multiplicador()
        case 0:
            break
