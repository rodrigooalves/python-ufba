while True:
    idade = int(input("Informe a idade do aluno (ou uma idade negativa para encerrar): "))
    
    if idade < 0:
        print("Leitura encerrada.")
        break
    else:
        print(f"Idade registrada: {idade}")