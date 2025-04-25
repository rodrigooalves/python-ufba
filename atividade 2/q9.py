senha_correta = "123456"

tentativas_restantes = 3

while tentativas_restantes > 0:
    senha = input("Digite a senha para acessar o sistema: ")
    
    if senha == senha_correta:
        print("Olá, . Seja bem-vindo ao nosso banco!")
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"Senha incorreta! Você ainda tem {tentativas_restantes} tentativa(s).")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")