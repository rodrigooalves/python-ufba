E = int(input("Informe o valor do espaço (E): "))
T = int(input("Informe o valor do tempo (T): "))

if 1 <= E <= 500 and 1 <= T <= 100:
    V = E // T
    print(f"A velocidade alcançada é: {V}")
else:
    print("Erro: Os valores de E e T devem estar nos intervalos 1 <= E <= 500 e 1 <= T <= 100.")