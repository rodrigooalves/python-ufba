soma = 0

for i in range(1, 11):
    nota = float(input(f"Digite a nota {i}: "))
    soma += nota

media = soma / 10

print("A média dos alunos é:", media)