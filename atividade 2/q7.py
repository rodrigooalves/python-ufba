num1 = float(input("Digite o primeiro número positivo: "))
num2 = float(input("Digite o segundo número positivo: "))

if num1 > 0 and num2 > 0:
    print("\nEscolha uma opção:")
    print("1. Média ponderada, com pesos 2 e 3, respectivamente")
    print("2. Quadrado da soma dos 2 números")
    print("3. Cubo do menor número")
    
    opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))
    
    if opcao == 1:
        media_ponderada = (num1 * 2 + num2 * 3) / 5
        print(f"A média ponderada é: {media_ponderada}")
    elif opcao == 2:
        quadrado_soma = (num1 + num2) ** 2
        print(f"O quadrado da soma dos números é: {quadrado_soma}")
    elif opcao == 3:
        menor_numero = min(num1, num2)
        cubo_menor = menor_numero ** 3
        print(f"O cubo do menor número ({menor_numero}) é: {cubo_menor}")
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
else:
    print("Por favor, insira apenas números positivos.")