try:
    with open("alunos.txt", "r") as arquivo:
        print("Arquivo aberto com sucesso!")

        conteudo = arquivo.read()
        print(conteudo)

except FileNotFoundError:
    print("Erro: o arquivo 'alunos.txt' não foi encontrado.")
    print("Verifique se o arquivo existe e se o nome está correto.")
