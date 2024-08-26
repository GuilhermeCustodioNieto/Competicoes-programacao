inicio = int(input())

rodadas = 0

def transformaMatriz(vetor):
    temp = str(vetor)

    vetorFinal = []

    for i in temp:
        vetorFinal.append(i)

    return vetorFinal

while inicio != 0:
    vetorAtual = transformaMatriz(inicio)
    vetorAtual.sort(reverse=True)
    rodadas += 1
    inicio -= int(vetorAtual[0])

print(rodadas)