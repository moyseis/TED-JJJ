
temperaturas = [23.5, 18.0, 31.2, -2.5, 31.2, 0.0, -5.4, 28.1]

if not temperaturas:
    print("Nenhuma temperatura foi registrada.")
else:
  
    maior = temperaturas[0]
    menor = temperaturas[0]

    
    for temp in temperaturas:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp

    print(f"Temperatura máxima: {maior}°C")
    print(f"Temperatura mínima: {menor}°C")
