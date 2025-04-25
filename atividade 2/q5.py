numero = int(input("Digite um número de 1 a 10: "))

if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Por favor, digite um número entre 1 e 10.")