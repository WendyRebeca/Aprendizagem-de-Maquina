import csv

dadosIniciais = [
    ["Nome", "Idade"],
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduardo", 35]
]

with open("dadosIniciais.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(dadosIniciais)


dadosLista = []
with open("dadosIniciais.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  
    for linha in reader:
        nome, idade = linha[0], int(linha[1])
        dadosLista.append((nome, idade))


idadeMax = max(dadosLista, key=lambda x: x[1])[1]


nomeProcurar = input("Digite um nome para procurar: ")

encontrado = False
for nome, idade in dadosLista:
    if nomeProcurar.strip().lower() == nome.lower():
        encontrado = True
        if idade == idadeMax:
            print(f"{nome} tem {idade} anos, é a pessoa mais velha da lista.")
        else:
            print(f"{nome} tem {idade} anos e não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print(f"O nome '{nomeProcurar}' não foi encontrado.")
