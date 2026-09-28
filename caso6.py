# 6. Senha fraca e tentativa de acesso

SENHA_CORRETA = "12345"
MAX_TENTATIVAS = 3
tentativas = 0

while tentativas < MAX_TENTATIVAS:
    senha = input("Digite a sua senha: ")
    tentativas += 1
    
    if senha == SENHA_CORRETA:
        print("Acesso concedido!")
        break
    else:
        tentativas_restantes = MAX_TENTATIVAS - tentativas
        if tentativas_restantes > 0:
            print(f"Senha incorreta! Tentativas restantes: {tentativas_restantes}")
        else:
            print("Número máximo de tentativas atingido. Acesso bloqueado!")
