

nomes = ["ely", "Jota", "Maria", "ely", "Pedro", "Jota"]

duplicados = []

for nome in nomes:
    if nomes.count(nome) > 1 and nome not in duplicados:
        duplicados.append(nome)

if len(duplicados) > 0:
    print("Nomes repetidos:")
    for nome in duplicados:
        print(nome)
else:
    print("Não existem nomes repetidos.")
