
print("=== CADASTRO DE PRODUTO ===")

preco = input("Digite o preço do produto: ").strip()

if preco == "":
    print("Erro: o preço não foi informado.")
else:
    try:
        preco = float(preco)
        print("Preço informado: R$", preco)
    except ValueError:
        print("Erro: digite um preço válido.")
