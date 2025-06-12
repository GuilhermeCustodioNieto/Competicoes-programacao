n, numPassos = map(int, input().split())
matriz = []

for i in range(0, numPassos + 5):
    matriz.append([])
    for j in range(numPassos + 5):
        matriz[i].append(0)


for i in range(0, n):
    entrada = input()
    for letra in range(0, len(entrada)):
        if(entrada[letra] == '1'):
            matriz[i][letra] = int(entrada[letra])




for passo in range(0, numPassos):
    copiaMatriz = matriz

    for i in range(0, n):
        for j in range(0, n):
            contagemAoRedor = 0
            valorAtual = matriz[i][j]
            if(matriz[i - 1][j - 1] == 1): contagemAoRedor += 1
            if(matriz[i - 1][j] == 1): contagemAoRedor += 1
            if(matriz[i - 1][j + 1] == 1): contagemAoRedor += 1
            if(matriz[i][j - 1] == 1): contagemAoRedor += 1
            if(matriz[i][j + 1] == 1): contagemAoRedor += 1
            if(matriz[i + 1][j - 1] == 1): contagemAoRedor += 1
            if(matriz[i + 1][j] == 1): contagemAoRedor += 1
            if(matriz[i + 1][j + 1] == 1): contagemAoRedor += 1

            if(valorAtual == 0 and contagemAoRedor == 3):
                copiaMatriz[i][j] = 1
            elif(valorAtual == 0 and contagemAoRedor != 3):
                copiaMatriz[i][j] = 0
            elif(valorAtual == 1 and (contagemAoRedor == 3 or contagemAoRedor == 2)):
                copiaMatriz[i][j] = 1
            elif(valorAtual == 1 and (contagemAoRedor < 2 or contagemAoRedor > 3)):
                copiaMatriz[i][j] = 0

    matriz = copiaMatriz

    print()
    for i in range(0, n):
        for j in range(0, n):
            print(matriz[i][j], end='')
                    
        print()

