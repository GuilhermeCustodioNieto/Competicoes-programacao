tamanho = int(input())
while (tamanho != 0):
    numeros = list(map(int, input().split()))
    soma = 0
    menorValor = 0
    for n in numeros:
        soma += n
        if(soma < 0):
            menorValor = soma
    print(soma)
    print(menorValor)
    tamanho = int(input())