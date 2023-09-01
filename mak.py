pacientes = dict()

id = 1

while True:
    escolha = int(input("""
Escolha uma das opções:
1 - Cadastrar novo paciente;
2 - Ver todos pacientes;
3 - Excluir paciente;
0 - Encerar o sistema.
"""))
    
    match escolha:
        case 1:
            nome = input("Digite o nome do paciente: ")
            idade = int(input("Digite a idade do paciente: "))
            peso = float(input("Digite a peso do paciente: "))
            altura = float(input("Digite a altura do paciente: "))

            pacientes[id] = [nome, idade, peso, altura]

            id += 1

            input("Paciente cadastado com sucesso, precione enter para continuar:")
            print("\n" * 50)

        case 2:
            for i in pacientes:
                print(f"O paciente com id: {i}, tem as seguintes informações:\n"+
                      f"nome: {pacientes[i][0]}\n" +
                      f"idade: {pacientes[i][1]}\n" +
                      f"peso: {pacientes[i][2]}\n" + 
                      f"altura: {pacientes[i][3]}")
                print("________________________________________________________________")

            input("Precione enter para continuar")
            print("\n" * 50)
                  
        case 3:
            for i in pacientes:
                print(f"id: {i} - nome: {pacientes[i][0]}")

            deletar = input("Qual o id do paciente para ser deletado: ")

            confirmacao = True

            for i in deletar:
                if i not in "1234567890":
                    confirmacao = False
                    break

            if confirmacao == True:
                if deletar in pacientes.keys():
                    del(pacientes[deletar])
                    print("Paciente deletado com sucesso")
                else:
                    print("Paciente inexistente")

                input("Precione enter para continuar")
                print("\n" * 50)
            else:
                print("Digitado uma letra, tente novamente")

