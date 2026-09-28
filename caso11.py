

n = int(input("Digite o valor de N: "))

contador_pares = 0

# Percorre todos os números de 1 até N (inclusive)
for numero in range(1, n + 1):
    if numero % 2 == 0:
        contador_pares += 1

print(f"Quantidade de números pares entre 1 e {n}: {contador_pares}")
