numero = int(input("Digite um número inteiro positivo: "))

if numero > 0:
    if numero % 2 == 0:
        resultado = numero ** 2
        print(f"O número é par. Seu quadrado é: {resultado}")
    else:
        resultado = numero ** 3
        print(f"O número é ímpar. Seu cubo é: {resultado}")
else:
    print("Por favor, digite um número inteiro positivo.")