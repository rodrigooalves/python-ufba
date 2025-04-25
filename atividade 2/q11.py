a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))

if a < b:
    soma = sum(range(a, b + 1))
    print(f"A soma dos números no intervalo [{a}, {b}] é: {soma}")
else:
    print("Erro: O valor de 'a' deve ser menor que o valor de 'b'.")