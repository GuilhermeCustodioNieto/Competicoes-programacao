m, n = map(int, input().split())

matriz = []
contador = 0

for i in range(m):
    miniLista = []
    for j in (map(int, input().split())):
        miniLista.append(j)
    matriz.append(miniLista)

p = int(input())
for i in range(p):
    linha, coluna = map(int, input().split())
    coluna-=1
    linha-=1
    if(matriz[linha][coluna] >= 1):
        matriz[linha][coluna] -= 1
        contador+=1

print(contador)