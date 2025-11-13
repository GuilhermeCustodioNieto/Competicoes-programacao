tamanho = int(input())
while (tamanho != 0):
    valores = list(map(int, input().split()))
    
    valores.sort(reverse=True)
    maior = valores[0]
    valores.sort()
    menor = valores[0]
    media = sum(valores) // tamanho

    print(str(menor) + " " + str(maior) + " " + str(media))
    tamanho = int(input())