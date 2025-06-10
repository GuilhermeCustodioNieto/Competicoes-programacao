# ler o número de premiados
# ler o n inteiro, onde 1 == Pequena e 2 == Média
# ler o número de camisetas médias produzidas

numPremiados = int(input())
camisetasPerdidas = map(int, input().split())
numPequenasFeitas = int(input())
numMediasFeitas = int(input())

numPequena = 0
numMedia = 0

for camiseta in camisetasPerdidas:
    if camiseta == 1:
        numPequena += 1
    else:
        numMedia += 1

if((numPequena == numPequenasFeitas) and (numMedia == numMediasFeitas)):
    print('S')
else:
    print('N')