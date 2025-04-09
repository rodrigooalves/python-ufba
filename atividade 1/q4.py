# 4. Você possui algumas variáveis em Python que descrevem alguns dos seus
# atributos:
# nome = {coloque seu nome}
# idade = {coloque sua idade}
# cidade = {coloque sua cidade}
# Com base nessas variáveis, gere uma apresentação curta de si mesmo.

nome = str(input("Digite seu nome: \n"))
age = int(input("Digite sua idade: \n"))
city = str(input("Digite sua cidade: \n"))

print(f"Olá {nome}, seja bem vindo(a)! Você tem {age} ano e mora em {city}.")