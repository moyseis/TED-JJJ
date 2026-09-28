
try:
   
    nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
    nota2 = float(input("Digite a segunda nota: ").replace(",", "."))
    nota3 = float(input("Digite a terceira nota: ").replace(",", "."))

    
    if any(n < 0 or n > 10 for n in [nota1, nota2, nota3]):
        print("Erro: As notas devem ser valores entre 0 e 10.")
    else:
      
        media = (nota1 + nota2 + nota3) / 3
        print(f"A média final calculada é: {media:.2f}")

except ValueError:
    print("Erro: Digite apenas números válidos para as notas.")
