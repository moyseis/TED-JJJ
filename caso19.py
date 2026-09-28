

def verificar_usuario(idade, renda, cadastro):

    if idade < 18:
        return "Usuário menor de idade."

    elif renda < 1500:
        return "Usuário maior de idade, mas possui renda baixa."

    elif cadastro == "inativo":
        return "Usuário maior de idade, renda suficiente, mas cadastro inativo."

    else:
        return "Usuário aprovado."
