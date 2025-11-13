tamanho = int(input())
while(tamanho != 0):
    valores = map(int, input().split())
    soma = 0
    for i in valores:
        soma += int(i * 0.9)

    print(soma)
    tamanho = int(input())
