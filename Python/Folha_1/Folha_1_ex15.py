def calcular_soma(erro):
    n = 0
    soma = 0
    termo = (2 ** n + 3 ** n) / 6 ** n

    while abs(termo) > erro:
        soma += (-1) ** n * termo
        n += 1
        termo = (2 ** n + 3 ** n) / 6 ** n

    return soma

erro = float(input("Digite o valor do erro permitido: "))
resultado = calcular_soma(erro)
print(f"A soma da série com erro inferior a {erro} é aproximadamente {resultado:.6f}")
