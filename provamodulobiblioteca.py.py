def AdicionarAluno():
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    alunos[matricula] = nome

    print("Aluno adicionado com sucesso!")

    return alunos

def RemoverAluno():
    matricula = int(input("Digite a matrícula do aluno: "))
    del alunos[matricula]
    print("Aluno removido com sucesso!")
    return alunos

def AtualizarAluno():
    matricula = int(input("Digite a matrícula do aluno: "))
    nome = input("Digite o nome do aluno: ")
    alunos[matricula] = nome
    print("Aluno atualizado com sucesso!")
    return alunos

def VerAlunos():
    for matricula, nome in alunos.items():
        print(matricula, nome)
    return alunos

alunos = {}

while True:
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        alunos = AdicionarAluno()
    elif opcao == 2:
        alunos = RemoverAluno()
    elif opcao == 3:
        alunos = AtualizarAluno()
    elif opcao == 4:
        alunos = VerAlunos()
    elif opcao == 5:
        break
    else:
        print("Opção inválida!")
        continue

    print()
    print("Deseja continuar? [1] Sim [2] Não")
    continuar = int(input())
    if continuar == 2:
        break