

entrada = input("Digite o preço do produto: ")

texto_limpo = entrada.strip().replace(" ", "").replace(",", ".")

if not texto_limpo:
    print("Erro: A entrada não pode estar vazia.")
else:
    try:
        preco = float(texto_limpo)
        if preco < 0:
            print("Erro: O preço não pode ser um valor negativo.")
        else:
            print(f"Preço válido registado: R$ {preco:.2f}")
    except ValueError:
        print("Erro: A entrada contém letras ou símbolos inválidos.")
