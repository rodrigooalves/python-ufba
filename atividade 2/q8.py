primeiro_termo = float(input("Digite o primeiro termo da PA: "))
quantidade_termos = int(input("Digite a quantidade de termos da PA: "))
razao = float(input("Digite a razão da PA: "))

print("\nProgressão Aritmética (PA):")
for i in range(quantidade_termos):
    termo = primeiro_termo + i * razao
    print(termo)