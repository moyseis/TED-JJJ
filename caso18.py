
def calcular_valor_compra(valor):
    if valor <= 0:
        return "Erro: Valor de compra inválido."
    elif valor <= 100:
        return valor  # Até R$ 100 não há desconto
    else:
        return valor * 0.90  # Acima de R$ 100 há 10% de desconto

# Suíte de testes de caixa-preta
casos_de_teste = [
    50.0,    # Caso normal (sem desconto)
    150.0,   # Caso normal (com desconto)
    100.0,   # Valor de fronteira (limite de 0% de desconto)
    100.01,  # Valor de fronteira (início dos 10% de desconto)
    0.0,     # Valor inesperado/inválido
    -20.0    # Valor inesperado/inválido (negativo)
]

print("--- Execução dos Testes de Caixa-Preta ---")
for valor_compra in casos_de_teste:
    resultado = calcular_valor_compra(valor_compra)
    if isinstance(resultado, float):
        print(f"Compra: R$ {valor_compra:.2f} | Valor Final: R$ {resultado:.2f}")
    else:
        print(f"Compra: R$ {valor_compra} | Mensagem: {resultado}")
